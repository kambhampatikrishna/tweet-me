from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TweetModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Tweet
from django.http import Http404
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from .mixins import FormUserNeededMixin,UserOwnerMixin
# Create your views here.
class ReTweetView(View):
    def get(self,request,pk,*args,**kwargs):
        tweet=get_object_or_404(Tweet,pk=pk)
        if request.user.is_authenticated:
            new_tweet=Tweet.objects.retweet(request.user,tweet)
            return HttpResponseRedirect("/")
        
        return HttpResponseRedirect(tweet.get_absolut_url())


class TweetCreateView(FormUserNeededMixin,CreateView):
    model=Tweet
    template_name="tweets/create_view.html"
    form_class=TweetModelForm
    # success_url=reverse_lazy('tweet:detail_view') 


class TweetUpdateView(UserOwnerMixin,UpdateView):
    queryset=Tweet.objects.all()
    template_name='tweets/update_view.html'
    model=Tweet
    form_class=TweetModelForm
   # success_url='/tweet'
    def get_object(self):
        obj = Tweet.objects.filter(pk=self.kwargs['pk']).first()
        return obj
    
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    #queryset=Tweet.objects.all()
    model=Tweet
    template_name='tweets/delete_confirm.html'
    success_url=reverse_lazy("tweet:list_view")
    def get_object(self,queryset=None):
        pk_=self.kwargs.get("pk")
        obj = Tweet.objects.filter(user_id=pk_)[0]
        return obj
    # def get_context_data(self,*args,**kwargs):
    #     context=super(TweetDeleteView,self).get_context_data(*args,**kwargs)
    #     return context


class TweetDetailedView(DetailView):
    model=Tweet
    template_name="tweets/detailed_view.html"
    

   
class TweetListView(ListView):
    queryset =  Tweet.objects.all()
    model=Tweet
    def get_context_data(self,*args,**kwargs):
        context=super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form']=TweetModelForm()
        context['create_url']=reverse_lazy('tweet:create_view')
        return context
    def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(Q(content__icontains=query) |
                        Q(user__username__icontains=query)
            )
        return qs

# def tweet_detail_view(request,pk=None):
#     obj=get_object_or_404(Tweet,pk=pk)
#     context={
#         "object":obj
#     }
#     return render(request,"tweets/detailed_view.html",context)