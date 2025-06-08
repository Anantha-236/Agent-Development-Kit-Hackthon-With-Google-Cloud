from rest_framework import serializers
from .models import Agent, AgentInteraction, AgentFeedback

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class AgentInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentInteraction
        fields = '__all__'

class AgentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentFeedback
        fields = '__all__'
