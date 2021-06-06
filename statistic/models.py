from django.db import models


class Statistic(models.Model):
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'statistic'

    def __str__(self):
        return str(self.pk)
