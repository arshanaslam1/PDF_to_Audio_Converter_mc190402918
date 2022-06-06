from converter.models import PDFAudio
from converter.utils import convert_pdf_to_audio
from settings.celery import app


@app.task
def generate_audio(obj_id):
    obj = PDFAudio.objects.get(pk=obj_id)
    file_name = convert_pdf_to_audio(obj)
    obj.audio_file = file_name
    obj.save()



