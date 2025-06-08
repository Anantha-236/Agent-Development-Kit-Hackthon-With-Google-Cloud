from django.contrib import admin
from .models import Agent, AgentInteraction, AgentFeedback

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')

@admin.register(AgentInteraction)
class AgentInteractionAdmin(admin.ModelAdmin):
    list_display = ('agent', 'created_at', 'confidence_score')
    search_fields = ('agent__name', 'input_text', 'response_text')
    list_filter = ('agent', 'created_at')

@admin.register(AgentFeedback)
class AgentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('interaction', 'user', 'rating', 'created_at')
    search_fields = ('interaction__agent__name', 'user__username', 'comment')
    list_filter = ('rating', 'created_at')
