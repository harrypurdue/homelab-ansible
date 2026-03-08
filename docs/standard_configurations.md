# Standard Configurations
To apply the standard configurations to servers run the following playbook.  

`./standard_configurations.yml`  

This will apply the standard configuration that I have defined and install any packages that are deemed to be standard. 

Standard configuration includes:  
- User accounts
- Timezone
- SSH public keys and key only login

Standard applications includes:
- Zabbix agent
- dnsutils

## Roles
Standard configurations are applied with my `standard_configs` role.  

Standard applications are installed with my `standard_apps` role.  
The list of packages to be installed is defined using the `packages` variable and the zabbix agent is installed based on the `zabbix_repo` variable.  

`packages` is a list of package names to be installed by the local package manager  

`zabbix_repo` is the URL of the .deb file for zabbix agent to install  

### Examples

```yaml
---
- name: standardized apps for all servers
  hosts: tags_ansible

  roles:
    - role: standard_apps
```
