from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import Url


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


class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(Url, shortcode=shortcode)
        return HttpResponseRedirect(obj.link)

    """ def post(self, request, *args, **kwargs):
        return HttpResponse()
    """


"""
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    # obj = Url.objects.get(shortcode=shortcode)

    obj = get_object_or_404(Url, shortcode=shortcode)

    # try:
    #     obj = Url.objects.get(shortcode=shortcode)
    # except:
    #     obj = Url.objects.all().first()

    # obj_link = None
    # qs = Url.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists()and qs.count == 1:
    #     obj = qs.first()
    #     obj_link = obj.link

    return HttpResponse('hello {sc}'.format(sc=obj_link))
"""