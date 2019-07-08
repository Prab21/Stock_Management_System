from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import *

# Create your views here.
  
def index(request):
	return  render(request,'index.html')


def display_laptops(request):
	items = Laptop.objects.all()
	context={
		'items':items,
		'header': 'laptop',
	}

	return render(request,'index.html',context) #3 aurgument in render


def display_Desktops(request):
	items = Desktop.objects.all()
	context={
		'items':items,
		'header': 'Desktop',
	}

	return render(request,'index.html',context) #3 aurgument in render


def display_Mobiles(request):
	items = Mobiles.objects.all()
	context={
		'items':items,
		'header': 'Mobiles',
	}

	return render(request,'index.html',context) #3 aurgument in rend



# def add_device(request,cls):
# 	if request.method == "POST":
# 		form=cls(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return redirect("index")
  

# 	else:
# 		form=cls()
# 		return render(request,'add_new.html',{'form': form})



# def add_desktop(request,cls):
# 	return add_device(request,DesktopForms)

# def add_laptop(request,cls):
# 	return add_device(request,LaptopForms)


# def add_mobile(request,cls):
# 	return add_device(request,MobilesForms)





 















# This is the function wh
# tilise above  
def add_laptop(request):
	if request.method == "POST":
		form=LaptopForms(request.POST)

		if form.is_valid():
			form.save()
			return redirect("index")


	else:
		form=LaptopForms()
		return render(request,'add_new.html',{'form': form})


def add_desktop(request):
	if request.method == "POST":
		form=DesktopForms(request.POST)

		if form.is_valid():
			form.save()
			return redirect("index")


	else:
		form=DesktopForms()
		return render(request,'add_new.html',{'form': form})


def add_mobile(request):
	if request.method == "POST":
		form=MobileForms(request.POST)

		if form.is_valid():
			form.save()
			return redirect("index")


	else:
		form=MobileForms()
		return render(request,'add_new.html',{'form': form})






# def edit_Laptop(request,pk):
# 	item=get_object_or_404(Laptop,pk=pk)
# 	if request.method=="POST":
# 		form=LaptopForms(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')
# 	else:
# 		form=LaptopForms(instance=item)
# 		return render(request,'edit_item.html',{'form': form})


def edit_device(request,pk,model,cls):
	item=get_object_or_404(model,pk=pk)
	if request.method=="POST":
		form=cls(request.POST,instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=cls(instance=item)
		return render(request,'edit_item.html',{'form': form})



def edit_laptop(request,pk):
	return edit_device(request,pk,Laptop,LaptopForms)


def edit_desktop(request,pk):
	return edit_device(request,pk,Desktop,DesktopForms)



def edit_mobile(request,pk):
	return edit_device(request,pk,Mobiles,MobileForms)




def delete_laptop(request,pk):
	Laptop.objects.filter(id=pk).delete()
	item=Laptop.objects.all()
	context={
		'items': items,
	}
	return render(request,'index.html',context)

def delete_desktop(request,pk):
	Desktop.objects.filter(id=pk).delete()
	item=Desktop.objects.all()
	context={
		'items': items,
	}
	return render(request,'index.html',context)

def delete_mobile(request,pk):
	Mobiles.objects.filter(id=pk).delete()
	item=Mobiles.objects.all()
	context={
		'items': items,
	}
	return render(request,'index.html',context)





















# def delete_deskop(request,pk):
# 	Desktop.objects.filter(id=pk).delete()
# 	item=Desktop.objects.all()
# 	context={
# 		'item': items
# 	}
# 	return render(request,'index.html',context)


# def delete_mobile(request,pk):

# 	Mobiles.objects.filter(id=pk).delete()
# 	item=Mobiles.objects.all()
# 	context={
# 		'item': items
# 	}
# 	return render(request,'index.html',context)