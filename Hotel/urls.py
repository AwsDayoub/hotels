from django.urls import path
from . import views

urlpatterns = [
    path('search_for_hotels/<str:word>', views.SearchForHotels.as_view()),
    path('show_hotels/', views.ShowHotels.as_view()),
    path('show_cities/', views.ShowCities.as_view()),
    path('show_hotel_details/<int:hotel_id>', views.ShowHotelDetails.as_view()),
    path('show_hotel_features/<int:hotel_id>', views.ShowHotelFeatures.as_view()),
    path('show_hotel_images/<int:hotel_id>', views.ShowHotelImages.as_view()),
    path('show_hotel_comments/<int:hotel_id>', views.ShowHotelComments.as_view()),
    path('show_hotel_stays/<int:hotel_id>', views.ShowHotelStays.as_view()),
]