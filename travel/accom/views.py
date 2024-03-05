from django.shortcuts import render,redirect,HttpResponse
from accom.models import Accommodation,Roomdetails,Bookroom,Account
from dest.models import location
from datetime import datetime
from django.contrib.auth.decorators import login_required



# Create your views here.
def accommodation(request,p):
    k=location.objects.get(dname=p)
    l=Accommodation.objects.filter(dist=k)
    return render(request,'stay.html',{'hotels':l,'loc':k})

def booking(request,p):
    n=Accommodation.objects.get(name=p)
    k=Roomdetails.objects.filter(name=n)
    return render(request,'booking.html',{'book':n,'room':k})

@login_required
def travellers(request,p):
    n=Accommodation.objects.get(name=p)
    k=Roomdetails.objects.get(name=n)

    if(request.method=="POST"):
        name=request.POST['na']
        pl= request.POST['pl']
        ph=request.POST['ph']
        e=request.POST['e']
        cin = request.POST['Cin']
        cot= request.POST['Cout']
        cmft = request.POST['Com']
        ad = request.POST['a']
        ch = request.POST['c']
        rmn = request.POST['r']
        acc_name = request.POST['aname']
        acc_type = request.POST['atype']
        acc_num = request.POST['anum']

        ac = Account.objects.get(acctnum=acc_num)
        u=request.user

        date1=datetime.strptime(cin,'%Y-%m-%d')
        date2=datetime.strptime(cot,'%Y-%m-%d')

        if date2>date1:
            day=(date2-date1).days
        else:
            day=(date1-date2).days

        toatl=0

        if cmft == "deluxe":
            if k.d_rooms >= int(rmn):
                tot = int(rmn) * int(k.d_rent)
                total = tot * int(day)
            else:
                return HttpResponse("No Rooms Available")

        else:
            if k.p_rooms >= int(rmn):
                tot = int(rmn) * int(k.p_rent)
                total = tot * int(day)
            else:
                return HttpResponse("No Rooms Available")


        if ac.amount >= total:
            ac.amount -= total
            ac.save()
            o = Bookroom.objects.create(user=u, place=pl, phone=ph, email=e, cin_date=cin, cout_date=cot,
                                        comfort=cmft,
                                        adults=ad, children=ch, noof_rooms=rmn, room_status="booked", hotel_name=k)
            o.save()

            if o.comfort == "deluxe":
                k.d_rooms -= int(o.noof_rooms)
                k.save()
            else:
                k.p_rooms -= int(o.noof_rooms)
                k.save()
            k.total_rooms =k.d_rooms+k.p_rooms
            k.save()
            msg = "Room booked Successfully"
        else:
            msg = "Insufficient Fund"
        return render(request, 'validate.html', {'det': k, 'tot': total, 'msg': msg,'day':day})

    return render(request,'form.html')

