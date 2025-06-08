from django.shortcuts import render
from rest_framework import viewsets
from .models import Agent, AgentInteraction, AgentFeedback
from .serializers import AgentSerializer, AgentInteractionSerializer, AgentFeedbackSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentInteractionViewSet(viewsets.ModelViewSet):
    queryset = AgentInteraction.objects.all()
    serializer_class = AgentInteractionSerializer

class AgentFeedbackViewSet(viewsets.ModelViewSet):
    queryset = AgentFeedback.objects.all()
    serializer_class = AgentFeedbackSerializer

# Create your views here.
