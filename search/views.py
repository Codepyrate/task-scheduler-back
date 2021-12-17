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

        url = f"https://serpapi.com/search.json?q={q}&location=Austin%2C+Texas%2C+United+States&hl=en&gl=us&google_domain=google.com&api_key=1bd1bc394ab69a581ecbd7ba87230e8c1473514be84f0012ebc949df8d827b2b"

        response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())



   

    

    
    
