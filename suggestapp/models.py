from queue import Full
from django.db import models

# Create your models here.
class feedback(models.Model):
    # feedback_id = models.AutoField(primary_key=True)
    any_suggestions = models.CharField(max_length=100)
    improve = models.CharField(max_length=100)

class new_prompt(models.Model):
    prompt_name = models.CharField(max_length=1000,default='null')
    prompt = models.CharField(max_length=1000)
    # label_l = models.CharField(max_length=100)
    # label_2 = models.CharField(max_length=100)
    # label_3 = models.CharField(max_length=100)
    # label_n = models.CharField(max_length=100)
    output  = models.CharField(max_length=1000)

class ApiProvider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=50)    

class ChatModels(models.Model):
    chat_model_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(ApiProvider, on_delete=models.CASCADE,db_index=True)
    chat_model_name = models.CharField(max_length=60)   