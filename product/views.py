from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .serializers import CategoryListSealizer, CategoryDetailSerializer , ProductListSealizer, ProductDetailSerializer, ReviewDetailSerializer, ReviewListSealizer, ProductReviewSerializer
from .models import Category , Product, Review
# Create your views here.



@api_view(['GET','PUT','DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist:
        return Response(data = {'error': 'Category not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    if request.method == 'GET':    
        data = CategoryDetailSerializer(category).data
        return Response(data = data)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(category).data)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST'])
def category_list_create_api_view(request):
    category = Category.objects.annotate(products_count=Count('products'))
    data = CategoryListSealizer(category, many = True).data

    if request.method == 'GET':
        return Response(
                data = data,
                status = status.HTTP_200_OK
            )
    elif request.method == "POST":
        name = request.data.get("name")

        category = Category.objects.create(
            name = name
        )

    return Response(status=status.HTTP_201_CREATED,
                    data=CategoryDetailSerializer(category).data)


@api_view(['GET','POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        data = ProductListSealizer(product, many = True).data

        return Response(
                data = data,
                status = status.HTTP_200_OK
            )
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
    
    product = Product.objects.create(
        title = title,
        description = description,
        price = price,
        category_id = category_id,

        )

    return Response(status=status.HTTP_201_CREATED,
                    data=ProductDetailSerializer(product).data)


@api_view(['GET','PUT','DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        return Response(data = {'error': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    
    
    if request.method == 'GET':
        data = ProductDetailSerializer(product).data
        return Response(data = data)
    
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()

        data = ReviewListSealizer(review, many = True).data

        return Response(
                data = data,
                status = status.HTTP_200_OK
            )
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
    
    review  = Review.objects.create(
        text = text,
        product_id = product_id,
        stars = stars
        )
    return Response(status=status.HTTP_201_CREATED,
                    data=ReviewDetailSerializer(review).data)

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id = id)
    except Review.DoesNotExist:
        return Response(data = {'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    if request.method == 'GET':    
        data = ReviewDetailSerializer(review).data
        return Response(data = data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.product_id = request.data.get('product_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


@api_view(['GET'])
def review_of_product_api_view(request):
    
    products = Product.objects.all()

    data = ProductReviewSerializer(products, many = True).data

    return Response(
            data = data,
            status = status.HTTP_200_OK
        )