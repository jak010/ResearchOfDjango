from ..models import Feed
from rest_framework import serializers


class FeedService(object):

    def __init__(self, model):
        self.model = model

    def read(self, query_param):

        # Parameter
        sort = query_param.get('sort')

        # query result set
        query_result = self.model.objects.all()

        if sort is not None:
            query_result = query_result.order_by(sort)

        data = [
            # Example. 데이터를 뽑아서 보여주기
            {
                'id': query.id,
                'user_id': query.user_id,
                'title': query.title,
                'content': query.content,
                'create_at': query.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': query.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for query in query_result
        ]
        return data

    def retrieve(self, path):
        user_pk = int(path.get('pk'))
        query_result = self.model.objects.filter(user_id=user_pk)

        data = [
            {
                'id': query.id,
                'user_pk': query.user_id,
                'title': query.title,
                'content': query.content,
                'create_at': query.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': query.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for query in query_result
        ]
        return data

    def create(self, valida_data, session):

        try:
            valida_data.update(
                {'user_id': session.pk}
            )

        except AttributeError:
            # Anonymous User
            valida_data.update({'user_id': 0})
        self.model.objects.create(**valida_data)

        return valida_data
