from django.conf.urls import url, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    Member,
    NewsFeed
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'feedview', NewsFeed.FeedViewSet, basename='Feed')

urlpatterns = [

    # DRF
    ## Register
    url(r"^login$", Member.MemberLoginView.as_view()),  # POST: 토큰 발급하기
    url(r"^refresh", TokenRefreshView.as_view()),
    url(r"^register$", Member.Register.as_view()),  # POST: 유저 등록하기

    # Custom
    # url(r"^login2$", Member.PublishToken.as_view()),  # POST: 토큰 발급하기

    # API Practice
    url(r"^users$", Member.Member.as_view()),  # GET: 유저 목록 조회

]

urlpatterns += router.urls
