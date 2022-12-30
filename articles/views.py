from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import  Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
class ArticleListView(ListView):
    model = Article 
    template_name = 'article_list.html'
    
class ArticleDetailView(DeleteView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title','body','summary','photo')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleCreateView(LoginRequiredMixin,CreateView):# UserPassesTestMixin,
    model = Article
    template_name = 'article_create.html'
    fields = ('title','body','summary','photo',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # super yuzerning faqat ozi post qosha oladi
    # def test_func(self):
    #     return self .request.user.is_superuser