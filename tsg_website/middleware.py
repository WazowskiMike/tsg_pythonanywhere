from datetime import datetime, timedelta
from django.utils.cache import patch_response_headers

class SetExpiresHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Устанавливаем время кэширования на 7 дней
        expiration_time = datetime.utcnow() + timedelta(days=7)

        # Рассчитываем количество секунд до истечения срока действия
        cache_timeout = (expiration_time - datetime.utcnow()).total_seconds()

        # Устанавливаем Expires header
        patch_response_headers(response, cache_timeout=cache_timeout)

        return response
