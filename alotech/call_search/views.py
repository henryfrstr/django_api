from django.shortcuts import render
from decouple import config
import requests
from .forms import Search

BASE_URL = config("root_api")

# Listede görüntülecek alanlar:
#     1.Calldate
#     2.Called_num
#     3.Callerid
#     4.Answered
#     5.Duration


def home(request):
    form = Search()
    # print(request.GET.get("startdate"))

    if request.GET.get("startdate") and request.GET.get("finishdate"):
        start_date = request.GET.get("startdate")
        end_date = request.GET.get("finishdate")
        print(start_date)
        print(end_date)
    else:
        start_date = "2017-08-01%2012:00:00"
        end_date = "2017-08-04%2013:00:00"

    api_url = BASE_URL.format(start_date, end_date)

    response = requests.get(api_url)
    # print(response)
    if response.status_code == 200:
        content = response.json()
        calldate = content["CallList"][0]["calldate"]
        call_num = content["CallList"][0]["called_num"]
        caller_id = content["CallList"][0]["callerid"]
        answered = content["CallList"][0]["answered"]
        duration = content["CallList"][0]["duration"]

        # print(calldate)
        context = {
            "calldate": calldate,
            "call_num": call_num,
            "caller_id": caller_id,
            "answered": answered,
            "duration": duration,
            "form": form
        }
    else:
        context = {
            "error": "Invalid Input",
            "form": form
        }

    return render(request, "call_search/home.html", context)
