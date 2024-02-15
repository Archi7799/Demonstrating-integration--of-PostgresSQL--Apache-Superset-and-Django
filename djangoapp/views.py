from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import render

@api_view(['GET'])
def getData(request):
    data = {"message": "Placeholder data from Superset"}
    return Response(data)

@api_view(['GET'])
def getDashboardCharts(request, id):
    payload = {
        "password": "admin",
        "provider": "db",
        "refresh": True,
        "username": "admin"
    }

    response = requests.post('http://superset_container:8088/api/v1/security/login', json=payload)

    if response.status_code != 200:
        return Response({"error": "Failed to log in to Superset"}, status=response.status_code)

    access_token = response.json().get('access_token')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    url = f'http://superset_container:8088/api/v1/dashboard/{id}/embedded'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dashboard_data = response.json()
        return render(request, 'dashboard.html', {'data': dashboard_data})
    else:
        return render(request, 'error.html', {'error_message': 'Failed to fetch dashboard charts'})
