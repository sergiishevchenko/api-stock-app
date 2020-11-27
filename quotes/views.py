from django.shortcuts import render

def home(request):
    import requests
    import json

    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_7c1ceb529b3041e69fcfe82141081a99')

    try:
        api = json.loads(api_request.content)
    except Exception as er:
        api = 'Error...'

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
