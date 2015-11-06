from django.conf.urls import url
from viewbook import views

urlpatterns = [
    # url(r'^(?P<pk>\d+)', views.ViewListBook.as_view(), name="viewlistbook"),
    url(r'^', views.ViewListBook.as_view(), name="viewlistbook1")
]