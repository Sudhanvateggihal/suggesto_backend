from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import feedbackViewSet,new_promptViewSet,LlamaAPIView, ApiProviderViewSet, ChatModelsViewSet


router = DefaultRouter()
router.register(r'feedbacks', feedbackViewSet)
router.register(r'new_prompts', new_promptViewSet)
router.register(r'api_providers', ApiProviderViewSet)
router.register(r'chat_models', ChatModelsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('llama-ap/', LlamaAPIView.as_view(), name='llama_ap'),
]