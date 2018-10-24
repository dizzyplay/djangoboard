from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'id': 'title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '10',
                'id': 'content',
            }),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }
