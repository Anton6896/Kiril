from django.db import models


class Statistic(models.Model):
    """
    class represents Statistics
    for better calculating reasons added default values as 1 to all not text fields
    """
    views = models.IntegerField(blank=True, null=True, default=1)
    clicks = models.IntegerField(blank=True, null=True, default=1)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=1, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    # db name apiaries
    class Meta:
        db_table = 'statistic'

    def __str__(self):
        return str(self.pk)
