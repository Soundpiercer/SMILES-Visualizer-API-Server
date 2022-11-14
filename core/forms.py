from django import forms


class GenerateForm(forms.Form):
    keyword = forms.CharField(required=True, max_length=100)


class CompareForm(forms.Form):
    pass


class SavedListForm(forms.Form):
    pass