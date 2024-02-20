from django.urls import path
from doctor import views
urlpatterns=[
    path("",views.docter),
    path("doctorview/",views.docterview),
    path("up/<int:pk>/",views.updatedocter,name="up"),
    path("del/<int:pk>/",views.delete,name="del")
]