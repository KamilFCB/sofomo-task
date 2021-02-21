import requests
import time

from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from sofomo_task.settings import IPSTACK_API, JWT_KEY
from .serializers import GeolocationSerializer
from rest_framework.response import Response
from .models import Geolocation
from rest_framework import generics
from jwt import encode
from django.core.cache import cache


class GeolocationRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """
        Retrieve or delete a geolocation instance.
    """

    def get_object(self, ip):
        try:
            return Geolocation.objects.get(ip=ip)
        except Geolocation.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        ip = kwargs['ip']
        cache_response = cache.get(ip)
        if cache_response is None:
            geolocation = self.get_object(ip=ip)
            serializer = GeolocationSerializer(geolocation)
            cache.set(ip, serializer.data, 3600)
            return Response(serializer.data)
        return Response(cache_response)

    def delete(self, request, *args, **kwargs):
        ip = kwargs['ip']
        geolocation = self.get_object(ip=ip)
        geolocation.delete()
        cache.delete(ip)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GeolocationCreate(generics.CreateAPIView):
    """
        Create a geolocation instance.
    """

    def post(self, request, *args, **kwargs):
        ip = request.data['ip']
        if Geolocation.objects.filter(ip=ip).exists():
            return JsonResponse(
                {"detail": 'Geolocation data already exists in the database for this IP address'},
                status=status.HTTP_409_CONFLICT
            )
        requested_fields = 'ip,type,continent_name,country_name,region_name,city,zip,latitude,longitude'
        response = requests.get(
            'http://api.ipstack.com/{}?access_key={}&fields={}'.format(ip, IPSTACK_API, requested_fields)
        )
        try:
            if response.json()['success'] == 'false':
                return JsonResponse({"detail": response.json()['info']}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            pass

        serializer = GeolocationSerializer(data=response.json())
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return JsonResponse({"detail": 'The requested resource does not exist.'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse(
            {"detail": 'Method {} not allowed.'.format(request.method)}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == 'admin':
        payload = {
            "username": username,
            "exp": time.time() + 300,

        }
        token = encode(payload, JWT_KEY, algorithm="HS256")
        return JsonResponse({"access_token": token}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"detail": 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
