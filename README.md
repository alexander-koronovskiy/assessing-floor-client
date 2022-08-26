# assessing-floor-client

# Запуск клиента
```
npm run serve
```

## Local docker test

```
docker build --build-arg ENV=production --tag assessing-floor-client:latest --file ./Dockerfile .
```

```
docker run -d -p 8080:8080 --restart=always --name "assessing-floor-client" assessing-floor-client:latest
```