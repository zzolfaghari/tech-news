from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from base.enums import StatusType
from base.models import Article


class FieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                "author",
                "title",
                "slug",
                "description",
                "category",
                "thumbnail",
                "publish",
                "is_special",
                "status"

            ]
        elif request.user.is_author:
            self.fields = [
                "title",
                "slug",
                "description",
                "category",
                "thumbnail",
                "publish",
                "is_special"

            ]

        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = StatusType.DRAFT
        return super().form_valid(form)


class AuthorAccessMixin:
    # to check that every author must access to their draft articles (not others articles) except superuser
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user and article.status in [StatusType.DRAFT, StatusType.BACK] \
                or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)

        else:
            raise Http404("you do not allowed to see this page")


class SuperuserAccessMixin:
    # just superusers can delete articles
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you do not allowed to see this page")


class AuthorsAccessMixin:
    # just superusers can delete articles
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:profile")