from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View


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
        return render(request, "urlsh/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "urlsh/home.html", {})


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