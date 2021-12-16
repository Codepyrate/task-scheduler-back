import requests
from django.http import HttpResponse, HttpRequest


def get_query(req):
    #print(req.query_params)
    if req.method == 'GET':
        print(HttpRequest.path)
        return HttpResponse("get")
    
    q= req.query_params.get('query')

    url = f"https://serpapi.com/search.json?q={q}&location=Austin%2C+Texas%2C+United+States&hl=en&gl=us&google_domain=google.com&api_key=48cb4bc06fef6a9897d8bec1d2a4724e475c9bbe1b4cbf19e2c7555f3ca4ea25"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)
    
