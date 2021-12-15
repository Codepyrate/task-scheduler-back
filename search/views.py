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

        url = f"https://serpapi.com/search.json?q={q}&location=Austin%2C+Texas%2C+United+States&hl=en&gl=us&google_domain=google.com&api_key=693a1f379d5a97618cc229cd8da16365ae557c41cf1c6513fc3e2a762d7be61b"

        response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())



   

    

    
    
