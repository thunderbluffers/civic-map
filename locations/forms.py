from django import forms
from .models import Location, Review

from easy_maps.widgets import MapWidget


class LocationForm(forms.ModelForm):
    address = forms.CharField(
        widget=MapWidget({
            'class': 'vTextField',
            'size': 60,
            'hidden': True,
        }),
        initial='Bucharest, Romania',
    )

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        instance = kwargs.get('instance', None)
        if instance is not None:
            self.fields['address'].initial = \
                '%.16f, %.16f' % (instance.latitude, instance.longitude)

    class Meta:
        model = Location
        exclude = ('user', 'tags')
        widgets = {
            'latitude': forms.NumberInput({'size': 26}),
            'longitude': forms.NumberInput({'size': 26}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'location')
