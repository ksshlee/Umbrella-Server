from django import forms


# url 폼
class UrlForm(forms.Form):
    url = forms.CharField(max_length=256)