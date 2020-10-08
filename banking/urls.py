from django.contrib import admin
from django.urls import path, include
from accounts.views import (user_login, user_logout, hhome,
    success, home, account_details, register_view, deposit,withdrawl, transactions)
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account/', include('accounts.urls')),
    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('account_details/', account_details, name="account_details"),
    path('register_view/', register_view, name= "register_view"),
    path('deposit/', deposit, name= "deposit"),
    path('withdrawal/',withdrawl, name= 'withdrawl'),
    path('home', hhome, name='hhome'),
    path('transactions/', transactions, name='transactions'),
    # path('transact/', transact, name="transact"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
