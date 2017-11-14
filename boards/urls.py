from django.conf.urls import url
from .views import home, board_topics, new_topic

urlpatterns = [
    url(r'^$', home, name ='home'),
    url(r'boards/(?P<pk>\d+)/$',board_topics, name = 'board_topics'),
    url(r'boards/(?P<pk>\d+)/new/$', new_topic, name = 'new_topic'),
]
