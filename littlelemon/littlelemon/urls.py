from django.contrib import admin
from django.urls import path, include
from restaurant.views import BookingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingView)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('restaurant/', include('restaurant.urls')),
   path('restaurant/menu/',include('restaurant.urls')),
   path('restaurant/booking/', include(router.urls))
]
