# Use the official Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables to non-interactive to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y \
        sudo \
        openssh-server \
        mysql-client \
        cron \
        netcat \
        vim \
        supervisor \
        wget \
        gnupg \
        lsb-release \
        python3 \
        python3-pip \
        less \
        perl \
        curl \
        sshpass \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m neo && \
    useradd -m morpheus && \
    useradd -m trinity && \
    useradd -m agent_smith && \
    echo "neo:FollowTheWhiteRabbit!" | chpasswd && \
    echo "morpheus:TheRedPill" | chpasswd && \
    echo "trinity:Tr1n1tyP@ss" | chpasswd && \
    echo "agent_smith:MrAnderson!" | chpasswd && \
    usermod -aG sudo neo

# Set home directories with restricted access for each user
RUN chmod 700 /home/neo /home/morpheus /home/trinity /home/agent_smith

# Create substantial directory structures for each user
RUN mkdir -p /home/neo/Desktop /home/neo/Downloads /home/neo/Documents /home/neo/.config /home/neo/.ssh /home/neo/.wallpapers \
    /home/neo/Projects /home/neo/Scripts /home/neo/Archives /home/neo/VirtualEnvs /home/neo/backups /home/neo/Notes \
    /home/morpheus/.config /home/morpheus/.ssh /home/morpheus/Philosophy /home/morpheus/Scripts /home/morpheus/Documents \
    /home/morpheus/Downloads /home/morpheus/MissionFiles /home/morpheus/.gnupg /home/morpheus/.cache /home/morpheus/.wallpapers \
    /home/trinity/.config /home/trinity/Documents /home/trinity/.ssh /home/trinity/Operations /home/trinity/Hacks /home/trinity/Backups \
    /home/trinity/Downloads /home/trinity/Scripts /home/trinity/Research /home/trinity/.cache /home/trinity/.local/share \
    /home/agent_smith/Documents /home/agent_smith/.cache /home/agent_smith/.trash /home/agent_smith/Logs /home/agent_smith/Analysis \
    /home/agent_smith/.config /home/agent_smith/Surveillance /home/agent_smith/Recon /home/agent_smith/Operations /home/agent_smith/.ssh \
    /opt/tools /var/log/rotated /usr/share

RUN chown -R neo:neo /home/neo && \
    chown -R morpheus:morpheus /home/morpheus && \
    chown -R trinity:trinity /home/trinity && \
    chown -R agent_smith:agent_smith /home/agent_smith

RUN chmod 700 /home/neo/.ssh /home/neo/VirtualEnvs /home/morpheus/MissionFiles /home/morpheus/.gnupg /home/trinity/Operations \
    /home/trinity/Hacks /home/agent_smith/Surveillance /home/agent_smith/Recon


RUN echo "flag{TheM4tr1xHasY0u}" > /home/neo/Desktop/welcome_flag.txt && \
    echo "flag{F0ll0wTheWh1teR4bbit}" | base64 > /home/neo/Documents/hidden_clue.b64 && \
    echo "flag{Gl1mps3TheTruth}" > /home/neo/Downloads/truth.txt && \
    echo "flag{Syst3mFa1lur3}" > /home/neo/Projects/system_failure.log && \
    echo "flag{W4k3UpN3o}" | xxd -p > /home/neo/Notes/dreams.hex && \
    echo "flag{Th3r3IsN0Sp00n}" > /home/morpheus/Philosophy/spoon.txt && \
    echo "flag{Tak3TheR3dP1ll}" | base64 > /home/morpheus/Scripts/pill.b64 && \
    echo "flag{The0ne}" > /home/morpheus/MissionFiles/one.txt && \
    echo "flag{Re4l1tyIsAnIllusi0n}" > /home/morpheus/Documents/reality_check.txt && \
    echo "flag{TheMatrixR3l0aded}" | xxd -p > /home/morpheus/.cache/reload.hex && \
    echo "flag{CodeIsAWeapon}" > /home/trinity/Operations/weapon_code.txt && \
    echo "flag{PathOfTheChosen}" > /home/trinity/Hacks/path.txt && \
    echo "flag{ControlIsAnIllusion}" > /home/trinity/Research/control.txt && \
    echo "flag{EscapingTheMatrix}" | base64 > /home/agent_smith/Recon/escape.b64 && \
    echo "flag{MrAnderson}" > /home/agent_smith/Analysis/mr_anderson.txt

RUN chown neo:neo /home/neo/Desktop/welcome_flag.txt /home/neo/Documents/hidden_clue.b64 /home/neo/Downloads/truth.txt \
    /home/neo/Projects/system_failure.log /home/neo/Notes/dreams.hex && \
    chown morpheus:morpheus /home/morpheus/Philosophy/spoon.txt /home/morpheus/Scripts/pill.b64 \
    /home/morpheus/MissionFiles/one.txt /home/morpheus/Documents/reality_check.txt /home/morpheus/.cache/reload.hex && \
    chown trinity:trinity /home/trinity/Operations/weapon_code.txt /home/trinity/Hacks/path.txt \
    /home/trinity/Research/control.txt && \
    chown agent_smith:agent_smith /home/agent_smith/Recon/escape.b64 /home/agent_smith/Analysis/mr_anderson.txt


# Install Flask for the API service
RUN pip3 install flask

# Set up SSH with The Matrix-themed login hint
RUN mkdir /var/run/sshd && \
    echo 'Welcome, the Matrix has you...' | tee /etc/motd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    echo "UseDNS no" >> /etc/ssh/sshd_config

# ============================
# 1. Hidden File Flag (The Matrix-style)
# ============================
RUN echo 'cahsi-{the_matrix_is_real}' > /home/neo/.the_matrix_flag.txt && \
    chown neo:neo /home/neo/.the_matrix_flag.txt && \
    chmod 600 /home/neo/.the_matrix_flag.txt

# ============================
# 2. Environment Variable Flag (Matrix code hint)
# ============================
RUN echo 'export FLAG_ENV="cahsi-{follow_the_white_rabbit}"' >> /home/neo/.bashrc

# ============================
# 3. Process Inspection Flag (Matrix reference)
# ============================
# A script that runs with a flag reference to "The Matrix"
RUN echo '#!/bin/bash\necho "The Matrix has a glitch: cahsi-{process_glitch_detected}"\nsleep 600' > /usr/local/bin/matrix_glitch && \
    chmod +x /usr/local/bin/matrix_glitch


# ============================
# 5. SSH Configuration Flag (Matrix agent hint)
# ============================
RUN mkdir -p /home/neo/.ssh && \
    echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3... neo@matrix # cahsi-{neo_ssh}' > /home/neo/.ssh/authorized_keys && \
    chown -R neo:neo /home/neo/.ssh && \
    chmod 700 /home/neo/.ssh 

# ============================
# 6. Cron Job Flag (Cron hint)
# ============================
RUN echo '* * * * * echo "cahsi-{time_is_an_illusion}"' | crontab -u neo -

# ============================
# 7. Permission-Based Flag
# ============================
RUN groupadd agents && \
    echo 'cahsi-{only_for_agents}' > /home/neo/flag_restricted.txt && \
    chown neo:agents /home/neo/flag_restricted.txt && \
    chmod 640 /home/neo/flag_restricted.txt

# ============================
# 8. Log File Flag (Log hint)
# ============================
RUN echo "cahsi-{trace_the_system_logs}" >> /var/log/syslog

# ============================
# 9. Vulnerable API Flag (API with Matrix-themed secret)
# ============================
# Create the flag file with restricted permissions
RUN echo "cahsi-{breaking_the_game}" > /home/neo/.secret_matrix_flag && \
    chmod 600 /home/neo/.secret_matrix_flag && \
    chown root:root /home/neo/.secret_matrix_flag

RUN mkdir /home/neo/matrix_api/
   
RUN echo 'from flask import Flask, request, jsonify\n\
\n\
app = Flask(__name__)\n\
\n\
@app.route("/api/v1/secret", methods=["GET"])\n\
def secret():\n\
    token = request.args.get("token")\n\
    if token:\n\
        with open("/home/neo/.secret_matrix_flag", "r") as f:\n\
            secret_flag = f.read().strip()\n\
        return jsonify({"secret": secret_flag}), 200\n\
    else:\n\
        return jsonify({"error": "Unauthorized access"}), 403\n\
\n\
if __name__ == "__main__":\n\
    app.run(host="0.0.0.0", port=5000)\n' > /home/neo/matrix_api/app.py && \
    chmod +x /home/neo/matrix_api/app.py


# ============================
# 10. Network Service Flag (Matrix hint)
# ============================
RUN echo '#!/bin/bash\n\
while true; do\n\
    echo "cahsi-{matrix_network_infiltration}" | nc -l -p 9000 -q 1;\n\
done' > /usr/local/bin/matrix_netcat_flag.sh && \
    chmod +x /usr/local/bin/matrix_netcat_flag.sh

# ============================
# 11. Lateral Escalation Users
# ============================
RUN echo "neo ALL=(morpheus) NOPASSWD: /usr/bin/less" >> /etc/sudoers.d/matrix_escalation && \
    echo "morpheus ALL=(trinity) NOPASSWD: /usr/bin/perl" >> /etc/sudoers.d/matrix_escalation && \
    echo "trinity ALL=(agent_smith) NOPASSWD: /usr/bin/awk" >> /etc/sudoers.d/matrix_escalation

# Set up hints for Neo to find the secrets
RUN echo "Hint: Neo, the path to truth lies within the system logs. Search for the hidden password for your account." > /home/agent_smith/neo_password_hint.txt && \
    chown agent_smith:agent_smith /home/agent_smith/neo_password_hint.txt && \
    chmod 600 /home/agent_smith/neo_password_hint.txt 

RUN echo "There is a secret user for neo with the password 'FollowTheWhiteRabbit!'" >> /var/log/syslog

RUN echo "Hint: The database user is 'hackuser' and the password is 'hackpassword'" > /home/neo/db_password_hint.txt && \
    chown neo:neo /home/neo/db_password_hint.txt && \
    chmod 600 /home/neo/db_password_hint.txt

# +++++++==========+++++++++++++++++++==========+++++++++++++++++++==========++++++++++++
# Inserting some cute little flags around here SINCE MARTY CAN'T DO HIS JOB!!!!!! kidding XP
# +++++++==========+++++++++++++++++++==========+++++++++++++++++++==========++++++++++++

# ============================
# 1. Neo's Desktop Flag
# ============================
RUN echo 'cahsi-{take_the_red_pill}' > /home/neo/Desktop/flag_red_pill.txt && \
    chown neo:neo /home/neo/Desktop/flag_red_pill.txt && \
    chmod 400 /home/neo/Desktop/flag_red_pill.txt

# ============================
# 2. Agent Smith's Documents Flag
# ============================
RUN echo 'cahsi-{inevitable_control}' > /home/agent_smith/Documents/flag_inevitable.txt && \
    chown agent_smith:agent_smith /home/agent_smith/Documents/flag_inevitable.txt && \
    chmod 400 /home/agent_smith/Documents/flag_inevitable.txt


# ============================
# 4. Morpheus’s Config Flag
# ============================
RUN echo 'cahsi-{free_your_mind}' > /home/morpheus/.config/flag_free_mind.txt && \
    chown morpheus:morpheus /home/morpheus/.config/flag_free_mind.txt && \
    chmod 400 /home/morpheus/.config/flag_free_mind.txt

# ============================
# 5. Neo's SSH Directory Flag
# ============================
RUN echo 'cahsi-{unlocking_destiny}' > /home/neo/.ssh/flag_destiny.txt && \
    chown neo:neo /home/neo/.ssh/flag_destiny.txt && \
    chmod 400 /home/neo/.ssh/flag_destiny.txt

# ============================
# 6. Root’s Flag in /root Directory
# ============================
RUN echo 'cahsi-{system_overlord}' > /root/flag_root_access.txt && \
    chmod 400 /root/flag_root_access.txt

# ============================
# 7. Temp Directory Flag
# ============================
RUN echo 'cahsi-{glitch_in_the_matrix}' > /tmp/flag_glitch.txt && \
    chmod 444 /tmp/flag_glitch.txt

# ============================
# 8. /etc Directory Flag
# ============================
RUN echo 'cahsi-{system_configured}' > /etc/flag_config.txt && \
    chmod 444 /etc/flag_config.txt

# ============================
# 9. /var Directory Flag
# ============================
RUN echo 'cahsi-{trace_the_code}' > /var/flag_trace.txt && \
    chmod 444 /var/flag_trace.txt

# ============================
# 10. Log Directory Flag in /var/log
# ============================
RUN echo 'cahsi-{hidden_log_entry}' > /var/log/flag_log.txt && \
    chmod 444 /var/log/flag_log.txt

# ============================
# 11. /usr/share Directory Flag
# ============================
RUN echo 'cahsi-{share_the_secret}' > /usr/share/flag_secret.txt && \
    chmod 444 /usr/share/flag_secret.txt

# ============================
# 12. Lost+Found Directory Flag (for Neo)
# ============================
RUN mkdir -p /home/neo/lost+found && \
    echo 'cahsi-{lost_found}' > /home/neo/lost+found/flag_lost_found.txt && \
    chown neo:neo /home/neo/lost+found/flag_lost_found.txt && \
    chmod 400 /home/neo/lost+found/flag_lost_found.txt

# ============================
# 13. Manually Created Hidden Directory in Neo’s Home
# ============================
RUN mkdir -p /home/neo/.hidden_matrix && \
    echo 'cahsi-{hidden_truth}' > /home/neo/.hidden_matrix/flag_hidden.txt && \
    chown neo:neo /home/neo/.hidden_matrix/flag_hidden.txt && \
    chmod 400 /home/neo/.hidden_matrix/flag_hidden.txt

# ============================
# 14. Flag in Neo's Downloads Directory
# ============================
RUN echo 'cahsi-{download_the_future}' > /home/neo/Downloads/flag_download.txt && \
    chown neo:neo /home/neo/Downloads/flag_download.txt && \
    chmod 400 /home/neo/Downloads/flag_download.txt

# ============================
# 15. Secret Flag in /opt Directory
# ============================
RUN echo 'cahsi-{opt_out}' > /opt/flag_opt_out.txt && \
    chmod 444 /opt/flag_opt_out.txt

# +++===+++===+++===+++===+++
# Making even more flags because why not 
# +++===+++===+++===+++===+++

# ============================
# 1. Hidden Flag in Neo’s Home .bashrc
# ============================
RUN echo 'cahsi-{wake_up_neo}' > /home/neo/.bashrc_flag.txt && \
    chown neo:neo /home/neo/.bashrc_flag.txt && \
    chmod 400 /home/neo/.bashrc_flag.txt

# ============================
# 2. Hidden Flag in Morpheus's Home .vimrc
# ============================
RUN echo 'cahsi-{follow_the_path}' > /home/morpheus/.vimrc_flag.txt && \
    chown morpheus:morpheus /home/morpheus/.vimrc_flag.txt && \
    chmod 400 /home/morpheus/.vimrc_flag.txt

# ============================
# 3. Secret Flag in Neo’s Wallpaper Directory
# ============================
RUN mkdir -p /home/neo/.wallpapers && \
    echo 'cahsi-{matrix_has_you}' > /home/neo/.wallpapers/flag_matrix_wall.txt && \
    chown neo:neo /home/neo/.wallpapers/flag_matrix_wall.txt && \
    chmod 400 /home/neo/.wallpapers/flag_matrix_wall.txt

# ============================
# 4. Agent Smith's Cache Directory Flag
# ============================
RUN mkdir -p /home/agent_smith/.cache && \
    echo 'cahsi-{inevitability_is_key}' > /home/agent_smith/.cache/flag_inevitability.txt && \
    chown agent_smith:agent_smith /home/agent_smith/.cache/flag_inevitability.txt && \
    chmod 400 /home/agent_smith/.cache/flag_inevitability.txt


# ============================
# 6. Hidden Flag in /usr/local Directory
# ============================
RUN echo 'cahsi-{you_cant_go_back}' > /usr/local/flag_no_return.txt && \
    chmod 444 /usr/local/flag_no_return.txt

# ============================
# 7. Log Rotation Directory Flag
# ============================
RUN mkdir -p /var/log/rotated && \
    echo 'cahsi-{illusion_of_choice}' > /var/log/rotated/flag_choice.txt && \
    chmod 444 /var/log/rotated/flag_choice.txt

# ============================
# 8. Flag in /opt/tools Directory
# ============================
RUN mkdir -p /opt/tools && \
    echo 'cahsi-{illusion_breaks}' > /opt/tools/flag_tools.txt && \
    chmod 444 /opt/tools/flag_tools.txt

# ============================
# 9. User Neo’s Backup Directory Flag
# ============================
RUN mkdir -p /home/neo/backups && \
    echo 'cahsi-{reality_is_relative}' > /home/neo/backups/flag_reality.txt && \
    chown neo:neo /home/neo/backups/flag_reality.txt && \
    chmod 400 /home/neo/backups/flag_reality.txt

# ============================
# 10. Flag in Agent Smith's Trash Directory
# ============================
RUN mkdir -p /home/agent_smith/.trash && \
    echo 'cahsi-{residual_self_image}' > /home/agent_smith/.trash/flag_residual.txt && \
    chown agent_smith:agent_smith /home/agent_smith/.trash/flag_residual.txt && \
    chmod 400 /home/agent_smith/.trash/flag_residual.txt


    # Copy the break_out.sh script into Neo's home directory
COPY break_out.sh /home/neo/break_out.sh
RUN chmod +x /home/neo/break_out.sh  # Make it executable

# Set permissions for sudoers files
RUN chmod 440 /etc/sudoers.d/*

# Set directory permissions for user home directories
RUN chmod 700 /home/neo && \
    chmod 700 /home/morpheus && \
    chmod 700 /home/trinity && \
    chmod 700 /home/agent_smith

# Expose necessary ports for The Matrix
EXPOSE 2222 9000 5000

# Configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor && \
    chown -R root:root /var/log/supervisor && \
    chmod -R 755 /var/log/supervisor



ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
