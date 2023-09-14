from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(['GET'])
def about_company(request):
    company = Company.objects.last()
    ser = CompanySerializer(company).data
    return Response(ser)


@api_view(['POST'])
def application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.POST.get('image')
        reason = request.POST.get('reason')
        phone_num = request.POST.get('phone_num')
        telegram = request.POST.get('telegram')
        other_contact = request.POST.get('other_contact')
        applicant = Person.objects.create(name=name, image=image, reason=reason, phone_num=phone_num, telegram=telegram, other_contact=other_contact)
        ser = PersonSerializer(applicant)
        return Response({'status': 'created', 'data': ser.data})


@api_view(['GET'])
def about_AllApplicants(request):
    person = Person.objects.all()
    ser = PersonSerializer(person, many=True)
    return Response(ser.data)


@api_view(['GET'])
def about_person(request, pk):
    try:
        person = Person.objects.get(id=pk)
        ser = PersonSerializer(person).data
        return Response(ser)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Applicant does not exist'})
