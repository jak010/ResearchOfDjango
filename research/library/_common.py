from django.core import serializers


def o2j(data):
    return serializers.serialize('json', data)
