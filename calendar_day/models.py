from django.db import models
from django.core.validators import MaxValueValidator
from aulas.models import Aula
from reservations.models import Reservation

# Create your models here.

class CalendarBlock(models.Model):
    aula_id = models.ForeignKey(Aula, related_name='calendar_block', on_delete=models.CASCADE)
    month = models.IntegerField(validators=[MaxValueValidator(11)],null=False, blank=False)
    date_num = models.IntegerField(validators=[MaxValueValidator(31)],null=False, blank=False)
    week_day = models.IntegerField(validators=[MaxValueValidator(6)],null=False, blank=False)
    timeblock = models.CharField(max_length=10, blank=False, null=False)
    reservation_id = models.ForeignKey(Reservation, related_name="calendar_block", related_query_name='calendar_block', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.month}-{self.date_num}-{self.timeblock}"