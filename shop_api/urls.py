from django.contrib import admin
from django.urls import path

from product.views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ReviewListCreateAPIView,
    ReviewDetailAPIView,
    ProductReviewAPIView,
)

from users.views import (
    RegistrationAPIView,
    AuthorizationAPIView,
    ConfirmationAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/categories/", CategoryListCreateAPIView.as_view()),
    path("api/v1/categories/<int:id>/", CategoryDetailAPIView.as_view()),
    path("api/v1/products/", ProductListCreateAPIView.as_view()),
    path("api/v1/products/<int:id>/", ProductDetailAPIView.as_view()),
    path("api/v1/products/reviews/", ProductReviewAPIView.as_view()),
    path("api/v1/reviews/", ReviewListCreateAPIView.as_view()),
    path("api/v1/reviews/<int:id>/", ReviewDetailAPIView.as_view()),
    path("api/v1/users/registration/", RegistrationAPIView.as_view()),
    path("api/v1/users/authorization/", AuthorizationAPIView.as_view()),
    path("api/v1/users/confirm/", ConfirmationAPIView.as_view()),
]
