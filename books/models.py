import uuid  # new. Universally Unique ID

from django.db import models
from django.urls import reverse  # new
from django.contrib.auth import get_user_model


class Book(models.Model):
    # override the default id
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)  # new

    def __str__(self):
        return self.title

    # new. This sets the canonical url.  Necessary when using 'reverse()' function
    def get_absolute_url(self):
        # preferred way, per WSV
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    # book is the one-to-many foreign key.  Standard practice is to nmae it the same as the linked model
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name='reviews',
    )

    review = models.CharField(max_length=255)

    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.review
