Role Name
=========

Perform system updates to servers using the target hosts package manager.

Snapshots with Proxmox are automatically taken and reverted if an error during the update process is encountered.

Verification tasks are ran after updates have been completed.

Currently only configured for Ubuntu.

Requirements
------------

Proxmox connectivity using the ansible community.proxmox.proxmox_snap module.
It is recommended to set the following environment variables:
PROXMOX_HOST  
PROXMOX_PASSWORD  
PROXMOX_USER  
PROXMOX_URL  

Recommended to have a seperate inventory source for proxmox and to specify the normal inventory source at the same time. See Example Playbook

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

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

License
-------

MIT

Author Information
------------------

[Harry Purdue](https://github.com/harrypurdue)
