from django.urls import path
from apps import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('activity_search_result', views.activity_search_result, name='activity_search_result'),
    path('add_car',views.add_car, name='add_car'),
    path('add_cruise',views.add_cruise, name='add_cruise'),
    path('add_flight',views.add_flight, name='add_flight'),
    path('add_hotel',views.add_hotel, name='add_hotel'),
    path('add_new_post',views.add_new_post, name='add_new_post'),
    path('add_tour',views.add_tour, name='add_tour'),
    path('admin_airlines',views.admin_airlines, name='admin_airlines'),
    path('admin_countries',views.admin_countries, name='admin_countries'),
    path('admin_currency_list',views.admin_currency_list, name='admin_currency_list'),
    path('admin_dashboard_booking',views.admin_dashboard_booking, name='admin_dashboard_booking'),
    path('admin_dashboard_orders_details',views.admin_dashboard_orders_details, name='admin_dashboard_orders_details'),
    path('admin_dashboard_orders',views.admin_dashboard_orders, name='admin_dashboard_orders'),
    path('admin_dashboard_reviews',views.admin_dashboard_reviews, name='admin_dashboard_reviews'),
    path('admin_dashboard_settings',views.admin_dashboard_settings, name='admin_dashboard_settings'),
    path('admin_dashboard_subscribers',views.admin_dashboard_subscribers, name='admin_dashboard_subscribers'),
    path('admin_dashboard_travel_agents',views.admin_dashboard_travel_agents, name='admin_dashboard_travel_agents'),
    path('admin_dashboard_traveler_detail',views.admin_dashboard_traveler_detail, name='admin_dashboard_traveler_detail'),
    path('admin_dashboard_travellers',views.admin_dashboard_travellers, name='admin_dashboard_travellers'),
    path('admin_dashboard_visa',views.admin_dashboard_visa, name='admin_dashboard_visa'),
    path('admin_dashboard_wishlist',views.admin_dashboard_wishlist, name='admin_dashboard_wishlist'),
    path('admin_dashboard',views.admin_dashboard, name='admin_dashboard'),
    path('admin_invoice',views.admin_invoice, name='admin_invoice'),
    path('admin_payments',views.admin_payments, name='admin_payments'),
    path('blog_single',views.blog_single, name='blog_single'),
    path('career_details',views.career_details, name='career_details'),
    path('career',views.career, name='career'),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('coming_soon',views.coming_soon, name='coming_soon'),
    path('contact',views.contact, name='contact'),
    path('destinations',views.destinations, name='destinations'),
    path('faq',views.faq, name='faq'),
    path('flight_booking',views.flight_booking, name='flight_booking'),
    path('flight_grid',views.flight_grid, name='flight_grid'),
    path('flight_list',views.flight_list, name='flight_list'),
    path('flight_search_result',views.flight_search_result, name='flight_search_result'),
    path('flight_sidebar',views.flight_sidebar, name='flight_sidebar'),
    path('flight_single',views.flight_single, name='flight_single'),
    path('gallery',views.gallery, name='gallery'),
    path('hotel_booking',views.hotel_booking, name='hotel_booking'),
    path('hotel_grid',views.hotel_grid, name='hotel_grid'),
    path('hotel_list',views.hotel_list, name='hotel_list'),
    path('hotel_search_result',views.hotel_search_result, name='hotel_search_result'),
    path('hotel_sidebar',views.hotel_sidebar, name='hotel_sidebar'),
    path('hotel_single',views.hotel_single, name='hotel_single'),
    path('page_404',views.page_404, name='page_404'),
    path('payment_complete',views.payment_complete, name='payment_complete'),
    path('payment_received',views.payment_received, name='payment_received'),
    path('pricing',views.pricing, name='pricing'),
    path('recover',views.recover, name='recover'),
    path('services',views.services, name='services'),
    path('tour_booking',views.tour_booking, name='tour_booking'),
    path('tour_details',views.tour_details, name='tour_details'),
    path('tour_fullwidth',views.tour_fullwidth, name='tour_fullwidth'),
    path('tour_grid',views.tour_grid, name='tour_grid'),
    path('tour_left_sidebar',views.tour_left_sidebar, name='tour_left_sidebar'),
    path('tour_list',views.tour_list, name='tour_list'),
    path('tour_right_sidebar',views.tour_right_sidebar, name='tour_right_sidebar'),
    path('tour_search_result',views.tour_search_result, name='tour_search_result'),
    path('user_dashboard_booking',views.user_dashboard_booking, name='user_dashboard_booking'),
    path('user_dashboard_profile',views.user_dashboard_profile, name='user_dashboard_profile'),
    path('user_dashboard_reviews',views.user_dashboard_reviews, name='user_dashboard_reviews'),
    path('user_dashboard_settings',views.user_dashboard_settings, name='user_dashboard_settings'),
    path('user_dashboard_wishlist',views.user_dashboard_wishlist, name='user_dashboard_wishlist'),
    path('user_dashboard',views.user_dashboard, name='user_dashboard'),
    path('user_profile',views.user_profile, name='user_profile'),
    
    
]