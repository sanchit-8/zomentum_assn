from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from datetime import datetime, timedelta

from .models import ticket
from .serializers import ticketSerializer

# Create your views here.

@api_view(['GET'])
def Viewtimings(request,time):
    cnt=0
    for i in ticket.objects.filter(timing=time):
        cnt=cnt+1
    data={}
    if(cnt<20):
        data["ticket available"]=20-cnt
    else:
        data["status"]="no ticket available for this timing"
    return Response(data=data)

@api_view(['GET'])
def viewtickets(request):
    try :
        tickets = ticket.objects.all()
    except : 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ticketSerializer(tickets,many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def ViewTicketById(request,ID):
    try :
        tickets = ticket.objects.get(id=ID)
    except : 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET" :
        serializer = ticketSerializer(tickets,many=False)
        return Response(serializer.data) 

@api_view(['GET'])
def ViewByTime(request,timings):
    try :
        tickets = ticket.objects.filter(timing = timings)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET" :
        serializer = ticketSerializer(tickets,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def BookTicket(request):
    serializer = ticketSerializer(data = request.data,partial=True)
    cnt=0
    if serializer.is_valid():
        print(serializer.validated_data)
        for i in ticket.objects.filter(timing=serializer.validated_data['timing']):
            cnt=cnt+1
    if(cnt<20):
        serializer.save()
        return Response(serializer.data)
    else:
        data={"status":"ticket not avaliable"}
        return Response(data=data)


@api_view(['PUT'])
def UpdateTimings(request,ID):
    try :
        tickets = ticket.objects.get(id=ID)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ticketSerializer(instance=tickets,data=request.data,partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["sussess"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteTicket(request,ID):
    try :
        tickets = ticket.objects.get(id=ID)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = tickets.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed" 
    return Response(data=data)

@api_view(['PUT'])
def ExpireTickets(request):
    # change status of all the tickets before 8hr than current time
    now = datetime.now()-timedelta(hours=8)
    tickets = ticket.objects.filter(timing__lt=now)
    print(tickets)

    for i in tickets:
        serializer = ticketSerializer(instance=i,data={'is_expired':True},partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            
    data["sussess"] = "update successful"
    return Response(data=data)
    

@api_view(['DELETE'])
def DeleteExpired(request):
    # delete all the tickets with status expired
    tickets = ticket.objects.filter(is_expired=True)
    for i in tickets:
        i.delete()

    return Response({"status":"deletion successful"})