from django.db import models


class EventPlan(models.Model):
    title = models.CharField(max_length=100)
    short_msg = models.CharField(max_length=500)
    caption_image = models.ImageField(upload_to='event_image')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


class EventImage(models.Model):
    event = models.ForeignKey(
        to='event_plans.EventPlan',
        on_delete=models.CASCADE,
        related_name='event_images'
    )
    image = models.ImageField(upload_to='event_images')