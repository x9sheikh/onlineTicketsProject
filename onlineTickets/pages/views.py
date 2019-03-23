from django.shortcuts import render
from django.http import HttpResponse
#from onlineTickets.tickets.models import Ticket
from tickets.models import Ticket

# Create your views here.
def homePageView(request,*args,**kwargs):
    context = {}
    return render(request,"index.html",context=context)

def sellTicketsView(request,*args,**kwargs):
    tickets =  Ticket.objects.all()
    context = {
        'tickets' : tickets,
    }

    return render(request,"sellTickets.html",context=context)

