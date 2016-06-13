
A wrapper around the [neural-art](https://github.com/jcjohnson/neural-style) algorithm on the [21 marketplace](https://21.co/mkt/).  This repo is a python wrapper around the [deepstyle](https://github.com/tleyden/deepstyle) backend code to allow it to accept 21 marketplace payments.

## Example

| Image        | Style           | Result  |
| ------------- |:-------------:| -----:|
| <img src="http://tleyden-misc.s3.amazonaws.com/21style/flowers.jpg" width="200">     |  <img src="http://tleyden-misc.s3.amazonaws.com/21style/pollock_key.jpg" width="200"> | <img src="http://tleyden-misc.s3.amazonaws.com/21style/flowers_pollock_key.jpg" width="200"> |


## Using the service

```
21 buy --maxprice 275000 -H "Content-Type: application/json" -X POST \ 
-d '{"style_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/pollock_key.jpg", \
"content_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/flowers.jpg"}' \ 
http://10.244.164.194:8001/buy
```

## Running service

Follow the [deepstyle](https://github.com/tleyden/deepstyle) instructions to get the service up and running, and then run the python wrapper to put it on the 21 marketplace.


```
$ git clone <this repo>
$ cd deepstyle-21-market
$ export DEEPSTYLE_SYNC_GATEWAY_URL=http://yourserver.io
$ export DEEPSTYLE_SYNC_GATEWAY_DB=yourdb
$ export DEEPSTYLE_SYNC_GATEWAY_USERNAME=your_username
$ export DEEPSTYLE_SYNC_GATEWAY_PASSWORD=password
$ python3 flask_service.py
```

## Calling API

```
curl -H "Content-Type: application/json" -X POST -d '{"style_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/van_gogh.jpg", "content_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/backyard.jpg"}' http://localhost:8000/buy
```

## Building AMI

```
packer build -var 'source_ami=ami-116d857a' -var 'ssh_username=ec2-user' -var 'access_key=YOUR_AWS_ACCESS_KEY' -var 'secret_key=YOUR_AWS_SECRET_KEY' 
```


