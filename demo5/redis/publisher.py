import redis
import time
import string
import random

def publish_random_data():
    try:
        r = redis.StrictRedis(host='localhost', port=6379)

        while True:
            r.publish('random_data', ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)))
            time.sleep(5)

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    publish_random_data()
