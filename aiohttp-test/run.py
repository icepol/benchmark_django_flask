from redis import Redis
from aiohttp import web


redis = Redis(host='localhost', port=6379)


async def hello(request):
    redis.incr('hits')
    body = 'hello {} times'.format(redis.get('hits'))
    return web.Response(body=body.encode('utf-8'))


app = web.Application()
app.router.add_route('GET', '/', hello)


if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=7777)
