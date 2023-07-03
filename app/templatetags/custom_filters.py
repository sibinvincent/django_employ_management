from django import template
from django.utils import timezone


register = template.Library()

@register.filter
def calculate_experience(created):
    now = timezone.now()
    experience = now - created
    days = experience.days
    hours, remainder = divmod(experience.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f" {days} days {hours:02d} hours and {minutes:02d}  minutes"
