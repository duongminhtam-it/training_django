from django.conf.urls import url
from viewbook import views

urlpatterns = [
    url(r'^', views.ViewListBook.as_view(), name="viewlistbook1")
]