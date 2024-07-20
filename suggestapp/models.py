from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    any_suggestions = models.CharField(max_length=100)
    improve = models.CharField(max_length=100)

class new_prompt(models.Model):
    prompt = models.CharField(max_length=1000)
    label_l = models.CharField(max_length=100)
    label_2 = models.CharField(max_length=100)
    label_3 = models.CharField(max_length=100)
    label_n = models.CharField(max_length=100)
    output  = models.CharField(max_length=1000)