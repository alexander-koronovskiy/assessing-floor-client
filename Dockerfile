# Build app
FROM node:16-alpine3.16 AS builder
ARG ENV=production
ENV NODE_ENV=$ENV
ENV npm_config_loglevel=error
ENV npm_config_update-notifier=false
WORKDIR /app
COPY . .
RUN echo $NODE_ENV
RUN npm ci --include=dev
RUN npm run build


FROM alpine:3.16
ARG ENV=production
RUN apk update && \
  apk upgrade && \
  apk add --no-cache \
  tzdata \
  nginx \
  nginx-mod-http-brotli \
  curl \
  && rm -rf /var/cache/apk/ \
  && rm -rf /root/.cache \
  && rm -rf /tmp/* \
  && cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
  && echo "Europe/Moscow" >> /etc/timezone
COPY ./docker/nginx/config/* /etc/nginx/
WORKDIR /app
COPY --from=builder /app/dist/ /app
HEALTHCHECK --interval=5s --timeout=2s \
  CMD curl -f http://127.0.0.1:8080/ping/ || exit 1
EXPOSE 8080
ENTRYPOINT ["nginx"]
CMD ["-g daemon off;"]
