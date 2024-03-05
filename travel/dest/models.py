from django.db import models

# Create your models here.
class location(models.Model):
    dname=models.CharField(max_length=200)
    img= models.ImageField(upload_to='dest/dists', blank=True,null=True)

    def __str__(self):
        return self.dname


class place(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='dest/places', blank=True, null=True)
    locate=models.ForeignKey(location,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Hotels(models.Model):
    place=models.CharField(max_length=100)
    image=models.ImageField(upload_to='dest/hotels',blank=True,null=True)
    img=models.ImageField(upload_to='dest/hotl',blank=True,null=True)


    def __str__(self):
        return self.place