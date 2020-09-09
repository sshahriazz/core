from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import my_resume, home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('my_resume/', my_resume, name='my_resume'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
