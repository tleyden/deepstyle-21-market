
## Calling flask service

```
curl -H "Content-Type: application/json" -X POST -d '{"style_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/van_gogh.jpg", "content_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/backyard.jpg"}' http://localhost:8000/buy
```

## Building AMI

```
packer build -var 'source_ami=ami-116d857a' -var 'ssh_username=ec2-user' -var 'access_key=YOUR_AWS_ACCESS_KEY' -var 'secret_key=YOUR_AWS_SECRET_KEY' 
```


