from django import forms
from .models import Location

from easy_maps.widgets import AddressWithMapWidget


class LocationForm(forms.ModelForm):
    address = forms.CharField(
        widget=AddressWithMapWidget({
            'class': 'vTextField'
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
        exclude = ['user', 'tags']
