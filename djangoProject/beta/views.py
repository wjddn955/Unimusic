from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import VoiceSerrializers
from .models import Singer
from .models import Audio


# Create your views here.
class main(APIView):
    def get(self, request):
        return render(request, 'beta/MAIN.html')


"""
class result(APIView):
    def get(self, request):
        result_idx = request.GET.get('result_idx')
        return render(request, 'beta/ResultPage.html')
"""


class inputPage(APIView):
    def get(self, request):
        return render(request, 'beta/inputPage.html')

    # audio input post
    def post(self, request, format=None):

        audio_file = request.FILES['audio_file']
        print(audio_file)
        #Audio.objects.create(file=audio_file)

        '''
        딥러닝 input output 
            
        '''
        output = 0
        singer_list = ['윤하', '이수현', '아이유', '자우림', '태연', '헤이즈', '윤미래', '백예린', '비비', '슬기', '나연', '거미', '10cm',
                           '엠씨더맥스', '성시경', '장범준', '신용재', '케이윌', '민경훈', '박효신', '나얼', '정승환']
        singer_name = singer_list[output]
        singer_rec = Singer.objects.filter(name=singer_name)

        context = {'singer': singer_rec}
        return render(request, template_name='beta/ResultPage.html', context=context)
