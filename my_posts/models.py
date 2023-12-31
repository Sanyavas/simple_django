from django.db import models


class Quote(models.Model):
    title = models.CharField(max_length=100)
    quote = models.CharField(max_length=3000)
    author = models.CharField(max_length=100)
    picture = models.CharField(null=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
