from django.shortcuts import render
import json # The info form API will come in the format of JSON
import urllib.request
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        # print(city)
        if request.POST["city"] == "":
            data = {}
            # print(data) 
        else:
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=2e2f5e4a3899a1bfe595cde0b7c6106b').read()
            json_data = json.loads(res)
            data = {
                "city": city,
                "country": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
                "temperature" : str(json_data['main']['temp']) + "K",
                "pressure" : str(json_data['main']['pressure']) + "hPa",
                "humidity": str(json_data['main']['humidity']) + "%",
            }

            # print(data)   
    else:
        data = {}
        
    return render(request,"index.html",data)