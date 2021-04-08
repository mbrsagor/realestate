from rest_framework.routers import DefaultRouter

from leads.views.book_views import BookViewSet
from leads.views.lead_views import LeadViewSet

router = DefaultRouter()
router.register('leads', LeadViewSet)
router.register('books', BookViewSet)

urlpatterns = router.urls
