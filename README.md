
A wrapper around the [neural-art](https://github.com/jcjohnson/neural-style) algorithm on the [21 marketplace](https://21.co/mkt/).  This repo is a python wrapper around the [deepstyle](https://github.com/tleyden/deepstyle) backend code to allow it to accept 21 marketplace payments.

## Example

| Image        | Style           | Result  |
| ------------- |:-------------:| -----:|
| <img src="http://tleyden-misc.s3.amazonaws.com/21style/flowers.jpg" width="200">     |  <img src="http://tleyden-misc.s3.amazonaws.com/21style/pollock_key.jpg" width="200"> | <img src="http://tleyden-misc.s3.amazonaws.com/21style/flowers_pollock_key.jpg" width="200"> |



## Running service

First you will need to get a [DeepStyle Sync Gateway database](https://github.com/tleyden/deepstyle) and supporting change listeners up and running.

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


