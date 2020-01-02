from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

admin.site.site_header = 'OVO Analytics Admin'
admin.site.site_title = 'OVO Analytics'
# admin.site.site_url = 'https://ovoanalyics.com/'
admin.site.index_title = 'OVO Analytics Administrator'
admin.empty_value_display = '**Empty**'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/post/', include('post.api.urls', namespace='post')),
                  path('api/comment/', include('comment.api.urls', namespace='comment')),
                  path('api/favourite/', include('favourite.api.urls', namespace='favourite')),
                  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
