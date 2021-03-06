"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # new
from django.conf import settings  # new
from django.conf.urls.static import static  # new
urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # User Mgmt
    # These urls include login, logout, password_change, etc
    # default: path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),  # new for allauth
    # Allauth also obviates the need for the users/urls.py and users/views.py.  (We could delete)

    # Local Apps
    path('', include('pages.urls')),  # new
    path('accounts/', include('users.urls')),  # new
    path('books/', include('books.urls')),  # new
    path('orders/', include('orders.urls')),  # new

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new
#print("URL PATTERNS: ")
# print(urlpatterns)
