# Netbox Docker Instance
Netbox is currently running in a Docker container. Netbox is installed using my `netbox_docker` role.  

## Role
The role does not install Docker and it assumes it is already installed.  

There are various variables available for the `netbox_docker` role.  

install netbox onto docker server  
```yaml
netbox_docker: true
```  

default credentials for the container can be controlled using the following variables  
```yaml
default_admin_username: admin
default_admin_email: admin@lab.lan
default_admin_password: Defaultpassword1
```
install location
```yaml
install_directory: /usr/local/netbox_docker 
```
backing up the sql database of netbox can be controlled with the following variables
```yaml
netbox_docker_backup: false
backup_file: db_dump.sql.gz
backup_database_command: docker compose exec -T postgres sh -c 'pg_dump -cU $POSTGRES_USER $POSTGRES_DB' | gzip > {{ backup_file }}
database_backup_location: ../backups/{{ ansible_hostname }}/{{ backup_file }}  
```
restoring the database
```yaml
netbox_docker_restore: false
restore_database_command: gunzip -c {{ backup_file }} | docker compose exec -T postgres sh -c 'psql -U $POSTGRES_USER $POSTGRES_DB' 
```
update netbox
```yaml
update: false
```
other
```yaml
git_repo: https://github.com/netbox-community/netbox-docker.git
``` 

## Examples
```yaml
  - name: install netbox docker container
    hosts: tags_docker

    roles:
      - role: netbox_docker
    become: true
```

The role will not install, backup, restore, or update the netbox instance unless the variables are set. 

Netbox is used as a source for Ansible and I do not set any of the Netbox install, backup, update, or restore variables.  

To install Netbox:  
`ansible-playbook example.yml -e "netbox_docker=true"`  