from django.forms import ModelForm
from candidature.models import PostCV

class PostCVForm(ModelForm):
    class Meta:
        model = PostCV
        fields = ['upload']

form = PostCVForm()

