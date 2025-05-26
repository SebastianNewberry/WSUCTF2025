FROM postgres:17.2

# Install Apache, PHP, and PHP-PostgreSQL support
RUN apt-get update && \
    apt-get install -y apache2 php libapache2-mod-php php-pgsql sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Enable Apache rewrite module
RUN a2enmod rewrite

# Create web root if it doesn't exist
RUN mkdir -p /var/www/html
RUN chmod o+w /var/log
RUN php -v

# Copy web files and Apache configuration
COPY src/ /var/www/html/
COPY entrypoint.sh /entrypoint.sh
COPY init.sql /init.sql
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN chmod +x /entrypoint.sh

# Expose Apache port
EXPOSE 80

# Use custom entrypoint
ENTRYPOINT ["/entrypoint.sh"]
