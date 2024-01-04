from django.shortcuts import render

# Create your views here.
# Here I am using django because we want to get how many requests are coming

# I am going to use here Asynchronous processing to handle multiple requests
# concurrently to get the requests without blocking
from django.http import JsonResponse
import requests


def evaluate_expression(expression):
    api_url = "YOUR_API_ENDPOINT"  # Replace with the actual Web API endpoint

    # Make a request to the Web API
    response = requests.post(api_url, json={"expression": expression})

    # Parse the result from the API response
    result = response.json().get('result',
                                 'Error: Unable to fetch result from the API')

    return {"expression": expression, "result": result}


def evaluate_expressions(request):
    if request.method == 'POST':
        expressions = request.POST.getlist('expressions[]', [])
        results = [evaluate_expression(expression) for expression in
                   expressions]
        return JsonResponse({"results": results})

    return JsonResponse({"error": "Invalid request method"})
