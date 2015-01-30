Installation
============

How to start developing
-----------------------
0. Before anything else install Ansible, Vagrant, and two vagrant plugins:  
   `vagrant plugin install vagrant-cachier`  
   `vagrant plugin install vagrant-vbguest`  
   Download VBoxGuestAdditions.iso for your version of VirtualBox
1. Remove `192.168.33.10` from the `~/.ssh/known_hosts` (otherwise error can occur during provision);
2. Switch to project's directory;
3. Comment this line in Vagrantfile, by adding `#`:  
   `config.vm.synced_folder ".", "/var/webapps/engus/code", owner: "engus", group: "engus"`
4. Start vagrant:  
   `vagrant up`
5. Make a provision of project:  
   `ansible-playbook deployment/provision.yml -i deployment/hosts/development`
6. Uncomment this line in Vagrantfile to allow syncing a project directory:  
   `config.vm.synced_folder ".", "/var/webapps/engus/code", owner: "engus", group: "engus"`
7. Now you have to reload vagrant, to sync your project directory with virtual server:  
   `vagrant reload`
8. Make a deploy of project:  
   `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
9. SSH to virtual server:  
   `vagrant ssh`
10. Switch to project user:  
   `sudo su -l engus`
11. Create website superuser with username `admin` and password `admin` for convention:  
   `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser`
12. Freeze installed python packages in requirements.txt file:  
    `/var/webapps/engus/virtualenv/bin/pip freeze > /var/webapps/engus/code/requirements.txt`
13. Start django development server:  
    `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001`
14. Now you can see your app running in browser:  
    `http://127.0.0.1:8002/`
15. Install static files libs (preferably I do this from local machine, not from virtual server):
    `cd engus/static/frontend`  
    `npm install`  
    `bower install`


Initial remote server setup
---------------------------
1. Add files:  
   `credentials/production/super_user_name`  
   `credentials/production/super_user_password`  
   `credentials/production/super_user_password_crypted`  
   `credentials/production/project_user_password`  
   `credentials/production/project_user_password_crypted`  
   `credentials/production/ssh_port`  
   `deployment/hosts/initial`  
   `deployment/hosts/production`  
2. Edit `deployment/vars.yml` file. Pay attention to `server_hostname`, `project_repo` and `remote_host` variables
3. Generate `id_rsa` ssh key in `deployment/files/ssh/` directory by command (it asks you where to generate key):  
   `ssh-keygen -t rsa -C "grialexey@gmail.com"`  
4. Add public key `id_rsa.pub` in your repository, to allow server pull this repository.  
   This command can help:  
   `cat deployment/files/ssh/id_rsa.pub | pbcopy`
5. Do initial provision of server:  
   `ansible-playbook deployment/initial.yml -i deployment/hosts/initial --ask-pass -c paramiko`  
6. Do project provision of server:  
   `ansible-playbook deployment/provision.yml -i deployment/hosts/production -K`  
7. Update system packages and upgrade them if needed:  
   `ansible-playbook deployment/upgrade.yml -i deployment/hosts/production -K`  
8. Make first deploy of project:  
   `ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`
9. Login on remote server and create superuser;
10. Enjoy your project!


Useful commands
---------------
`vagrant ssh`  
`sudo su -l engus`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py shell`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001`  

`/var/webapps/engus/virtualenv/bin/pip install <package>`  
`/var/webapps/engus/virtualenv/bin/pip freeze > /var/webapps/engus/code/requirements.txt`


Passwords crypt
---------------
`>>> openssl passwd -salt salty -1 mypass`
