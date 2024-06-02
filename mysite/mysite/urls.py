from django.contrib import admin
from django.urls import path

from . import views
from blog import views as blogviews
from kontak import views as kontakviews

urlpatterns = [
    path('', views.index),
    path('blog/', blogviews.index),
    path('kontak/', kontakviews.index),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
