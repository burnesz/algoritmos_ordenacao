from django.shortcuts import render
from app.forms import FormArray

# Create your views here.
def home(request):
    if request.method == "GET":
        form = FormArray()
        context = {'form': form}
        return render(request, "index.html", context=context)