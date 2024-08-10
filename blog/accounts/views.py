from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                        'data': serializer.errors,
                        'message': "something went wrong"
                    }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': "User created successfully"
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error: ", e)
            return Response({
                        'data': {},
                        'message': "something went wrong"
                    }, status= status.HTTP_400_BAD_REQUEST)

class loginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                 return Response({
                        'data': serializer.errors,
                        'message': "something went wrong"
                    }, status= status.HTTP_400_BAD_REQUEST)
            response = serializer.get_token(serializer.data)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print("LoginView Error: ", e)
            return Response({
                'data': {},
                'message': "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)