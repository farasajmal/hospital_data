from django.urls import path
from patiend import views
urlpatterns=[
    path("",views.paitend),
    path("viewpatiend/",views.paitendview,name="viewpt"),
    path("update/<int:pk>/",views.updatepatient,name="update"),
    path("delete/<int:pk>/",views.delete,name="delete")

]