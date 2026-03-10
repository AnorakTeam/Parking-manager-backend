# Frontend (vanilla HTML/JS/CSS) - Nginx
FROM nginx:alpine

# use our config
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY *.html *.css *.js /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
