from django.db.models import Q
from django.views.generic import ListView

from base.models import Article


class SearchList(ListView):
    paginate_by = 1
    template_name = 'base/search_list.html'

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.published().filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
