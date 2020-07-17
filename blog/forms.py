from django.forms import ModelForm
from . import models

class ArticleForm(ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title', 'desc', 'article_text']