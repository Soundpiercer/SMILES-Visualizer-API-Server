from django import forms


class GenerateForm(forms.Form):
    keyword = forms.CharField(required=True, max_length=100)


class CompareForm(forms.Form):
    mole1 = forms.CharField(required=True, max_length=50)
    mole2 = forms.CharField(required=True, max_length=50)


class SavedListForm(forms.Form):
    pass