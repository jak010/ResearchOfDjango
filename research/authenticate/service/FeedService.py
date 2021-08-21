from dataclasses import dataclass, asdict


@dataclass
class FeedData:
    title: str = None
    content: str = None


class FeedService(object):

    def __init__(self, model):
        self.model = model

        # query result set
        self.query_result = self.model.objects.all()

    def read(self, query_param):

        # Data Initialize
        FeedDTO = FeedData(
            title=query_param.get('title'),
            content=query_param.get('content'),
        )

        query_result = self.query_result.filter(
            **self.filter_kwargs(FeedDTO),
        ).order_by('id')

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

    """ Method Notes
    01. filter_kwargs : query string to orm dict 
    
    """

    def filter_kwargs(self, feed_dto):
        filter_kwargs = {}
        for k, v in asdict(feed_dto).items():
            if v is not None:
                filter_kwargs.update({k: v})
        return filter_kwargs
