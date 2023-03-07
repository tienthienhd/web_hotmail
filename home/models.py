from django.db import models
from datetime import datetime

# Create your models here.
from django.db.models import ForeignKey, SET_NULL
from django.utils.translation import gettext_lazy


class StatusChoices(models.TextChoices):
    SUBMITTED = 'submitted', gettext_lazy('submitted')
    LIVE = 'live', gettext_lazy('live')
    DIE = 'die', gettext_lazy('die')
    SOLD = 'sold', gettext_lazy('sold')


class RegisterStatusChoices(models.TextChoices):
    SUCCESS = 'success', gettext_lazy('success')
    FAILED = 'failed', gettext_lazy('failed')
    HAS_REGISTER_BEFORE = 'has_registered', gettext_lazy('has_registered')


class RegisteredEmail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=15)
    dob = models.DateField()

    register_status = models.CharField(max_length=50,
                                       choices=RegisterStatusChoices.choices,
                                       default=RegisterStatusChoices.FAILED)

    status = models.CharField(max_length=30,
                              choices=StatusChoices.choices,
                              default=StatusChoices.SUBMITTED)
    country_code = models.CharField(max_length=10, null=True)
    country_name = models.CharField(max_length=50, null=True)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "registered_mail"
