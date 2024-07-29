# Generate RSA private key + public keys
## Private:
```shell
openssl genrsa -out jwt-private.pem 2048
```
## Public:
```shell
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```