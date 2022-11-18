from django.urls import path
from .views import (UserProfileListCreateView, 
                    MessageCreateView, 
                    DeliveryCreateView, 
                    UserProfileListDestroyView, 
                    UserProfileListUpdateView, 
                    StatDeliveryView,
                    DeliveryDestroyAPIView,
                    DeliveryUpdateAPIView,)


urlpatterns = [
    path('v1/clients/', UserProfileListCreateView.as_view()),
    path('v1/client/destroy/<int:pk>', UserProfileListDestroyView.as_view()),
    path('v1/client/update/<int:pk>', UserProfileListUpdateView.as_view()),
    path('v1/message/', MessageCreateView.as_view()),
    path('v1/delivery/', DeliveryCreateView.as_view()),
    path('v1/delivery/Update/<int:pk>', DeliveryUpdateAPIView.as_view()),
    path('v1/delivery/destroy/<int:pk>', DeliveryDestroyAPIView.as_view()),
    path('v1/message/stat', StatDeliveryView.as_view()),
]