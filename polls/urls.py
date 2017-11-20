from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^(?P<question_id>[0-9]+)/$', views.choices, name='choices'),
]
