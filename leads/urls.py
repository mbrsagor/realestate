from rest_framework.routers import DefaultRouter

from leads.views.lead_views import LeadViewSet

router = DefaultRouter()
router.register('leads', LeadViewSet)

urlpatterns = router.urls
