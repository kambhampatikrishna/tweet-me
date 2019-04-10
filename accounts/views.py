from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.views import View
from .models import UserProfile
# Create your views here.


User=get_user_model()
class UserDetailView(DetailView):
    queryset=User.objects.all()
    template_name="accounts/user_detail.html"
    def get_object(self):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))
    def get_context_data(self,*args,**kwargs):
        context=super(UserDetailView,self).get_context_data(*args,**kwargs)
        context['following']=UserProfile.objects.is_following(self.request.user,self.get_object())
        return context

class UserFollowView(View):
    def get(self,request,username,*args,**kwargs):
        toogle_user=get_object_or_404(User,username__iexact=username)
        if request.user.is_authenticated:
            is_following=UserProfile.objects.toogle_follow(request.user,toogle_user)
        return redirect("profile:detail_view",username=username)