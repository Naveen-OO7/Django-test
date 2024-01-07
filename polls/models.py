from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Session(models.Model):
    """
    Model to store data regarding sessions
    """
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_created=True, null=False, auto_now=True)
    speaker = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    total_entry = models.IntegerField()

    def __str__(self):
        return self.name + " by " + self.speaker.first_name