# Use the official MySQL 8.0 as the base image
FROM mysql:8.0

# Set environment variables for MySQL, themed as Matrix references
ENV MYSQL_ROOT_PASSWORD="Z10nM@inframe"
ENV MYSQL_DATABASE="matrix_db"
ENV MYSQL_USER="hackuser"
ENV MYSQL_PASSWORD="hackpassword"

# Copy the initialization script to create tables and flags upon start
COPY --chown=mysql:mysql init.sql /docker-entrypoint-initdb.d/

# Expose MySQL port for access
EXPOSE 3306
