# Ansible Homelab
This is my ansible environment that I use to manage my homelab

In order to run playbooks, change into the playbook folder  

`cd playbooks`

## Environment
ansible vault is used to store api keys and other sensitive information
- ansible username
- ansible password
- ansible become password
- local user account usernames and passwords
- zabbix auth key

other values are stored in environment variables
- proxmox api password
- ansible vault password file
- proxmox user
- proxmox host
- proxmox url
- netbox api url
- netbox token
- zabbix host

## Documentation
For documentation related to specific playbooks see the [docs](docs/) folder  

Some roles have a readme associated with them in the roles folder. Over time, the documentation for these will be moved to the [docs](docs/) folder.