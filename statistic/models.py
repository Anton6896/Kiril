from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class Statistic(models.Model):
    """
    class represents Statistics
    for better calculating reasons added default values as 1 to all not text fields
    """
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField()

    # db name apiaries
    class Meta:
        db_table = 'statistic'
        indexes = [models.Index(fields=['date'])]

    def __str__(self):
        return f"stat: {str(self.pk)}, date:{self.date}"


def statistics_data_updater(sender, instance, created, *args, **kwargs):
    """
    additional check ig data is None change in db
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
        if instance.date is None:
            instance.date = timezone.now()
            instance.save()


post_save.connect(statistics_data_updater, sender=Statistic)
