from django.db import models


CATEGORY_CHOICES = (
    ("PR", "Происшествия"),
    ("POL", "Политика"),
    ("SP", "Спорт"),
    ("KU", "Культура")
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default="SP")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title