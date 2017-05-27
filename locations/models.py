from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from civic_map import settings


class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10240)
    latitude = models.DecimalField(max_digits=20, decimal_places=18)
    longitude = models.DecimalField(max_digits=20, decimal_places=18)
    program = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    _credibility = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        default=0.0,
        db_column='credibility'
    )

    @property
    def credibility(self):
        return min(1, max(self._credibility, 0))

    @credibility.setter
    def credibility(self, value):
        self._credibility = min(1, max(value, 0))


    # putem folosi un ImageField pentru o poza cu locatia
    # https://docs.djangoproject.com/en/1.10/ref/models/fields/#imagefield

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def get_absolute_url(self):
        return reverse('locations:view', args=[self.id])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


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

    content = models.TextField(max_length=65535, blank=True, null=True)
    mark = models.PositiveSmallIntegerField(
        choices=MARK_CHOICES,
        default=MARK_5,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-id']

    # pentru unique ar trebui folosit ceva gen
    # https://stackoverflow.com/questions/2270808/compound-composite-primary-unique-key-with-django
    # doar ca am impresia ca elimina primary key-ul
    # asa ca sau trebuie declarat id ca primary key separat
    # sau putem folosi alea ca primary key si vedem cum se comporta
    # need testing
