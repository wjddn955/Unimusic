from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InputSerrializers

# Create your views here.
class main(APIView):
    def get(self, request):
        return render(request, 'beta/MAIN.html')


class inputPage(APIView):
    def get(self, request):
        return render(request, 'beta/inputPage.html')

    def post(self,request):
        serializer = InputSerrializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            input = serializer['input']
            return Response({'output': '3'})