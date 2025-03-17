from django.db import models

class UploadedJSONFile(models.Model):
    file = models.FileField(upload_to='json_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserAVG(models.Model):
    user_id = models.IntegerField(primary_key=True)
    global_avg = models.DecimalField(max_digits=5, decimal_places=2)
    vio_avg = models.DecimalField(max_digits=5, decimal_places=2)
    will_avg = models.DecimalField(max_digits=5, decimal_places=2)
    swift_avg = models.DecimalField(max_digits=5, decimal_places=2)
    des_avg = models.DecimalField(max_digits=5, decimal_places=2)