from django import forms

class UploadForm(forms.Form):
    bestand = forms.FileField(
        label='Selecteer je ABN AMRO exportbestand (.TAB) \n',
    )
