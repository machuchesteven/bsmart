from django.shortcuts import render, HttpResponse, get_object_or_404

# Working with the API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# import the models
from .models import *


# Create your views here.


def homepage(request):
    return HttpResponse("<h1>Bsmart Learning management system</h1>")


class DepartmentView(APIView):
    def get(self, request, id=None):
        if id is not None:
            dept = get_object_or_404(Department, id=id)
            return HttpResponse(dept)
        else:
            departments = Department.objets.all()
            for deps in departments:
                print(deps)
            return Response({"name": "bsmart learning management system, we could have rendered the departments list"}, status=status.HTTP_200_OK)
