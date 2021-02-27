from django import forms
from django.core.exceptions import ValidationError

from .models import Post


widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control"
    }
)

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control"
    }
)


class TextForm(forms.Form):
    text = forms.CharField(label="", widget=widget_textarea)
    search = forms.CharField(label="Search characters", widget=widget_textinput)
    replace = forms.CharField(label="Replace to", widget=widget_textinput)

    def clean(self):
        data = super().clean()
        text = data["text"]

        if len(text) <= 5:
            raise ValidationError("Text must be longer than 5 letters!")

        return data


# Model form (auto generate form based on model)
class PostForm(forms.ModelForm):
    # Inherite form
    class Meta:
        model = Post
        fields = ["title", "body"]
