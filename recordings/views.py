from django.shortcuts import render,redirect
from .models import Recording ,Category ,Favorite
from .serializers import RecordingSerializer,FavoriteSerializer,CategorySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.


class RecordingCreateView(APIView):
    
      parser_classes = [MultiPartParser, FormParser]
      def get_permissions(self):
          if self.request.method == 'Get':
              return [AllowAny()]
          return [IsAuthenticated()]
      
      def get(self,request):
          
          recordings = Recording.objects.all()
          serializer = RecordingSerializer(recordings,many =True)
          return Response(serializer.data,status=status.HTTP_200_OK)
      
      def post(self,request):
          
          serializer = RecordingSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
      
class RecordingDetaitView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(Recording, pk=pk)



    def get(self, request, pk):
        recording = self.get_object(pk)
        serializer = RecordingSerializer(recording)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        recording = self.get_object(pk)
        if recording.user != request.user:
             return Response({'detail': 'You are not allowed to delete this recording'}, status=403)
        recording.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk): 
        recording = self.get_object(pk)
        if recording.user != request.user:
             return Response({'detail': 'You are not allowed to delete this recording'}, status=403)
        serializer = RecordingSerializer(recording, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
      
      

class CategoryCreateView(APIView):
    
      permission_classes = [AllowAny]
      
      def get(self,request):     
       categorys = Category.objects.all()
       serializer = CategorySerializer(categorys,many =True)
       return Response(serializer.data,status=status.HTTP_200_OK)
      
      
      def post(self,request):
          
          serializer = CategorySerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
   
    
      
class CategoryDetaitView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(Category, pk = pk)



    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
   
    def patch(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
      
      

class FavoriteCreateView(APIView):
    
      permission_classes = [IsAuthenticated]
      
      def get(self,request):
           
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
      def post(self,request):
          
          serializer = FavoriteSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save(user = request.user)
              return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
   
    
      
class FavoriteDetaitView(APIView):
    
    permission_classes = [IsAuthenticated]
    
 
    def delete(self, request, pk):
      
        favorite = get_object_or_404(Favorite,pk=pk , user=request.user )
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        print("Incoming data:", request.data)
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not username or not email or not password:
             return Response({'error': 'All fields are required.'}, status=400)

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        tokens = RefreshToken.for_user(user)
       
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token),
                'user_id': user.id 
            },
            status=201
        )