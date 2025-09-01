FROM nginx:alpine
RUN rm -f /etc/nginx/conf.d/default.conf
COPY app.conf.template /etc/nginx/templates/app.conf.template