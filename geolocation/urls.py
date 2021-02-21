from django.urls import path

from . import views

urlpatterns = [
    path('geolocation/', views.GeolocationCreate.as_view(), name='add_geolocation'),
    path('geolocation/<str:ip>', views.GeolocationRetrieveDestroy.as_view(), name='geolocation'),
    path('login/', views.login, name='login')
]
