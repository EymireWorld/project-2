# Env files structure
## db.env
```
POSTGRES_HOST: str
POSTGRES_DB: str
POSTGRES_USER: str
POSTGRES_PASSWORD: str
```
## app.env
```
JWT_TOKEN_LIFETIME: int
```
## How to start
1. Clone repository
```shell
git clone https://github.com/EymireWorld/project-1.git
```
2. Export requirements
```shell
poetry export --without-hashes -o requirements.txt
```
3. Start docker container
```shell
docker compose up -d
```
4. Join app shell
```shell
docker exec -t app sh
```
5. Start migrations
```shell
alembic revision --autogenerate
alembic upgrade head
```
6. Generate RSA keys
```shell
cd certificates
openssl genrsa -out jwt-private.pem 2048
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```
7. Enjoy)