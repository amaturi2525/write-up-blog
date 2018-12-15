from django.views.generic import TemplateView
from problems.models import Problem


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CTFs'] = Problem.objects.all().values('ctf').order_by('ctf').distinct()
        context['Categories'] = Problem.objects.all().values('category').order_by('category').distinct()
        return context
