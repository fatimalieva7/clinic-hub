
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinic_app.urls import router as clinic_router
from  users_app.urls import router as users_router
from doctors_app.urls import router as doctors_router


router = routers.DefaultRouter()
router.registry.extend(clinic_router.registry)
router.registry.extend(users_router.registry)
router.registry.extend(doctors_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include(router.urls)),
]
