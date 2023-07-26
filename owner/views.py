from owner.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from owner.models import User
from rest_auth.views import LoginView

class UserRegistrationAPI(ModelViewSet):

    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(is_active=True)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "You are logged in !", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response


class CustomUserLogoutView(APIView):
    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):

        logout(request)
        response = Response({"detail": ("You are successfully logged out.")},
                            status=status.HTTP_200_OK)
        return response
