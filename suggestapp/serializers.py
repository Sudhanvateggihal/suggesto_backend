from rest_framework import serializers
from .models import feedback, new_prompt

class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'  # Correct way to include all fields

class new_promptSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_prompt
        fields = '__all__'  # Correct way to include all fields
