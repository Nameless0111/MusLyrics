from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }