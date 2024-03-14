from django import forms

class UploadAbsenceFileForm(forms.Form):
    file = forms.FileField(label='', label_suffix='', allow_empty_file=False, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'form-browse-btn'})