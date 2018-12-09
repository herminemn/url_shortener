from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import SubmitUrlForm
from .models import Url
from url_data.models import ClickUrl


""" def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(Url, shortcode=shortcode)
    return HttpResponseRedirect(obj.link)
"""


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        return render(request, "urlsh/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Want to Shorten URL?",
            "form": the_form
        }
        return render(request, "urlsh/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Want to Shorten URL?",
            "form": form
        }
        template = "urlsh/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("link")
            obj, created = Url.objects.get_or_create(link=new_url)
            context = {
                "object": obj,
                "created": created
            }
            if created:
                template = "urlsh/success.html"
            else:
                template = "urlsh/already_exists.html"
        return render(request, template, context)


class UrlRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = Url.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists:
            raise Http404
        obj = qs.first()
        # ClickUrl.objects.create_count(obj)
        return HttpResponseRedirect(obj.link)
