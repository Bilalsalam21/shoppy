from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products,Carts,Reviews
from api.serializers import ProductSerializers,ProductModelSerializer,UserSerializer,CartSerializer,ReviewSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication,permissions


class ProductViewsetView(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Products.objects.all()
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes =[permissions.IsAuthenticated]

    @action(methods=["GET"],detail=False)
    def categories(self,request,*args,**kwargs):
        res=Products.objects.values_list('category',flat=True).distinct()
        return Response(data=res)

    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Products.objects.get(id=id)
        user=request.user
        user.carts_set.create(product=item)
        return Response(data="item add to cart")

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get("pk")
        object=Products.objects.get(id=id)
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=object,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["GET"],detail=True)
    def reviews(self,request,*args,**kwargs):
        product=self.get_object()
        qs=product.reviews_set.all()
        serializer=ReviewSerializer(qs,many=True)
        return Response(data=serializer.data)

class CartsView(viewsets.ModelViewSet):
    serializer_class =CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    
class ProductView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializers(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializers(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Products.objects.filter(id=id).update(**request.data)
        qs=Products.objects.get(id=id)
        serializer=ProductSerializers(qs,many=False)
        return Response(data=serializer.data)

    def delete(self,*args,**kwargs):
        id=kwargs.get("id")
        Products.objects.filter(id=id).delete()
        return Response(data="object deleted")


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def create(self,request,*args,**kwargs):
    #     serializer=UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)


# class UserView(APIView):
#     authentication_classes =[authentication.BasicAuthentication]
#     permission_classes =[permissions.IsAuthenticated]
#
#
#     def Post(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         item=Products.objects.get(id=id)
#         user=request.user
#         user.carts_set.create(product=item)
#         return Resposne(data="item add to cart")


class ReviewDelteView(APIView):
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Reviews.objects.filter(id=id).delete()
        return Response(data="review deleted")