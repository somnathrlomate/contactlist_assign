from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from contact.models import Contact, Group
from contact.serializers import ContactSerializer, GroupSerializer


@csrf_exempt
def contact_list(request):
    if request.method == 'GET':
        cont = Contact.objects.all()
        cont_serializer = ContactSerializer(cont, many=True)
        return JsonResponse(cont_serializer.data, safe=False)

    elif request.method == 'POST':
        cont_data = JSONParser().parse(request)
        cont_serializer = ContactSerializer(data=cont_data)

        if cont_serializer.is_valid():
            cont_serializer.save()
            return JsonResponse(cont_serializer.data,
                                status=201)
        return JsonResponse(cont_serializer.errors,
                            status=400)


@csrf_exempt
def contact_detail(request, pk):
    try:
        cont = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        cont_serializer = ContactSerializer(cont)
        return JsonResponse(cont_serializer.data)
    elif request.method == 'DELETE':
        cont.delete()
        return HttpResponse(status=204)


@csrf_exempt
def group_list(request):
    if request.method == 'GET':
        group = Group.objects.all()
        group_serializer = GroupSerializer(group, many=True)
        return JsonResponse(group_serializer.data, safe=False)
    elif request.method == 'POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse(group_serializer.data,
                                status=201)
        return JsonResponse(group_serializer.errors,
                            status=400)


@csrf_exempt
def group_detail(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except group.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        group_serializer = GroupSerializer(group)
        return JsonResponse(group_serializer.data)

    elif request.method == 'DELETE':
        group.delete()
        return HttpResponse(status=204)
