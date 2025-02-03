# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"
  config.vm.define "despliegue" do |despliegue|
    despliegue.vm.hostname = "despliegue"
    despliegue.vm.network "forwarded_port", guest: 8080, host: 8080
    despliegue.vm.network "private_network", ip: "192.168.50.20"
    despliegue.vm.provision "shell", name: "basic_provision", inline: <<-SHELL
      sudo apt-get update && sudo apt-get install -y python3-pip
      sudo apt-get install -y nginx
      sudo mkdir -p /var/www/rconcan
      sudo chown -R $USER:www-data /var/www/rconcan
      sudo chmod -R 775 /var/www/rconcan
      cp /vagrant/conf-despliegue/.env /var/www/rconcan/.env
    
      SHELL

    despliegue.vm.provision "shell",  privileged: false, inline: <<-SHELL
      pip3 install pipenv
      pip3 install python-dotenv


    SHELL
  end # despliegue

end
#/home/vagrant/.local/share/virtualenvs/rconcan-mweWztWZ/bin/gunicorn
# /home/vagrant/.local/share/virtualenvs/msdocs-python-flask-webapp-quickstart-YrxIX3KC/bin/gunicorn
# gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app

#/home/vagrant/.local/share/virtualenvs/app2-8dqDLCtH/bin/gunicorn