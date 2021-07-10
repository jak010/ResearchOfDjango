from django.conf.urls import url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    Member
)

urlpatterns = [

    # Member Register
    url(r"^register$", Member.Register.as_view()),
    # url(r"^users$", Member.MemberInfo.as_view()),  # GET: 유저 목록 조회

    url(r"^login$", TokenObtainPairView.as_view()),
    url(r"^refresh", TokenRefreshView.as_view()),

]
