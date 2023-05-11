from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import VoiceSerrializers


# Create your views here.
class main(APIView):
    def get(self, request):
        return render(request, 'beta/MAIN.html')


class result(APIView):
    def get(self, request):
        return render(request, 'beta/ResultPage.html')


class inputPage(APIView):
    def get(self, request):
        return render(request, 'beta/inputPage.html')

    # audio input post
    def post(self, request):
        serializer = VoiceSerrializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            voice = serializer['file']
            '''
            딥러닝 input output 
            
            '''
            output = '윤하'
            context = dict(output=output)
            return render(request, template_name='beta/ResultPage.html', context=context)
