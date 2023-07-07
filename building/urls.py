from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'building'

urlpatterns = [
    path('', views.register_building, name='registration'),
    path('registration/success/', views.registration_success, name='registration_success'),
    path('building_list/', views.building_list, name='building_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
