from django.urls import path, include
from . import views
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

router.register(r'expenses', views.ExpenseViewSet)
router.register(r'categories', views.CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Expense Tracker API",
        default_version='v1',
        description="API for managing user expenses",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@expense.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]