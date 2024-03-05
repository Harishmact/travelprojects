
from django.db import models
from dest.models import location
from django.contrib.auth.models import User

class Accommodation(models.Model):
    type=models.CharField(max_length=200)
    dist=models.ForeignKey(location,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    loc=models.CharField(max_length=200)
    desc=models.TextField()
    image = models.ImageField(upload_to='tour/trips', blank=True, null=True)
    def __str__(self):
        return self.name

class Roomdetails(models.Model):
    name = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    total_rooms = models.IntegerField()
    d_rooms = models.IntegerField()
    p_rooms = models.IntegerField()
    d_rent = models.IntegerField()
    p_rent = models.IntegerField()
    dimage = models.ImageField(upload_to='rooms/deluxe', blank=True, null=True)
    pimage = models.ImageField(upload_to='room/premium', blank=True, null=True)
    available=models.BooleanField(default=True)


    def __str__(self):
        return self.name.name

class Bookroom(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    hotel_name = models.ForeignKey(Roomdetails, on_delete=models.CASCADE)

    room_status=models.CharField(default="notbooked",max_length=20)

    place=models.CharField(max_length=200)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=200)
    cin_date = models.DateField()
    cout_date = models.DateField()
    comfort=models.CharField(max_length=30)
    adults=models.IntegerField()
    children=models.IntegerField()
    noof_rooms=models.IntegerField()

    def __str__(self):
        return self.user.username


class Account(models.Model):
    acctnum=models.CharField(max_length=20)
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return self.acctnum












