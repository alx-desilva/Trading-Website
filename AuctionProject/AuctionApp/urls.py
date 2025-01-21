from django.urls import path
from . import views

app_name = 'AuctionApp'

urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='TradePage'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('registration/', views.registration_request, name='registration'),
    path('createauction/', views.create_auction, name='createauction'),
    path('removeauction/<int:auction_id>/', views.remove_auction, name='removeauction'),
]