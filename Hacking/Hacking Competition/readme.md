# Lilzims Adventure: The Matrix-themed CTF Docker Container

Welcome to **Lilzims Adventure**, a Capture The Flag (CTF) challenge container designed for the **GMIS Hackathon**! This project, inspired by the **Matrix** universe, provides an immersive environment for users to explore security vulnerabilities, flags, and access controls in a custom Ubuntu 22.04 setup. Built to help users improve their penetration testing and cybersecurity skills, this container hosts an array of scenarios and challenges that lead to flag discoveries.

### Repository Link
Find the codebase on GitHub: [Lilzims Adventure - Hacking Competition](https://github.com/lilzims/Lilzims_adventure/tree/master/Hacking/Hacking%20Competition)

---

## Features

This project utilizes Docker to create a secure sandbox where players can navigate through different tasks inspired by characters from the Matrix. Each character's environment has unique security flags, directories, permissions, and hints.

### Key Functionalities:

- **User Accounts**: Four users inspired by The Matrix — `neo`, `morpheus`, `trinity`, and `agent_smith` — each with unique access permissions and directory structures.
- **Flags**: Numerous flags are hidden across various files, directories, and configurations. Challenges require techniques like base64 encoding, hex decoding, log inspection, and privilege escalation to uncover.
- **API Service**: A Flask API with an endpoint providing restricted access, a hint for those with an eye for detail in network security.
- **Network and Cron Jobs**: Simulates network vulnerabilities and timed tasks with hidden flags, reinforcing concepts of service monitoring and process inspection.
- **SSH and Permissions**: Custom SSH configurations and escalated sudo permissions for lateral movement challenges.

---

## Installation and Setup

### Prerequisites

Ensure that [Docker](https://docs.docker.com/get-docker/) is installed on your system. This container is built to run in a local Docker environment for testing purposes.

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lilzims/Lilzims_adventure.git
    cd Lilzims_adventure/Hacking/Hacking Competition
    ```

2. **Build the Docker Image**:
    ```bash
    docker-compose build && docker-compose up -d
    ```
Make sure here that you are in the current directory with the docker-compose.tml

---

## Ports

- **2222**: SSH Access
- **9000**: Netcat Service (for the flag hint)
- **5000**: Flask API

---

## Challenges

Below are a few highlights of the challenges and concepts included in this CTF:

1. **Hidden Files**: Hidden files across different directories contain base64-encoded flags.
2. **Environment Variable Flags**: The `.bashrc` includes hints that need decoding to reveal flags.
3. **Process Flags**: Certain flags can only be found by inspecting running processes.
4. **Network Service Flag**: Netcat-based flag that simulates a listening service.
5. **Vulnerable API**: The Flask API contains a hidden flag if accessed with the correct token.
6. **Escalation Paths**: Users have permission settings allowing controlled privilege escalation, simulating real-world penetration scenarios.

---

## Supervision and Service Management

This container utilizes **Supervisor** to manage services, including:
- The `sshd` server (for SSH access)
- The Flask API service
- The netcat service

---

## Disclaimer

This project is designed for educational purposes and is not intended for any malicious use. Users are encouraged to respect ethical hacking standards while using this project.


Enjoy the adventure, and remember, **There is no spoon**!

