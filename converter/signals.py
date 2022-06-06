from django.db.models.signals import post_save
from django.dispatch import receiver
from converter.models import PDFAudio
from converter.tasks import generate_audio


@receiver(post_save, sender=PDFAudio)
def profile_create(sender, instance, created, **kwargs):
    if created:
        generate_audio.delay(instance.id)
