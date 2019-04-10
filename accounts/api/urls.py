from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from tweets.api.views import (
    TweetListAPIView,
    # TweetCreateView, TweetDetailedView, TweetListView,
    #                 TweetUpdateView,TweetDeleteView
                    )

urlpatterns = [
    # path('search/',RedirectView.as_view(url="/")),
    re_path(r'^(?P<username>[\w.@+-]+)/tweet/',TweetListAPIView.as_view(),name='list_view'),
  
    
]


