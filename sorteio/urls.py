from baton.autodiscover import admin
from django.urls import path, include
from card.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', home, name="home"),

]
