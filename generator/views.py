from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "generator/home.html", {"password": "hjsjdvjdfvvdjkvnkd"})


def password(request):


    chars = list("abcdefghıijklmnoöprsştvyz")
    length = int(request.GET.get("length", 14))
    if request.GET.get("uppercase"):
        chars.extend(list("ABCDEFGHIJKLMNOPRSŞTVYZ"))
    if request.GET.get("special"):
        chars.extend("@&/))=//%+^%&/")
    if request.GET.get("numbers"):
        chars.extend("0123456789")
    the_password= ""
    for x in range(length):
        the_password +=  random.choice(chars)
    return render(request, "generator/password.html", {"password": the_password})
#
def about(request):
    return render(request, "generator/about.html")


