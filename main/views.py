from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.http import Http404
from .models import Driver
from .serializers import DriverSerializer
from .models import Cab
from .serializers import CabSerializer
from .models import Cab_History
from .serializers import Cab_HistorySerializer
from .models import Travel_History
from .serializers import Travel_HistorySerializer
# Create your views here.



# STUDENT

class SViewOrAdd(APIView):

    def get(self, request):
        students=Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SModOrDelete(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet=self.get_object(pk)
        serializer=StudentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet=self.get_object(pk)
        serializer=StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# DRIVER

class DViewOrAdd(APIView):

    def get(self, request):
        drivers= Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DModOrDelete(APIView):
    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer=DriverSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet=self.get_object(pk)
        serializer = DriverSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        snippet= self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CAB



class CViewOrAdd(APIView):

    def get(self, request):
        cabs= Cab.objects.all()
        serializer = CabSerializer(cabs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CModOrDelete(APIView):
    def get_object(self, pk):
        try:
            return Cab.objects.get(pk=pk)
        except Cab.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer=CabSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet=self.get_object(pk)
        serializer = CabSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        snippet= self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# CAB_HISTORY

class CHViewOrAdd(APIView):

    def get(self, request):
        cab_histories= Cab_History.objects.all()
        serializer = Cab_HistorySerializer(cab_histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=Cab_HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CHDelete(APIView):
    def get_object(self, pk):
        try:
            return Cab_History.objects.get(pk=pk)
        except Cab_History.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer=Cab_HistorySerializer(snippet)
        return Response(serializer.data)


    def delete(self,request, pk):
        snippet= self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# TRAVEL_HISTORY

class THViewOrAdd(APIView):

    def get(self, request):
        travel_histories = Travel_History.objects.all()
        serializer = Travel_HistorySerializer(travel_histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Travel_HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class THDelete(APIView):
    def get_object(self, pk):
        try:
            return Travel_History.objects.get(pk=pk)
        except Travel_History.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = Travel_HistorySerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
