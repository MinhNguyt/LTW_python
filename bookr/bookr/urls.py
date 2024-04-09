"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.contrib import admin
# # from django.urls import include
# from django.urls import path
# import reviews.views
# urlpatterns = [
#     # Các ánh xạ URL khác của ứng dụng của bạn có thể ở đây
#      path('admin/', admin.site.urls),
#      # path('', include('reviews.urls')),
#      path('',reviews.views.index),
#      path('th21/',reviews.views.index3),
#      path('th22/',reviews.views.index1),
#      path('bt1/',reviews.views.index2),
#      path('book-search/', reviews.views.search),
# ]
#
#chuong2
# from django.contrib import admin
# from django.urls import include,path
# import reviews.views
# urlpatterns = [
#      path('admin/', admin.site.urls),
#      path('', include('reviews.urls')),
# ]
from django.contrib import admin, auth
from django.contrib import admin
import reviews.views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from bookr.views import profile
urlpatterns = [
 path("admin/", admin.site.urls),
 path("",reviews.views.index),
 path("publishers/<int:pk>/",reviews.views.publisher_edit, name="publisher_edit"),
 path("publishers/new/",reviews.views.publisher_edit, name="publisher_create"),
 path("", include("reviews.urls")),
 path("accounts/", include(("django.contrib.auth.urls", "auth"),namespace="accounts")),
 path("accounts/password_reset/done/",auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
 path("accounts/reset/done/",auth.views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
 path('accounts/profile/', profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

