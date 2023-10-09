import os
from celery import Celery
import asyncio

from server.cover_letter_generator import get_cover_letter


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")
celery.conf.task_default_queue = os.environ.get("CELERY_DEFAULT_QUEUE", "coverlettergen")

@celery.task(name="generate")
def generate_cover_letter_task(resume, job_description, extra_information, to):
    # use the cover letter generator to generate a cover letter
    return asyncio.run(get_cover_letter(job_description, resume, extra_information=extra_information, model="gpt-4", to=to))