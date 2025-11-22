from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import default_storage
import json

from .models import Room
# Create your views here.


# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def room_list(request):

#     #get all room
#     if request.method == "POST":

#         room_number=request.POST.get("room_number")
#         type=request.POST.get("type")
#         status=request.POST.get("status")
#         price=request.POST.get("price")
#         description = request.POST.get("description")
#         image = request.FILES.get("image")

#         room = Room.objects.create(
#             room_number=room_number,
#             type=type,
#             status=status,
#             price=price,
#             description=description,
#             image=image
#         )

#     return JsonResponse({"message": "Room created", "id": room.id}, status=201)


# @csrf_exempt
# @require_http_methods(["GET", "PUT", "DELETE"])
# def room_detail(request, id):

#     try:
#         room = Room.objects.get(id=id)
#     except Room.DoesNotExist:
#         return JsonResponse({"error": "Room not found"}, status=404)

#     # GET one room
#     if request.method == "GET":
#         return JsonResponse({
#             "id": room.id,
#             "room_number": room.room_number,
#             "type": room.type,
#             "status": room.status,
#             "price": room.price,
#             "description": room.description,
#             "image": room.image.url if room.image else None
#         }, status=200)

#     # UPDATE
#     if request.method == "PUT":
#         body = json.loads(request.body)

#         room.room_number = body.get("room_number", room.room_number)
#         room.type = body.get("type", room.type)
#         room.status = body.get("status", room.status)
#         room.price = body.get("price", room.price)
#         room.description = body.get("description", room.description)

#         room.save()
#         return JsonResponse({"message": "Room updated"}, status=200)

#     # DELETE
#     if request.method == "DELETE":
#         room.delete()
#         return JsonResponse({"message": "Room deleted"}, status=200)

# just to show all the reoom if not to insert manually.
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})