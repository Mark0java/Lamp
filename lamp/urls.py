from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^store$', views.view_store, name='store'),
    url(r'^get_on_off$', views.get_on_off, name='get_on_off'),
    url(r'^send_on_off$', views.send_on_off, name='send_on_off'),
    url(r'^get_rotations$', views.get_rotations, name='get_rotations'),
    url(r'^send_rotations$', views.send_rotations, name='send_rotations'),
    url(r'^get_up_down$', views.get_up_down, name='get_up_down'),
    url(r'^send_up_down$', views.send_up_down, name='send_up_down'),
    url(r'^get_brightness$', views.get_brightness, name='get_brightness'),
    url(r'^send_brightness$', views.send_brightness, name='send_brightness'),
]