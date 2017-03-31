Vagrant.configure(2) do |config|
  config.vm.box = "debian/jessie64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000  # Flask app
  config.ssh.forward_agent = true
  config.ssh.insert_key = true
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cpuexecutioncap", "75"]
    vb.cpus = 4
    vb.gui = false
    vb.memory = "4096"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant-playbook.yml"
    # ansible.verbose = true
  end
end
