from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import pickle
from django.contrib import messages

# Create your views here.

guserlname = ""
pickle.dump(
    guserlname,
    open(
        "C:/Users/CHIRON/Desktop/mpcode/major-project/major_project/Climate_change/main_app/templates/variableStoringFile.dat",
        "wb",
    ),
)

def homepage(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        useremail = request.POST.get("uemail")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            user = User.objects.create_user(
                username=username, email=useremail, password=password1
            )
            return render(
                request,
                "login.html",
            )
            # user2 = new_user(name=username)
            # user2.save()
            # new_user.save()
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        userlname = request.POST["lemail"]
        lpassword = request.POST["lpassword"]
        print(userlname, lpassword)
        user = authenticate(username=userlname, password=lpassword)
        guserlname = userlname
        pickle.dump(
            guserlname,
            open(
                "C:/Users/CHIRON/Desktop/mpcode/major-project/major_project/Climate_change/main_app/templates/variableStoringFile.dat",
                "wb",
            ),
        )
        if user is not None:
            print("user is present")
            return render(request, "dashboard.html", {"name": userlname})
        else:
            print("user not present")
    return render(request, "login.html")

def dashboard(request):
    if request.method == "POST":
        data = request.POST["data"]
        guserlname = pickle.load(
            open(
                "C:/Users/CHIRON/Desktop/Mini Project/code/miniproject1/accounts/variableStoringFile.dat",
                "rb",
            )
        )
        print(guserlname)
        if data == "bookapi" or data == "history":
            messages.info(request, data)

        return render(request, "dashboard.html", {"name": guserlname})


def bookapi(request):
    import requests

# Set up API key and search engine ID
    api_key = 'AIzaSyDRXVYng56GJNHm-YtIdsPqmVIftfiJcmk'
    search_engine_id = 'c13c46cfbee6641cf'

# Construct API request
    query = 'impact of climate change book'
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'

    # Send API request
    response = requests.get(url)

    # Parse JSON response
    json_data = response.json()
    books = []
    for item in json_data['items']:
        book = {
            'title': item['title'],
            'snippet': item['snippet'],
            'link': item['link'],
            'image_url': None  # Initialize image URL to None
        }
        if 'pagemap' in item and 'thumbnail' in item['pagemap']:
            # Extract image URL if available
            book['image_url'] = item['pagemap']['thumbnail'][0]['src']
        books.append(book)

    context = {
        'books': books
    }

    return render(request, 'bookapi.html', context)

def logout(request):
    
    return render(request,"index.html")