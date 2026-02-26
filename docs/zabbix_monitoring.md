# Zabbix Monitoring
To configure Zabbix with the hosts from Netbox run the following playbook.

`./zabbix_monitoring.yml`  

Virtual machines in netbox which are tagged with `ansible` will be added to zabbix. The tags in Netbox will be copied to the host in Zabbix.

This playbook does not remove hosts.