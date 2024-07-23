from django.shortcuts import render
from .models import NecModel
from .forms import NecForm

def home(request):
    if request.method == "POST":
        form = NecForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Record saved"
            form = NecForm() 
            return render(request, "home.html", {"msg": msg, "form": form})
        else:
            msg = "Check errors"
            return render(request, "home.html", {"msg": msg, "form": form})
    else:
        form = NecForm()
        return render(request, "home.html", {"form": form})
