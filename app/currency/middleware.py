import time
from .models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        processing_time = int((time.time() - start_time) * 1000)

        log_entry = RequestResponseLog(
            path=request.path,
            request_method=request.method,
            time=processing_time
        )

        log_entry.save()

        return response
