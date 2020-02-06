from rest_framework.routers import SimpleRouter
from apptwo.views import ProductOperations,VendorOperations
srouter = SimpleRouter()
srouter.register('product',ProductOperations)
srouter.register('vendor',VendorOperations)
urlpatterns = srouter.urls

