# Dockerfile
FROM php:apache

# Copy your website files into the container's web root
COPY . /var/www/html/

# Set proper permissions (if needed)
RUN chown -R www-data:www-data /var/www/html

# Install sql because it wont work by default
RUN docker-php-ext-install mysqli

# Expose port 80 for web access
EXPOSE 80
