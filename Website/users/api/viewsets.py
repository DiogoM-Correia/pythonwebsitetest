from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# class UserFilterViewSet(viewsets.ModelViewSet):

#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def get_queryset(self):
#         queryset = User.objects.all()
#         region = self.request.query_params.get('region')

#         if (region != ''):
#             queryset = queryset.filter(region = region)
#         return queryset


    

