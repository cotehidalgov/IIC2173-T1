from django import forms

class PostsForm(forms.Form):
    text = forms.CharField(
      widget=forms.Textarea(
        attrs={
          "rows": "5",
          "class": "form-control",
          "placeholder":"Message",
          "id":"message",
          "required": "",
          "data-validation-required-message": "Please enter a message.",
          "aria-invalid": "false"
          }), 
      label='Type here:', 
      max_length=1000)
