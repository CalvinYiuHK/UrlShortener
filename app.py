from flask import Flask, request, redirect, abort
import configparser
import validators
import shortuuid
import logging
from db import UrlDatabase

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# api for submitting url, return the shorten url
@app.route('/shorten', methods=['POST'])
def shorten():
    conn = UrlDatabase()
    if request.method == 'POST':
        try:
            url = request.get_json()['URL']
            if not validators.url(url):
                raise ValueError('Invalid Url format')

            result = conn.check(url)
            if result:
                return result['ShortUrl']

            # code for short url
            code = shortuuid.ShortUUID().random(length=8)

            # prevent code collision
            while conn.collection.find_one({'UrlCode': code}):
                code = shortuuid.ShortUUID().random(length=8)

            short_url = f"{config['general']['BaseUrl']}:{config['general']['Port']}/{code}"
            conn.insert(url, short_url, code)
            return short_url

        except Exception as e:
            logging.exception('POST data format not correct')
            return 'POST data format not correct'
    else:
        return 'Method not supported'


# redirect to the long url
@app.route('/<code>')
def code_router(code):
    conn = UrlDatabase()
    result = conn.collection.find_one({'UrlCode': code})
    if result:
        return redirect(result['LongUrl'])

    abort(404)


if __name__ == '__main__':
    app.run(port=config['general']['Port'], host='0.0.0.0')
