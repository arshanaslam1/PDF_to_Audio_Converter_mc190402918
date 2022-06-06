from django.conf import settings

import os
import pyttsx3
import fitz
from uuid import uuid4


def extract_text(filename):
    doc = fitz.open(filename)
    text = ""
    if doc.page_count > 500:
        pages = 500
    else:
        pages = doc.page_count
    for pageNum in range(pages):
        page = doc[pageNum]
        text += page.get_text("text")
    return text


def store_audio_file(filepath, text):

    engine = pyttsx3.init()
    engine.save_to_file(text, filepath)
    engine.runAndWait()
    engine.stop()


def convert_pdf_to_audio(instance):
    text = extract_text(instance.pdf.path)
    file_name = uuid4()
    filepath = os.path.join(settings.BASE_DIR, f'media/recs/{file_name}.mp3')
    store_audio_file(filepath, text)
    file_name = f'recs/{file_name}.mp3'
    return file_name
