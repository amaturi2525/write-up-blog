#pip install pygments,py-gfm
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Problem
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension


# Create your views here.
class Index(TemplateView):
    template_name = 'problems/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problems'] = Problem.objects.filter(ctf=kwargs['ctf'])
        context['CTF_name'] = kwargs['ctf']
        context['CTFs'] = Problem.objects.all().values('ctf').order_by('ctf').distinct()
        context['Categories'] = Problem.objects.all().values('category').order_by('category').distinct()
        return context


class CIndex(TemplateView):
    template_name = 'problems/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problems'] = Problem.objects.filter(category=kwargs['cate'])
        context['CTF_name'] = kwargs['cate']
        context['CTFs'] = Problem.objects.all().values('ctf').order_by('ctf').distinct()
        context['Categories'] = Problem.objects.all().values('category').order_by('category').distinct()
        return context

class Detail(TemplateView):
    template_name = 'problems/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problem'] = Problem.objects.filter(pk=kwargs['problem_id'])
        context['CTFs'] = Problem.objects.all().values('ctf').order_by('ctf').distinct()
        context['Categories'] = Problem.objects.all().values('category').order_by('category').distinct()
        sample_makedown = Problem.objects.get(pk=kwargs['problem_id']).body
        md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
        context['text'] = md.convert(sample_makedown)
        return context
