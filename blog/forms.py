from django import forms
from .models import Post


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
