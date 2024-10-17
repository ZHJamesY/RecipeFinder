# Nginx image
FROM nginx

# remove the default nginx.conf from Nginx image
# RUN rm /etc/nginx/conf.d/default.conf

# replace with our own nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

# COPY nginx.conf /etc/nginx/conf.d/