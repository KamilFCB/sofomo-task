from django.http import HttpResponse, JsonResponse
from jwt import decode, InvalidSignatureError, ExpiredSignatureError
from rest_framework import status

from sofomo_task.settings import JWT_KEY


class AuthorizationMiddleware:
    """
        Access token verification middleware
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if callback.__name__ == 'login':
            return None
        try:
            token = request.headers['Authorization'].split()[1]
            decoded = decode(token, JWT_KEY, algorithms="HS256")
            if decoded['username'] != 'admin':
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        except KeyError:
            return JsonResponse(
                {"detail": 'Request requires Authorization header'}, status=status.HTTP_401_UNAUTHORIZED
            )
        except InvalidSignatureError:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        except ExpiredSignatureError:
            return JsonResponse({"detail": 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)

