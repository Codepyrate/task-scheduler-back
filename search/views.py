import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET' , 'POST'])
def get_query(req):
   
    
    if req.method == 'GET':
        payload={}
        headers = {}
        q = req.query_params.get('q')
        print(q)

        url = f"https://serpapi.com/search.json?q={q}&location=Austin%2C+Texas%2C+United+States&hl=en&gl=us&google_domain=google.com&api_key=48cb4bc06fef6a9897d8bec1d2a4724e475c9bbe1b4cbf19e2c7555f3ca4ea25"

        response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())