from redis import Redis
from django.http import HttpResponse

redis = Redis(host='localhost', port=6379)


def hello(request, *args, **kwargs):
    redis.incr('hits')
    return HttpResponse('hello {} times'.format(redis.get('hits')))
