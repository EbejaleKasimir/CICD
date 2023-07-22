Dockerfile
# Dockerfile for installing NGINX
# NGINX is a popular web server, reverse proxy server, load balancer, and HTTP cache.
# Using Ubuntu 20.04 as the base image
FROM ubuntu:20.04
 # Label information
LABEL maintainer="Ebejale"
 # Update the package lists for upgrades and new package installations
RUN apt-get update
 # Install NGINX
RUN apt-get install -y nginx
 # Add your custom index.html to the default NGINX directory
ADD index.html /usr/share/nginx/html/index.html
 # Start NGINX when the container starts, running in the foreground
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
 # Expose port 80 for the NGINX server
EXPOSE 80