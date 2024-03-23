FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server cron samba python3 python3-pip && \
    apt-get clean && \
    apt-get install sudo &&\
    apt-get install less && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy api.py and set up Flask application
COPY api.py /app/api.py
WORKDIR /app
RUN pip3 install Flask


# Create SSH banner with custom message
RUN echo "Welcome to trinity's machine." > /etc/ssh/banner

# Create the trinity user
RUN useradd -m -p $(openssl passwd -1 tiffany) trinity

#Create the morpheus user
RUN useradd -m -p $(openssl passwd -1 Nebuchadnezzar) morpheus

#Create the neo user
RUN useradd -m -p $(openssl passwd -1 matrix) neo

#Create the smith user
RUN useradd -m -p $(openssl passwd -1 agent) smith

# Add morpheus to the blue_pill_group
RUN groupadd blue_pill_group && \
    usermod -aG blue_pill_group morpheus

# Enable password authentication
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Configure SSH
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo 'Banner /etc/ssh/banner' >> /etc/ssh/sshd_config

# Set up directories for morpheus, neo, and trinity
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
             /home/morpheus/Videos \
             /home/neo/Documents \
             /home/neo/Desktop \
             /home/neo/Downloads \
             /home/neo/Pictures \
             /home/neo/Music \
             /home/neo/Videos \
             /home/trinity/Documents/Personal/Hobbies \
             /home/trinity/Desktop \
             /home/trinity/Downloads \
             /home/trinity/Pictures \
             /home/trinity/Music \
             /home/trinity/Videos 

# Set permissions for home directories
RUN chown -R morpheus:morpheus /home/morpheus && \
    chown -R neo:neo /home/neo && \
    chown -R trinity:trinity /home/trinity && \
    chmod 700 /home/morpheus /home/neo /home/trinity


#add rot13-b64 flag
USER trinity
RUN echo 'cGdzKHJhcDBxMyk=' >> /home/trinity/Documents/Personal/Hobbies/bookclub.txt 

# Switch back to root user
USER root

#Insert base line flags
RUN echo 'ctf(tr1n_h0m3) Password for next user, Morpheus: Nebuchadnezzar' >> /home/trinity/.hidden.txt
RUN echo 'The hints for this user is: look through Trinitys files to find an encoded flag' >> /home/trinity/.hidden.txt
RUN echo 'ctf(m0rph3us_h0me) Password for next user, neo: matrix' >> /home/morpheus/.hidden.txt
RUN echo 'The hint for this user is look into their cron and find all the files that are owned by the group morpheus is in' >> /home/morpheus/.hidden.txt
RUN echo 'ctf(n30_h0m3) cat /etc/sudoers to find how to get to the final root user' >> /home/neo/.hidden.txt
RUN echo 'The hints for this is /etc directory has some passwords in it you should look at XP' >> /home/neo/.hidden.txt


# Move Group Access flag to another directory
RUN mkdir /flags && \
    echo 'ctf(n3o_is_the_1)' > /flags/group_access_flag.txt && \
    chmod 440 /flags/group_access_flag.txt

RUN chown root:blue_pill_group /flags/group_access_flag.txt

USER morpheus
# Set up Cron job for morpheus
RUN echo '* * * * * echo "ctf(m0rph3us_j0b)" >> /home/morpheus/Pictures/.cron_flag.txt' | crontab -

# Switch back to root user
USER root

# Add a flag in the /etc/passwd file
RUN echo "ctf(ch0s3n_0n3)" >> /etc/passwd

# Change ownership of neo's flag as root
RUN echo "ctf(Alm0st_0ut)" >> /home/neo/neo_flag.txt
RUN chown root:root /home/neo/neo_flag.txt
RUN echo "neo ALL=(root) NOPASSWD: /usr/bin/less /home/neo/neo_flag.txt" >> /etc/sudoers
RUN chmod 400 /home/neo/neo_flag.txt


# Set root password and root flag
RUN echo 'root:th3_matr1x' | chpasswd
RUN echo "ctf(3scap3d_th3_m4tr1x)" >> /root/root.txt

# Configure SMB share accessible to anonymous users
RUN mkdir /srv/.smb_share && \
    echo 'ctf(m1ltiplying_smb)' > /srv/.smb_share/flag.txt && \
    chmod -R 777 /srv/.smb_share && \
    printf "[global]\n   map to guest = bad user\n\n[public]\n   path = /srv/.smb_share\n   browsable = yes\n   read only = no\n   guest ok = yes" > /etc/samba/smb.conf

COPY ./data.txt.enc /flags/data.txt.enc
COPY ./private.pem /flags/private.pem

# Add a cron job to display text every 30 seconds
RUN echo '*/30 * * * * root echo "ctf(m1ltipl1er_pr0cesses)"' > /etc/cron.d/multiplier_process

# Copy service file into the container
COPY flask-api.service /etc/systemd/system/flask-api.service

# Expose SSH, Flask, and SMB ports
EXPOSE 22 5000 445

# Change the file in app to make it executable
RUN chmod +x /app/api.py

# Start SSH and SMB services, and run Flask application
CMD service cron start && service smbd start && /usr/sbin/sshd -D && python3 /app/api.py
