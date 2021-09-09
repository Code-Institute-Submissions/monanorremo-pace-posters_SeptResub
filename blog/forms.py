from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form'}),
            'slug': forms.TextInput(attrs={'class': 'form'}),
            'author' : forms.Select(attrs={'class': 'form'}),
            'content' : forms.Textarea(attrs={'class': 'form'}),
            }

    image = forms.ImageField(label='Image', required=False)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            }

