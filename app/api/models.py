from django.db import models


class WildfireReport(models.Model):
    id = models.AutoField(primary_key=True)
    town = models.CharField(max_length=255)
    reported_by = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id}"
