from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegisterSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario creado exitosamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
