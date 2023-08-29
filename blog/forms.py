from .models import Comment
from django.forms import ModelForm

from .models import Image

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
