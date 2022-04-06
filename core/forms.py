from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        fields = ('author', 'text','content',)