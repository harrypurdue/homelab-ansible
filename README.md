# ansible homelab
this is my ansible environment that I use to manage my homelab

in order to run playbooks, change into the playbook folder  

`cd playbooks`

## environment
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

## docs
for documentation related to specific playbooks see the [docs](docs/) folder  

for documentation related to my roles see the readme at the root of each role folder