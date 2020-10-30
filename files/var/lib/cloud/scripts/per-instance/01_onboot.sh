#!/bin/bash

export DEBIAN_FRONTEND=noninteractive
export LC_ALL=C
export LANG=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

# Generate Yacht admin pass

yacht_admin_pass=$(openssl rand -hex 24)

# Save the password
cat > /root/.yacht_password <<EOM
yacht_admin_pass="${yacht_admin_pass}"
EOM


# Launch container with the password
docker run -d \
    -p 8000:8000/tcp \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /opt/Yacht:/config \
    -e "ADMIN_PASS=${yacht_admin_pass}" \
    --restart=always \
    selfhostedpro/yacht:do