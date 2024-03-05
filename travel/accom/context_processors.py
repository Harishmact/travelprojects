from accom.models import Bookroom


def roomdet(request):
        room=0

        if request.user.is_authenticated:
                u=request.user

                try:
                        room=Bookroom.objects.filter(user=u,room_status="booked")
                except:
                        room=0

        return {'room':room}


