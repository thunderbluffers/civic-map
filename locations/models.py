from django.db import models
from civic_map import settings

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10240)
    coordinates_x = models.DecimalField(max_digits=9, decimal_places=6)
    coordinates_y = models.DecimalField(max_digits=9, decimal_places=6)
    program = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # putem folosi un ImageField pentru o poza cu locatia
    # https://docs.djangoproject.com/en/1.10/ref/models/fields/#imagefield

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('locations:view', args=[str(self.id)])

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Review(models.Model):
    MARK_1 = 1
    MARK_2 = 2
    MARK_3 = 3
    MARK_4 = 4
    MARK_5 = 5
    MARK_CHOICES = (
        (MARK_1, 'Mark 1'),
        (MARK_2, 'Mark 2'),
        (MARK_3, 'Mark 3'),
        (MARK_4, 'Mark 4'),
        (MARK_5, 'Mark 5'),
    )

    content = models.TextField(max_length=65535)
    mark = models.PositiveSmallIntegerField(
        choices=MARK_CHOICES,
        default=MARK_1,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )

    # pentru unique ar trebui folosit ceva gen
    # https://stackoverflow.com/questions/2270808/compound-composite-primary-unique-key-with-django
    # doar ca am impresia ca elimina primary key-ul
    # asa ca sau trebuie declarat id ca primary key separat
    # sau putem folosi alea ca primary key si vedem cum se comporta
    # need testing

