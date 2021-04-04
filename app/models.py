from django.db import models

class TBL_DEVICE_INFO(models.Model):
    status = models.BooleanField()
    station = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    install_date = models.DateField()

    def __str__(self):
        return str(self.id)


class TBL_PERSON_INFO(models.Model):
    degree = models.FloatField()
    has_mask = models.BooleanField()
    reg_date = models.DateTimeField(auto_now_add=True)
    device_id = models.ForeignKey(
        TBL_DEVICE_INFO,
        on_delete = models.CASCADE,
        null = False,
    )

    # img = models.BinaryField(blank=True)

    def __str__(self):
        return str(self.degree)


class TBL_TOTAL_INFO(models.Model):
    device_id = models.IntegerField()
    total_pop = models.IntegerField()
    mask_pop = models.IntegerField()
    high_temp_pop = models.IntegerField()
    region = models.CharField(max_length=50)

    def __str__(self):
        return str(self.total_app)



