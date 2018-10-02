from rest_framework import routers


from postit.views import PostitViewSet, ListItemViewSet

router = routers.SimpleRouter()
router.register(r'post', PostitViewSet)
router.register(r'listitem', ListItemViewSet)

urlpatterns = router.urls
