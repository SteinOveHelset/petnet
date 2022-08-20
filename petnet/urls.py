from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, about

urlpatterns = [
    path('', include('store.urls')),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
