from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def home(request):
    return Response({"message":"API working"})


@api_view(['GET','POST'])
def students(request):

    # GET → data show
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    # POST → data add
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)