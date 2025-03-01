from django.shortcuts import render
from django.http import JsonResponse
import requests

def bitcoin_price(request):
    # Fetch Bitcoin price from CoinGecko API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
    except Exception as e:
        bitcoin_price = "Error fetching price"

    # If it's an AJAX request, return JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'bitcoin_price': bitcoin_price})

    # Otherwise, render the template
    context = {'bitcoin_price': bitcoin_price}
    return render(request, 'bitcoin/price.html', context)
