
## Building AMI

```
packer build -var 'source_ami=ami-116d857a' -var 'ssh_username=ec2-user' -var 'access_key=YOUR_AWS_ACCESS_KEY' -var 'secret_key=YOUR_AWS_SECRET_KEY' 
```


