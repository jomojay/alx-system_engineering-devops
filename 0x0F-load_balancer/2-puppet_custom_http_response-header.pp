# i'm a puppet manifest to install nginx

exec { 'command':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo echo "Hello World" >> /var/www/html/index.nginx-debian.html
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
