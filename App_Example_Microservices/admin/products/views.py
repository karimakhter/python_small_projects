from rest_framework import viewsets, status
from rest_framework.response import Response
from .producer import publish
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer

class ProductViewSet( viewsets.ViewSet ):
    def list( self, request ):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        data =serializer.data
        publish(data,b'All Products')
        return Response(data)

    def create( self, request ):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(serializer.data,b'Product Created')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve( self, request, pk=None ):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        data=serializer.data
        publish(data, b'Prodect reterived')
        return Response(data)

    def update( self, request, pk=None ):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(serializer.data, b'Product Updated')
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy( self, request, pk=None ):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        publish(serializer.data, b'Product Deleted')
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserViewSet(viewsets.ViewSet):

    def list( self, request ):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def create( self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def retrieve( self, request, pk=None ):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update( self, request, pk=None ):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy( self, request, pk=None ):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)