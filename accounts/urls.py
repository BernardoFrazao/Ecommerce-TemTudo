from django.urls import path, re_path
from products.views import UserProductHistoryView

from .views import (
        AccountHomeView,
        AccountEmailActivateView,
        )

app_name = "accounts"

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('history/products/', UserProductHistoryView.as_view(), name='user-product-history'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    re_path(r'^email/resend-activation$', AccountEmailActivateView.as_view(), name='resend-activation'),
]