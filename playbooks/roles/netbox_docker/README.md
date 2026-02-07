netbox_docker
=========

Install netbox docker container.

Requirements
------------

Docker must already be installed onto the target host.

Role Variables
--------------

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

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

None.

Example Playbook
----------------

By default the role will install netbox docker container
`ansible-playbook example.yml`

backup netbox sql database
`ansible-playbook example.yml -e "netbox_docker_backup=true"`

restore netbox sql database
`ansible-playbook example.yml -e "netbox_docker_restore=true"`

update netbox
`ansible-playbook example.yml -e "update=true"`

```yaml
  - name: install netbox docker container
    hosts: tags_docker

    roles:
      - role: netbox_docker
    become: true
```

License
-------

MIT

Author Information
------------------

[Harry Purdue](https://github.com/harrypurdue)

