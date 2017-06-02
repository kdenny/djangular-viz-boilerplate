from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^results/$', views.GetResult.as_view()),
    url(r'^results/(?P<result_key>[0-9]+)/$', views.GetResult.as_view())
]