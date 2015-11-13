from django.conf.urls import url
from viewbook import views

urlpatterns = [
    url(r'^listview/$', views.ViewListBook.as_view(), name="viewlistbook1"),
    url(r'^formview/$', views.FormViewBook.as_view(), name="formview"),
]