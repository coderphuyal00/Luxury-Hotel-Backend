from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models import Booking
from Room.models import Room
# full_message = f"Question from {name} <{email}>:\n\n{question} for {department} deparment."
# send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

def book_room(request, id):
    room = get_object_or_404(Room, id=id)

    if room.status == "booked":
        return render(request, 'already_booked.html', {"room": room})

    if request.method == 'POST':
        name = request.POST.get('customer_name')
        phone = request.POST.get('phone_number')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        Booking.objects.create(
            room=room,
            customer_name=name,
            phone_number=phone,
            check_in=check_in,
            check_out=check_out
        )

        room.status = 'booked'
        room.save()

        return redirect('room_list')

    return render(request, 'book_room.html', {'room': room})
