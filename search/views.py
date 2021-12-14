import requests
from django.http import HttpResponse, HttpRequest


def get_query(req):
    #print(req.query_params)
    if req.method == 'GET':
        print(HttpRequest.path)
        return HttpResponse("get")
    
    # q= req.query_params.get('query')

    # url = f"https://serpapi.com/search.json?q={q}&location=Austin%2C+Texas%2C+United+States&hl=en&gl=us&google_domain=google.com&api_key=693a1f379d5a97618cc229cd8da16365ae557c41cf1c6513fc3e2a762d7be61b"

    # payload={}
    # headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)

    #return(response.text)
    
