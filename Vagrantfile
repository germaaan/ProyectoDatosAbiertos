# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "CKAN"
  # config.vm.provision :shell, path: "bootstrap.sh"
  # config.vm.network :forwarded_port, host: 9200, guest: 9200
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 1
    v.name = config.vm.hostname.to_s
  end

end
