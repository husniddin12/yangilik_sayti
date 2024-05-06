from django.contrib import admin
from django.urls import path
from .views import yangiliklar_list_view, yangiliklar_detail_view, contact_view, about_us_view, texno_news_view, \
    mahalliy_news_view, sport_news_view, iqtisodiy_news_view, jamiyat_news_view

urlpatterns = [
    path('', yangiliklar_list_view, name='yangiliklar_list_link'),
    path('mahalliy/', mahalliy_news_view, name = 'mahalliy_news'),
    path('iqtisodiyot/', iqtisodiy_news_view, name = 'iqtisodiyot_news'),
    path('jamiyat/', jamiyat_news_view, name = 'jamiyat_news'),
    path('sport/', sport_news_view, name = 'sport_news'),
    path('texnologiya/', texno_news_view, name = 'texno_news'),
    path('contact-us', contact_view, name='contact_page'),
    path('about/', about_us_view, name='about_us_page'),
    path('<str:slug>/', yangiliklar_detail_view, name='deatil_link'),
]


