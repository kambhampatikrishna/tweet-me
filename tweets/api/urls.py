from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from .views import (
    RetweetAPIView,
    TweetListAPIView,
    TweetCreateAPIView,
    TweetLikeAPIView,TweetDetailAPIView,
    # TweetCreateView, TweetDetailedView, TweetListView,
    #                 TweetUpdateView,TweetDeleteView
                    )

urlpatterns = [
    # path('search/',RedirectView.as_view(url="/")),
    path('',TweetListAPIView.as_view(),name='list_view'),
    path('create/',TweetCreateAPIView.as_view(),name='create_view'),
    re_path(r'^(?P<pk>\d+)/$',TweetDetailAPIView.as_view(),name='detail_view'),
    re_path(r'^(?P<pk>\d+)/retweet/$',RetweetAPIView.as_view(),name='retweet'),
    re_path(r'^(?P<pk>\d+)/like/$',TweetLikeAPIView.as_view(),name='like-toogle'),
    # # path('<int:pk>/update/',TweetUpdateView.as_view(),name='update_view'),
    # re_path(r'^(?P<pk>\d+)/$',TweetDetailedView.as_view(),name='detail_view'),
    # re_path(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view(),name='update_view'),
    # re_path(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name='delete_view'),
    
]


