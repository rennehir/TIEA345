import redis

def redis_check():
    try:
        r = redis.StrictRedis(host='localhost', port=6379)

        p = r.pubsub()
        p.subscribe('random_data')

        while True:
            message = p.get_message()
            if message:
                print(message['data'])

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    redis_check()
