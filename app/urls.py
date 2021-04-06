from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('monitoring/', views.hello_world),
    path('device/', views.device, name='device'),
    path('deviceshow/', views.device_show, name='device_show'),
    path('deviceedit/<int:tbl_device_info_id>', views.device_edit, name='device_edit'),
    path('devicedelete/<int:tbl_device_info_id>', views.device_destroy, name='device_delete'),
    path('person/', views.person, name='person'),
    path('personshow/', views.person_show, name='person_show'),
    path('personedit/<int:tbl_person_info_id>', views.person_edit, name='person_edit'),
    path('persondelete/<int:tbl_person_info_id>', views.person_destroy, name='person_delete'),
    path('total/', views.total_table, name='total'),
    path('marker/', views.show_tjs, name='show_tjs'),


]
