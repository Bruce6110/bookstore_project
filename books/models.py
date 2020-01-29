import uuid  # new. Universally Unique ID

from django.db import models
from django.urls import reverse  # new

# Create your models here.


class Book(models.Model):
    # override the default id
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    # new. This sets the canonical url.  Necessary when using 'reverse()' function
    def get_absolute_url(self):
        # preferred way, per WSV
        return reverse('book_detail', args=[str(self.id)])
