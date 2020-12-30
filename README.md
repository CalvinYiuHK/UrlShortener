# Flask Url Shortening API
This is a API to provide url shortening service. 

## Installation
Run the following line to install all the required package
```commandline
$ pip install -r requirements.txt
```

## Start the server
To use the service, the flask server need to be running, run the following command to start the server
```commandline
$ python app.py
```

## Use the service
When the service is running, it will accept two api request, one is for url shortening, one is for redirect the shortened url to the original url

### Shorten url service


#### Request

`POST /shorten/`

#### Data format

`{URL: original url}`

#### Response

`shortened url`

### Redirect service

#### Request

`GET /<code>/`

The server will redirect it to the original website


