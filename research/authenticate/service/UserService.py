"""
 TODO: 비즈니스 로직 삽입 위치 고민해보기
    1. DRF 에서 비즈니스 로직이 시리얼라이저에 위치한다면 뷰에는 어떤 것만 보여주면 될까?
    2. 비즈니스 로직이 시리얼라이저에 위치하는게 옳은 걸까?
    3. 비즈니스 로직이 시리얼라이저 말라고 다른 계층에 속하다면 어떤 방식으로 분류할 수 있을까?

"""
import datetime
from pytz import timezone
from typing import List, Optional

from rest_framework import serializers

from ..models import User


class UserService(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    # jwt를 직접 만들어서 사용하려면 아래와 같이
    # def validate(self):
    #
    #     credential = {
    #         'email': self.initial_data.get('email'),
    #         'password': self.initial_data.get('password')
    #     }
    #
    #     user = authenticate(**credential)
    #
    #     if user:
    #         return user
    #     else:
    #         return False

    @staticmethod
    def get_users() -> Optional[List]:
        users = User.objects.all().values('id', 'email', 'last_login')  # 불필요한 필드는 제거
        return list(users)

    @staticmethod
    def register(validated_data) -> bool:
        """ 유저 등록  """
        if validated_data:
            user = User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password']
            )
            if user:
                return True
            else:
                return False
