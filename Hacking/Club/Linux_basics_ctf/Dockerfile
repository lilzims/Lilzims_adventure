# Use a base image with interactive shell
FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && \
    apt-get install -y apt-utils openssl cron openssh-server
RUN apt-get install -y curl wget git vim net-tools nano  

# Create user 'linus' with password 'torvalds'
RUN useradd -m -p $(openssl passwd -1 torvalds) linus

# Set up crontab process
USER linus
RUN echo "* * * * * echo 'ctf(cr0n_757842)'" | crontab -
USER root

# Create file in /var/www
RUN mkdir /var/www && \
    echo "ctf(w3b_d1r_637348)" > /var/www/file.txt

# Append flag to .bashrc
RUN echo "export flag='ctf(3nviron_4C696E)'" >> /home/linus/.bashrc
RUN echo "#echo 'ctf(us3r_d@t@_617369)'" >> /home/linus/.bashrc

# Create directory in root
RUN mkdir /app && \
    echo "ctf(out_0f_PLAce_617468)" > /app/.app.txt
RUN touch /app/what.txt
RUN echo "Something seems off about this directory........." >> what.txt 

# Create a file in linus's home directory documents folder
RUN mkdir /home/linus/Desktop && mkdir /home/linus/Downloads && mkdir /home/linus/Music
RUN mkdir -p /home/linus/Documents && \
    echo "01011001 00110011 01010010 01101101 01001011 01000111 01010010 01101100 01011001 01111010 01000010 01000101 01011010 01010110 00111000 00110010 01001101 01010100 01011001 01111010 01001110 01101011 01001001 01110000" > /home/linus/Documents/b64.txt

# Copy flag.txt from your local machine to /bin
COPY flag.txt /bin/flag.txt

# Remove read privileges for others
RUN chmod o-r /bin/flag.txt

# Set execute permission for linus user
RUN chmod +x /bin/flag.txt && chown linus /bin/flag.txt

# Set root password
RUN echo 'root:ctf(LinuxBasicsHackathon)' | chpasswd

# Set working directory
WORKDIR /home/linus

# Configure SSH
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo 'Banner /etc/ssh/banner' >> /etc/ssh/sshd_config

# Create SSH banner with custom message
RUN echo "Welcome to Linus's Docker container. The password is the last name of the creator of Linux." > /etc/ssh/banner

# Expose SSH port
EXPOSE 22

RUN export flag="ctf(3nviron_4C696E)"

# Start SSH service and interactive shell
CMD ["/usr/sbin/sshd", "-D"]
