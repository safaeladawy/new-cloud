# Base Image
FROM nginx

# Remove default config file
RUN rm /etc/nginx/conf.d/default.conf || true

# Add custom config file
COPY nginx.conf /etc/nginx/conf.d

# Expose port
EXPOSE 80

# Start nginx-server
CMD [ "nginx-debug", "-g", "daemon off;" ]


