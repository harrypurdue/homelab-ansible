# Zabbix Monitoring
To configure Zabbix with the hosts from Netbox run the following playbook.

`./zabbix_monitoring.yml`  

Virtual machines in netbox which are tagged with `ansible` will be added to zabbix. The tags in Netbox will be copied to the host in Zabbix.  

Default configuration will add the hosts using their IP addresses using the Zabbix Agent and configure my standard templates.

This playbook does not remove hosts.

Requires `ZABBIX_HOST` environment variable.  
Requires `ansible_zabbix_auth_key` ansible variable.

## Vars
`zabbix_interfaces`  
A list of interfaces to be configured for the host in Zabbix. Built dynamically by the playbook for most hosts. See playbook for information on hosts excluded for dynamic creation. For hosts that are excluded, the variable need to be configured in Netbox.  

Default (Via playbook):
```json
{
    "zabbix_interfaces" : [
        "ip" : "{{hostvars[inventory_hostname].ansible_host}}"
        "main" : 1,
        "type" : "agent",
        "useip" : 1
    ]
}
```  

`zabbix_host_groups`  
List of groups to add the host to in Zabbix. Not used by default. Populated via Netbox.  

`zabbix_description`  
Description to apply to the host in Zabbix. Not used by default. Populated via Netbox.  

`zabbix_link_templates`  
List of templates to apply to the host in Zabbix. Populated via Netbox.  
Default:
```json
{
    "zabbix_link_templates": [
        "ICMP Ping",
        "Linux by Zabbix agent"
    ],
}
```  

`zabbix_monitored_by`  
Server that will monitor the host. Populated via Netbox.  

Default:  
```json
{
    "zabbix_monitored_by": "zabbix_server"
}
```  

`zabbix_tags`  
List of tags to apply to the host in Zabbix. These tags mirror the tags applied to the host in Netbox. The playbook generates the varaible dynamically based on the tags from Netbox.  


## References
[Zabbix Host Module](https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/zabbix_host_module.html)  