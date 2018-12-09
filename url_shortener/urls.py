from django.conf.urls import url
from django.contrib import admin
from urlsh.views import HomeView, UrlRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', UrlRedirectView.as_view(), name='scode')
]
