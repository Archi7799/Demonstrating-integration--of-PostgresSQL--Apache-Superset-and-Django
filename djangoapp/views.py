from rest_framework.response import Response
import requests
from django.shortcuts import render
from rest_framework.decorators import api_view

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
    print(access_token, "Response")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    # p = {
    #     "resources": [
    #         {
    #             "id": "915ea5b9-fa1c-4cd3-a3bf-9b0f50bb3437",
    #             "type": "dashboard"
    #         }
    #     ],
    #     "rls": [
    #         {
    #             "publisher = 'Nintendo'"
    #         }
    #     ],
    #     "user": {
    #         "first_name": "Archi",
    #         "last_name": "Gupta",
    #         "username": "archi_gupta"
    #    }
    # }

    # url='http://superset_container:8088/api/v1/security/guest_token/'
    # response = requests.post(url, json=p,headers={"Authorization": f"Bearer {access_token}"})
    # print("hagi")
    # guest_token = response.json()
    # print(response,"hehe")

    # url = f'http://superset_container:8088/api/v1/dashboard/{id}/charts'
    response = requests.get(url, headers=headers)
    print(response,"Hii")

    # if response.status_code == 200:
    #     dashboard_data = response.json()
    return render(request, 'dashboard.html')
    # else:
     #    return Response({'error_message': 'Failed to fetch dashboard charts'})
