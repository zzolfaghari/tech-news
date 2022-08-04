from django.views.generic import ListView

from base.logic.authors.authors_logic import AuthorLogic


class AuthorController(ListView):
    paginate_by = 1
    template_name = 'base/author_list.html'

    def __init__(self):
        super().__init__()
        self.author_logic = AuthorLogic()

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = self.author_logic.get_author_by_username(username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context



