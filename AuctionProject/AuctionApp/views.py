from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from AuctionApp.models import Trades
import logging

logger = logging.getLogger(__name__)


def index(request):
    context = {}
    auctions = Trades.objects.all()
    context['auction_list'] = auctions
    return render(request, 'AuctionApp/auction_view.html', context=context)

def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))

    logout(request)
   
    return redirect('AuctionApp:TradePage')


def login_request(request):
    context = {}
   
    if request.method == "POST":
       
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('AuctionApp:TradePage')
        else:
            return render(request, 'AuctionApp/user_login.html', context)
    else:
        return render(request, 'AuctionApp/user_login.html', context)
    


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'AuctionApp/user_registration.html', context)
    
    elif request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.debug("{} is new user".format(username))
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("AuctionApp:TradePage")
        else:
            return render(request, 'AuctionApp/user_registration.html', context)
        

def create_auction(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'AuctionApp/auction_creation.html', context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            sellitem = request.POST['sellitem']
            buyitem = request.POST['buyitem']
            Title = request.POST['title']
            contact = request.POST['contact']
            forSale = True
            user = request.user
            trade = Trades(ItemSell=sellitem,ItemBuy=buyitem,Title=Title,ForSale=forSale,user=user,ContactInfo=contact)
            trade.save()
            return redirect("AuctionApp:TradePage")
        
def remove_auction(request,auction_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            auction = get_object_or_404(Trades, id=auction_id)
            if str(auction.user) == str(request.user):
                print("Correct User!")
                auction.ForSale = False
                auction.save()
                return redirect("AuctionApp:TradePage")
                print(auction)
            else:
                print("incorect user")
                return redirect("AuctionApp:TradePage")
            
