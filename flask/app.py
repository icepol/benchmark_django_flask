from flask import Flask
from redis import Redis

application = Flask(__name__)
redis = Redis(host='localhost', port=6379)


@application.route('/')
def hello():
    redis.incr('hits')
    return 'hello {} times'.format(redis.get('hits'))


if __name__ == 'main':
    application.run('0.0.0.0', debug=False)
