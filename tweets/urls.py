from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from .views import (TweetCreateView, TweetDetailedView, TweetListView,
                    TweetUpdateView,TweetDeleteView,ReTweetView)

urlpatterns = [
    path('search/',RedirectView.as_view(url="/")),
    path('',TweetListView.as_view(),name='list_view'),
    path('create/',TweetCreateView.as_view(),name='create_view'),
    # path('<int:pk>/update/',TweetUpdateView.as_view(),name='update_view'),
    re_path(r'^(?P<pk>\d+)/$',TweetDetailedView.as_view(),name='detail_view'),
    re_path(r'^(?P<pk>\d+)/retweet/$',ReTweetView.as_view(),name='retweet_view'),
    re_path(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view(),name='update_view'),
    re_path(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name='delete_view'),
    
]


