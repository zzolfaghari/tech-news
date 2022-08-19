"""tech_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from account.controller.login_controller import Login
from account.controller.register_controller import Register, activate

urlpatterns = [path('account/', include('account.urls')),
               path('admin/', admin.site.urls),
               path("login/", Login.as_view(), name="login"),
               path('register/', Register.as_view(), name='register'),
               path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
               path('comment/', include('comment.urls')),
               # path("logout/", views.LogoutView.as_view(), name="logout"),
               # path("password_change/", PasswordChange.as_view(), name="password_change"),
               # path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
               path('', include('base.urls')),
               path('', include('django.contrib.auth.urls')),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               )
