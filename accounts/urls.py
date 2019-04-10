from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from .views import (
    UserDetailView,
    UserFollowView,
    
                    )

urlpatterns = [
   
  
   
    re_path(r'^(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(),name='detail_view'),
    re_path(r'^(?P<username>[\w.@+-]+)/follow/$',UserFollowView.as_view(),name='follow'),
    
]


