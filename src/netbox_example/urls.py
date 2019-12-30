from django.urls import path

from . import views

urlpatterns = [
    path('example/', views.ExampleListView.as_view(), name='example_list'),
    path('example/add/', views.ExampleCreateView.as_view(), name='example_add'),
    path('example/delete/', views.ExampleBulkDeleteView.as_view(), name='example_bulk_delete'),
    path('example/<int:pk>/edit/', views.ExampleEditView.as_view(), name='example_edit'),
    path('example/<int:pk>/delete/', views.ExampleDeleteView.as_view(), name='example_delete'),

    path('dcim/devices/extra/', views.DeviceExampleListView.as_view(), name='deviceexample_list'),
    path('dcim/devices/extra/add/', views.DeviceExampleCreateView.as_view(), name='deviceexample_add'),
    path('dcim/devices/extra/delete/', views.DeviceExampleBulkDeleteView.as_view(), name='deviceexample_bulk_delete'),
    path('dcim/devices/extra/<int:pk>/edit/', views.DeviceExampleEditView.as_view(), name='deviceexample_edit'),
    path('dcim/devices/extra/<int:pk>/delete/', views.DeviceExampleDeleteView.as_view(), name='deviceexample_delete'),
]
