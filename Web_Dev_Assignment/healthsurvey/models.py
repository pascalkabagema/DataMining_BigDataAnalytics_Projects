from django.db import models

from django.db import models

class HealthSurvey(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    health_condition = models.CharField(max_length=100)
    exercise_frequency = models.CharField(max_length=50)
    remarks = models.TextField(blank=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
