from django.conf import settings



GOOGLE_TRANSLATOR_BASE_URL = getattr(settings, 'GOOGLE_TRANSLATOR_BASE_URL',  'https://translate.google.com/') 
GOGGLE_RESULT_DIV_CONTAINER_CLASS = getattr(settings, 'GOGGLE_RESULT_DIV_CONTAINER_CLASS', 'result-container')