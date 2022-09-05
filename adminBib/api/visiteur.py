from rest_framework.decorators import api_view
from rest_framework.response import Response
from adminBib.models import Visiteur
from adminBib.serializers import VisiteurSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404







@api_view(['GET'])
def view(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        visiteurs = Visiteur.objects.filter(**request.query_params.dict())
    else:
        visiteurs = Visiteur.objects.all()
    # if there is something in visiteurs else raise error
    if visiteurs:
        serializer = VisiteurSerializer(visiteurs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add(request):
	visiteur = VisiteurSerializer(data=request.data)

	# validating for already existing data
	if Visiteur.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if visiteur.is_valid():
		visiteur.save()
		return Response(visiteur.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update(request, pk):

    visiteur_ = Visiteur.objects.get(pk=pk)
    data = VisiteurSerializer(instance=visiteur, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete(request, pk):
    visiteur = get_object_or_404(Visiteur, pk=pk)
    visiteur.delete()
    return Response(status=status.HTTP_202_ACCEPTED)




    """"
@api_view(['POST'])
def update_id(request):
    id = request.POST.get("id")
    visiteur = Visiteur.objects.get(pk=id)
    data = VisiteurSerializer(instance=visiteur, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
     
         def retrieve(self, request, pk):
        visiteur = self.get_object()
        serializer = self.get_serializer(visiteur)
        return Response(serializer.data)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    """