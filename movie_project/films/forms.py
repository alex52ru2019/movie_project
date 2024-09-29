from .models import films_posts
from django.forms import ModelForm, TextInput, Textarea

class films_postsForm(ModelForm):
    class Meta:
        model = films_posts
        fields = ['films_name', 'films_text', 'films_review']
        widgets = {
            'films_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'films_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'films_review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),

        }