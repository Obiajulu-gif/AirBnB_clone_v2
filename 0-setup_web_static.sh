#!/usr/bin/env bash
# Install Nginx if not already installed

if ! [ -x "$(command -v nginx)" ]; then
    apt-get -y update
    apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
sed -i '/^}/ i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$config_file"

service nginx restart

exit 0
