Role Name
=========

Installing a standard set of applications or packages onto machines.  

There is a list of packages to be installed via the `packages` variable and the zabbix agent is installed based on the `zabbix_repo` variable.  

TODO: zabbix_repo for different flavors of linux

Requirements
------------

None.

Role Variables
--------------

packages is a list of package names to be installed by the local package manager  
`packages`

zabbix_repo is the URL of the .deb file for zabbix agent to install  
`zabbix_repo`

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- name: standardized apps for all servers
  hosts: tags_ansible

  roles:
    - role: standard_apps
```


License
-------

MIT

Author Information
------------------

[Harry Purdue](https://github.com/harrypurdue)
