from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
    link = forms.CharField(label="Submit URL", validators=[validate_url])
