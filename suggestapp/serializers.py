from rest_framework import serializers
from .models import feedback, new_prompt, ApiProvider, ChatModels

class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'  # Correct way to include all fields

class new_promptSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_prompt
        fields = '__all__'  # Correct way to include all fields

class ApiProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiProvider
        fields = '__all__'

class ChatModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModels
        fields = '__all__'