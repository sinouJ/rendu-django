from django import forms
from .models import PostCV

class PostCVForm(forms.ModelForm):

    class Meta:
        model = PostCV
        fields = ('title', 'description', 'fileCV')