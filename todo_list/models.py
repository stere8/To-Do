from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your models here.


class task(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    due_date = models.DateTimeField(null=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        super(task,self).clean()
        now = timezone.make_aware(datetime.datetime.now())
        if self.due_date < now:
            raise ValidationError('The time should be later than now')





