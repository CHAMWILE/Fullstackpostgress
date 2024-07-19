from django.urls import path,include
from API import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('department/',views.departmentApi),
    path('department/([0-9]+)$',views.departmentApi),

    path('employee/',views.employeeApi),
    path('employee/([0-9]+)$',views.employeeApi),

    path('employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)