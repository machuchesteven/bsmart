from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def homepage(request):
    return HttpResponse("<h1>Bsmart Learning management system</h1>")


class DepartmentView(APIView):
    def get(self, request, id=None):
        if id is not None:
            return HttpResponse("The id was provided")
        return Response({"name": "bsmart learning management system"}, status=status.HTTP_200_OK)
