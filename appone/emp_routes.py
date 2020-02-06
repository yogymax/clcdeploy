from rest_framework.routers import SimpleRouter
from appone.views import EmpOperations,AddressOperations
srouter = SimpleRouter()
srouter.register('employee',EmpOperations)
srouter.register('address',AddressOperations)
urlpatterns = srouter.urls

