from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter

@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    count_list = list(Counter(data).elements())
    sorted_list = sorted(count_list, key=count_list.count, reverse=True)
    return Response({'solution': sorted_list})