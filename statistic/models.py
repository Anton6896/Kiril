
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class Statistic(models.Model):
    """
    class represents Statistics
    for better calculating reasons added default values as 1 to all not text fields
    """
    views = models.IntegerField(blank=True, null=True, default=1)
    clicks = models.IntegerField(blank=True, null=True, default=1)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=1, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now())

    # db name apiaries
    class Meta:
        db_table = 'statistic'

    def __str__(self):
        return str(self.pk)


def statistics_data_updater(sender, instance, created, *args, **kwargs):
    """
    in case if statistics object created without data
    change None fields to 1 for calculations
    """
    # create Profile for ech user (Singleton)
    if created:
        if instance.views is None:
            instance.views = 1
            instance.save()
        if instance.clicks is None:
            instance.clicks = 1
            instance.save()
        if instance.cost is None:
            instance.cost = 1
            instance.save()


post_save.connect(statistics_data_updater, sender=Statistic)
