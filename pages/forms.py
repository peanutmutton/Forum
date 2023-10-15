from django import forms

class PostForm(forms.Form):
    text_field = forms.CharField(widget=forms.Textarea)