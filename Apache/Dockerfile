# Dockerfile for installing Apache
# Using Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Label information
LABEL key = Ebejale

# Set environment variables for Apache
ENV APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2 \
    APACHE_PID_FILE=/var/run/apache2/apache2.pid \
    APACHE_RUN_DIR=/var/run/apache2 \
    APACHE_LOCK_DIR=/var/lock/apache2

# Preconfigure tzdata package
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "Etc/Africa" > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    dpkg-reconfigure -f noninteractive tzdata

# Update the package lists for upgrades and new package installations
RUN apt-get update

# Install Apache and clean up the package lists to free up space
RUN apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Correct the Apache configuration file
RUN sed -i 's|^DefaultRuntimeDir.*|DefaultRuntimeDir /var/run/apache2|' /etc/apache2/apache2.conf
RUN apache2 -v
RUN mkdir -p /var/run/apache2
RUN chown -R www-data:www-data /var/run/apache2

# Expose port 80 for the Apache server
EXPOSE 80

# Start Apache in the foreground when the container starts
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
