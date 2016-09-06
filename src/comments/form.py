from django import forms

class CommentForm(forms.Form):
    content_type = forms.CharField(widget = forms.HiddenInput)

