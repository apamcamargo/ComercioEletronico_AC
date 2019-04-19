from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "login.html",
                  context={"form":form})
    if request.method == "GET":
        print("Acesso via GET")
    else:
        print("Acesso via POST")
    return rende(request, "login.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
