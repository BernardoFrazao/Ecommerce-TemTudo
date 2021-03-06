from django.urls import path, re_path
from products.views import UserProductHistoryView

from .views import (
        OrderListView,
        OrderDetailView,
        )

app_name = "accounts"

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    re_path(r'^(?P<order_id>[0-9A-Za-z]+)/$', OrderDetailView.as_view(), name='detail'),
]