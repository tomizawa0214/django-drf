from django.views.generic import TemplateView


class IndexView(templateView):
    template_name = 'jobs/index.html'