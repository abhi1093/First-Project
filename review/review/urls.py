"""review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# http://127.0.0.1:8000/admin/
# http://127.0.0.1:8000/auth/mni/
# http://127.0.0.1:8000/auth/users/
# http://127.0.0.1:8000/auth/token/login

# superuser:- username-admin,password-mnblkj
# login user:- username-abhi@,password-123asdzxc
# auth_token :- '4a5e336a748f4811541421b3938b8387db85666a'