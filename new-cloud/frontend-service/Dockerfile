FROM nginx

# Remove default Nginx config file
RUN rm /etc/nginx/conf.d/default.conf || true

# Copy our custom Nginx configration file
COPY nginx.conf /etc/nginx/conf.d/

# Copy HTML files
COPY html etc/nginx/html

# Expose the port
EXPOSE 80

# Start Nnginx when container is running
CMD [ "nginx", "-g", "daemon off;" ]