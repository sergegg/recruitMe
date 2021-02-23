import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.recruitMe import RecruitMe
from ..serializers import RecruitMeSerializer, UserSerializer

class RecruitMes(generics.ListCreateAPIView):
  premission_classes=(IsAuthenticated,)
  serializer_class = RecruitMeSerializer
  def get(self, requst):
    recruitMes = RecruitMe.objects.all()
    """index request to get all recruitMe profiles"""
    # recruitMes = RecruitMe.objects.filter(owner=request.user.id)
    data = RecruitMeSerializer(recruitMes, many=True).data
    return Response({ 'recruitMes': data })

  def post(self, request):
    """create recruitMe"""
    data = json.loads(request.body)
    # print(f'data is ${data}')
    data['recruitMe']['owner'] = request.user.id
    # request.data['recruitMe']['owner'] = request.user.id
    recruitMe = RecruitMeSerializer(data=data['recruitMe'])
    if recruitMe.is_valid():
      recruitMe.save()
      return Response({ 'recruitMe': recruitMe.data}, status=status.HTTP_201_CREATED)
    return Response(recruitMe.errors, status=status.HTTP_400_BAD_REQUEST)

class RecruitMeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        recruitMe = get_object_or_404(recruitMe, pk=pk)
        if not request.user.id == recruitMe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recruitMe')

        data = RecruitMeSerializer(recruitMe).data
        return Response({ 'recruitMe': data })

    def delete(self, request, pk):
        """Delete request"""
        recruitMe = get_object_or_404(RecruitMe, pk=pk)
        if not request.user.id == recruitMe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recruitMe')
        recruitMe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['recruitMe'].get('owner', False):
            del request.data['recruitMe']['owner']

        recruitMe = get_object_or_404(RecruitMe, pk=pk)
        if not request.user.id == recruitMe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recruitMe')

        request.data['recruitMe']['owner'] = request.user.id
        # Validate updates with serializer
        data = RecruitMeSerializer(recruitMe, data=request.data['recruitMe'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
