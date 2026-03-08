# Updates
Updates can be run on all machines in the environment or using tags.  
`tags_prod` or `tags_dev`  

A proxmox snapshot is taken before updates and if the update task fails, the virtual machine is reverted to the snapshot. Verification tasks are ran after updates are applied and before the snapshot is removed. If any of the verification tasks fails, then the snapshot is restored to its original state prior to updates.  

Updates are usually ran on the dev environment first and then production.  
`ansible-playbook updates.yml -t tags_dev`  
`ansible-playbook updates.yml -t tags_prod`  

## Role
Updates are performed using the `updates` role  

The role currently only supports debian based distributions.

Proxmox connectivity using the ansible community.proxmox.proxmox_snap module.
It is recommended to set the following environment variables:
PROXMOX_HOST  
PROXMOX_PASSWORD  
PROXMOX_USER  
PROXMOX_URL  

### Example
Copy the below into a file called `updates.yml` and run the playbook with  

`ansible-playbook updates.yml -l tags_dev`  

After updates to the dev evnrionment have completed, then run updates for the production environment.  

`ansible-playbook updates.yml -l tags_prod`  

```yaml
#!/usr/bin/env -S ansible-playbook -i inventory/netbox.yml -i inventory/proxmox.yml
---
- name: updates in dev
  hosts: tags_dev

  roles:
    - role: updates

- name: updates in prod
  hosts: tags_prod

  roles:
    - role: updates
```