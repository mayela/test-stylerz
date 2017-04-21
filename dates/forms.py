from django.forms import ModelForm

from dates.models import Date


class DateForm(ModelForm):

    class Meta:
        model = Date
        fields = ('treatment_type', 'customer', 'specialist', 'start_datetime')
