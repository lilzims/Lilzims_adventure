#!/bin/bash

# Use sshpass to connect to the exploit container via SSH as the_one user on port 2223
sshpass -p 'r3dP1ll' ssh -o StrictHostKeyChecking=no -p 2223 the_one@localhost