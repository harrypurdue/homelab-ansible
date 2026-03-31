# Virtual Machine Lifecycle

## Create

Virtual machines are created using the following playbook:  

`vm_create.yml`  

This playbook will:
- Create the virtual machine in Netbox
- Create the virtual machine in Proxmox by cloning an existing template
- Start the VM
- Update the netbox configuration context for DNS records to include the hostname

This playbook can be ran without additional variables. The name of the virtual machine is generated automatically if not specified. The IP address is pulled from the IPAM in netbox.

The below variables can be passed to the playbook with -e to change values.

```yaml
---
vm_name: example-01
netbox_platform: ubuntu-25-10
prefix: "192.0.2.0/24"
nameservers:
  - 192.0.2.101
  - 192.0.2.102
searchdomains:
  - lab.example
netbox_tags:
  - ansible
  - dev
```

By default:
- ubuntu-24-04 is the operating system `platform` in netbox.
- ip address is assigned from the netbox IPAM based on the prefix.
- netbox_tags only contains ansible.
- nameservers are configured for the current dns servers.
- searchdomains is configured as the current domain name.
 
The bridge that is used in proxmox for the virtual machine network adapter is chosen based on the prefix.  

Variables containig ip address or other information are stored in the `ansible-vault`.  

Variables can be passed individually at the command line or by using a yml file.  
`vm_create.yml -e @new_vm.yml` or  
`vm_create.yml -e "vm_name=example-02"`  

Virtual machines are created from templates already created on the Proxmox host. The following options are configured:  
`cloud-init user`  
`cloud-init ssh public key`  
`cloud-init upgrade packages - yes`  

This playbook does not handle the following:
- Pushing DNS records to DNS servers
- [Zabbix monitoring](zabbix_monitoring.md)
- [Standard Configurations](standard_configurations.md)
 
After this playbook is ran, it is recommended to run the following playbooks:  
- dns_servers.yml
- zabbix_monitoring.yml
- standard_configurations.yml

## Destroy

Virtual machines deleted using the following playbook:  

`vm_destroy.yml`  

The name of the virtual machine must be defined.  

`./vm_destroy.yml -e "vm_name=test-01"`  

This playbook does not handle the following:
- Pushing (removing) DNS records to DNS servers

After this playbook is ran, it is recommended to run the following playbooks:  
- dns_servers.yml

## Creating Virtual Machine Template
Virtual machine templates are created using the cloud image from the distribution.  

The image file is downloaded onto the proxmox server and then the script `scripts/new_proxmox_vm_image.sh` is ran.  

The `new_proxmox_vm_image.sh` script accepts three arguments.
- full path to the image file
- vmid
- name of template (match platform in netbox)

After the creation of the template, the following needs to be configured.
- platform in netbox
- config contexts for platform in netbox
- ssh key for template in cloud-init

## References
[Proxmox Cloud Init](https://pve.proxmox.com/wiki/Cloud-Init_Support)  