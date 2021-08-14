
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class GenerateTokenSerializer(TokenObtainPairSerializer):
    """
    DRF 용 Service
    """

    @classmethod
    def get_token(cls, user):
        # JWT Claim 순서 바꾸기
        token = super().get_token(user)

        token['email'] = user.email
        return token

    def validate(self, attrs):
        # JWT 정렬하기
        token = super().validate(attrs)

        return {
            key: token[key]
            for key in sorted(token.keys())
        }
