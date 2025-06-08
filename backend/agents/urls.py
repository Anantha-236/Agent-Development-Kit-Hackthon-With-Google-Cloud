from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, AgentInteractionViewSet, AgentFeedbackViewSet

app_name = 'agents'

router = DefaultRouter()
router.register(r'', AgentViewSet, basename='agent')
router.register(r'interactions', AgentInteractionViewSet, basename='agentinteraction')
router.register(r'feedback', AgentFeedbackViewSet, basename='agentfeedback')

urlpatterns = router.urls
