from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
    link = forms.CharField(
        label="",
        validators=[validate_url],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the URL",
                "class": "form-control"
            }
        )
    )
