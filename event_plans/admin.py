from django.contrib import admin
from .models import EventPlan, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage


@admin.register(EventPlan)
class EventPlanAdmin(admin.ModelAdmin):
    inlines = [
        EventImageInline
    ]
    fieldsets = (
        ('caption', {
            'fields': [('title', 'short_msg')]
        }),
        ('images', {
            'fields': ['caption_image']
        }),
    )
