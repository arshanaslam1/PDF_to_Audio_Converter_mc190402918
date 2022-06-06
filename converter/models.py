from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from accounts.models import User
from converter.utils import convert_pdf_to_audio

AUDIO_VOICES = (
    ( 0, 'Male'),
    ( 1, 'Female')
)


class PDFAudio(models.Model):

    class AudioVoice(models.IntegerChoices):
        Male = 0
        Female = 1

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    pdf = models.FileField(upload_to='pdfs', validators=[FileExtensionValidator(['pdf'])])
    audio_file = models.FileField(upload_to='recs', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('converter:pdf-home')

    def audio_url(self):
        try:
            return self.audio_file.url
        except:
            return None

