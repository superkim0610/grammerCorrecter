from django.contrib import admin
from django.views.generic import RedirectView
# from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('meal', include('SchoolMeal.urls')),
    # path('grammer/', include('mainapp.urls')),
    # path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
