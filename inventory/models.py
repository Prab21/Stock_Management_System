from django.db import models


#creating a common table for all the devices like laptop,desktop, mobiles
class Device(models.Model):
	Type=models.CharField(max_length=100, blank=False)
	price=models.IntegerField()
	choices=(
		('Available','Item ready to be Purchace'),
		('Sold','Sold'),
		('Restore','Item restore in few days'),
		)
	status=models.CharField(max_length=10, choices =choices,default="Sold")
	issues=models.CharField(max_length=100,default="No Issues")

#This is going to avoid make migrations an extra model for the class devices
	class Meta:
		abstract=True

	#creating a common funtion for device class which represent device object
	def __str__(self):
		return 'Type :{0} Price:{1}'.format(self.Type,self.price)




#all other class like laptop,desktop,mobile can inharit the common attributes of device class
class Laptop(Device):
	pass

class Desktop(Device):
	pass

class Mobiles(Device):
	pass
