from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/' + ticker + '/quote?token=pk_7c1ceb529b3041e69fcfe82141081a99')

        try:
            api = json.loads(api_request.content)
        except Exception as er:
            api = 'Error...'

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    return render(request, 'add_stock.html', {})
