from django.urls import path,include
from .views import viewtickets,ViewTicketById,BookTicket,UpdateTimings,DeleteTicket,ViewByTime,Viewtimings,ExpireTickets,DeleteExpired

urlpatterns = [
    path('viewtiming/<str:time>',Viewtimings),
    path('view/',viewtickets),
    path('viewbyid/<str:ID>',ViewTicketById),
    path('bookticket/',BookTicket),
    path('updateticket/<str:ID>',UpdateTimings),
    path('deleteticket/<str:ID>',DeleteTicket),
    path('viewbytime/<str:timings>',ViewByTime),
    path('expire/',ExpireTickets),
    path('deleteexpired/',DeleteExpired)
]