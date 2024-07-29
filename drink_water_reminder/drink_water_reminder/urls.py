from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from water_tracker import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'water-intakes', views.WaterIntakeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('water_tracker.urls')),  # Inclua as URLs do app water_tracker
]
