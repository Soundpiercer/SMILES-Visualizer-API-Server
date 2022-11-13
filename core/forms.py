from django import forms


class GenerateForm(forms.Form):
    keyword = forms.CharField(required=True, max_length=100)