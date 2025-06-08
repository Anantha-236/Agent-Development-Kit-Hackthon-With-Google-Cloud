from django.db import models
from django.conf import settings

class Agent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AgentInteraction(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='interactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    input_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    confidence_score = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.agent.name} interaction at {self.created_at}"

class AgentFeedback(models.Model):
    class Rating(models.IntegerChoices):
        POOR = 1, 'Poor'
        FAIR = 2, 'Fair'
        GOOD = 3, 'Good'
        VERY_GOOD = 4, 'Very Good'
        EXCELLENT = 5, 'Excellent'

    interaction = models.ForeignKey(AgentInteraction, on_delete=models.CASCADE, related_name='feedback')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['interaction', 'user']

    def __str__(self):
        return f"Feedback for {self.interaction.agent.name} by {self.user.username}"
