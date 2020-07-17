from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200,help_text="Title of Article")
    desc = models.CharField(max_length=500, help_text="Short Description of the Article")
    date_modified = models.DateField(auto_now=True)
    article_text = models.TextField()

    def __str__(self):
        return self.title

