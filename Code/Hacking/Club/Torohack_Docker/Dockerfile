FROM ubuntu:latest

# Install SSH server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create the trinity user
RUN useradd -m -p $(openssl passwd -1 tiffany) trinity

#Create the morpheus user
RUN useradd -m -p $(openssl passwd -1 Nebuchadnezzar) morpheus

#Create the neo user
RUN useradd -m -p $(openssl passwd -1 matrix) neo

#Create the smith user
RUN useradd -m -p $(openssl passwd -1 agent) smith

# Enable password authentication
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Create directories for trinity
USER trinity
RUN mkdir -p /home/trinity/Documents \
             /home/trinity/Documents/Personal \
             /home/trinity/Documents/Personal/Hobbies \
             /home/trinity/Documents/Work \
             /home/trinity/Documents/work/spreadsheets \
             /home/trinity/Desktop \
             /home/trinity/Desktop/random \
             /home/trinity/Desktop/dontlookhere \
             /home/trinity/Desktop/cats \
             /home/trinity/Downloads \
             /home/trinity/Pictures \
             /home/trinity/Music \
             /home/trinity/Videos

# Create directories for morpheus
USER morpheus
RUN mkdir -p /home/morpheus/Documents \
             /home/morpheus/Documents/random \
             /home/morpheus/Documents/random/randomer \
             /home/morpheus/Documents/cyber \
             /home/morpheus/Documents/cyber/miles \
             /home/morpheus/Desktop \
             /home/morpheus/Desktop/random \
             /home/morpheus/Desktop/jfkdlsahg \
             /home/morpheus/Desktop/cats \
             /home/morpheus/Downloads \
             /home/morpheus/Pictures \
             /home/morpheus/Music \
             /home/morpheus/Videos

# Create directories for neo
USER neo
RUN mkdir -p /home/neo/Documents \
             /home/neo/Documents/Personal \
             /home/neo/Documents/Personal/Hobbies \
             /home/neo/Documents/Work \
             /home/neo/Documents/work/spreadsheets \
             /home/neo/Desktop \
             /home/neo/Desktop/random \
             /home/neo/Desktop/dontlookhere \
             /home/neo/Desktop/cats \
             /home/neo/Downloads \
             /home/neo/Pictures \
             /home/neo/Music \
             /home/neo/Videos

# Create directories for smith    
USER smith    
RUN mkdir -p /home/smith/Documents \
             /home/smith/Documents/Personal \
             /home/smith/Documents/Personal/Hobbies \
             /home/smith/Documents/Work \
             /home/smith/Documents/work/spreadsheets \
             /home/smith/Desktop \
             /home/smith/Desktop/random \
             /home/smith/Desktop/dontlookhere \
             /home/smith/Desktop/cats \
             /home/smith/Downloads \
             /home/smith/Pictures \
             /home/smith/Music \
             /home/smith/Videos

#add rot13-b64 flag
USER trinity
run echo 'cGdzKHJhcDBxMyk=' >> /home/trinity/Documents/Personal/Hobbies/bookclub.txt 
run echo 'ctf(tr1n_h0m3)' >> /home/trinity/.hidden.txt

# Switch back to root user
USER root


# Configure SSH
RUN mkdir /var/run/sshd && \
    echo 'trinity:tiffany' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    echo 'Banner /etc/ssh/banner' >> /etc/ssh/sshd_config

# Create SSH banner with custom message
RUN echo "Welcome to trinity's machine." > /etc/ssh/banner

# Expose SSH port
EXPOSE 22

# Start SSH service and interactive shell
CMD ["/usr/sbin/sshd", "-D"]
RUN echo 'Banner /etc/ssh/banner' >> /etc/ssh/sshd_config

# Create SSH banner with custom message
RUN echo "Welcome to trinity's machine." > /etc/ssh/banner

# Expose SSH port
EXPOSE 22

# Start SSH service and interactive shell
CMD ["/usr/sbin/sshd", "-D"]
