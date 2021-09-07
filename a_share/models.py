from django.db import models


class IndexInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField()
    name = models.CharField()
    display_name = models.CharField()
    type = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()


class DayK(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    amount = models.FloatField()
    turnover = models.FloatField()
    date = models.DateField()

    class Meta:
        index_together = [
            ['code', 'date'],
        ]
