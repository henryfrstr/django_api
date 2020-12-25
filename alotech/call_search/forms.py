from django import forms


class Search(forms.Form):
    startdate = forms.DateTimeField()
    finishdate = forms.DateTimeField()
