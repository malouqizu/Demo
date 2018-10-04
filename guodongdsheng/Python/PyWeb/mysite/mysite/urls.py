from django.conf.urls import include, url
from django.contrib import admin
from mysite import HomeView
from myApp import views
urlpatterns = [
    url(r'^HomeView/', 'mysite.HomeView.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myApp/views/', 'myApp.views.home'),
]

# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
