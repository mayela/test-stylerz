from datetime import timedelta

from django.db import models

from userprofiles.models import UserProfile


class Date(models.Model):
    TYPE_OF_TREATMENT = (
            (1, 'Manicure'),
            (2, 'Pedicure'),
            (3, 'Corte de cabello'),
            (4, 'Tinte'),
            (5, 'Masaje'),
            )
    treatment_type = models.PositiveSmallIntegerField(choices=TYPE_OF_TREATMENT)
    customer = models.ForeignKey(UserProfile, related_name='dates_by_customer', limit_choices_to={'is_customer': True})
    specialist = models.ForeignKey(UserProfile, related_name='dates_by_specialist', limit_choices_to={'is_specialist': True})
    start_datetime = models.DateTimeField('Start datime')
    end_datetime = models.DateTimeField('End datime', blank=True)

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

    def __str__(self):
        return self.customer.user.username + ' ' + self.start_datetime.strftime('%A %d/%B/%Y %H:%M')

    def save(self, *args, **kwargs):
        self.end_datetime = self.start_datetime + timedelta(minutes=30)
        super(Date, self).save(*args, **kwargs)
