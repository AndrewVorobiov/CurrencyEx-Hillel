
from currency.views import (index, CreateContactUs, RateListView, RateDetailView, RateUpdateView, RateDeleteView, RateCreateView
                            )
from django.urls import path


app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name = 'rate-details'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contact-us/create/', CreateContactUs.as_view(), name='contact-us-create')
    ]