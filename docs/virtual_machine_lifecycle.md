# Virtual Machine Lifecycle

## Create

Virtual machines are created using the following playbook:  

`vm_create.yml`  

This playbook will:
- Create the virtual machine in Netbox
- Create the virtual machine in Proxmox by cloning an existing template
- Start the VM

This playbook requires the following variables:
```yaml
---
vm_name: example-01
clone: cloud-init-ubuntu-25-10
netbox_platform: ubuntu_25_10
ip_info:
  ip_address: "192.0.2.44/24"
  gateway: "192.0.2.254"
  nameservers:
    - 192.0.2.101
    - 192.0.2.102
  bridge: "vmbr2"
  searchdomains:
    - lab.example
netbox_tags:
  - ansible
  - dev
```

`clone` is the name of the template in proxmox  
`netbox_platform` is the name of the platform as defined in netbox  
`netbox_tags` are the tags to apply to the virtual machine in netbox  

Variables can be passed individually at the command line or by using a yml file.  
`vm_create.yml -e @new_vm.yml`

Virtual machines are created from templates already created on the Proxmox host. The following options are configured:  
`cloud-init user`  
`cloud-init ssh public key`  
`cloud-init upgrade packages - yes`  

This playbook does not handle the following:
- DNS records
- [Zabbix monitoring](zabbix_monitoring.md)
- [Standard Configurations](standard_configurations.md)
 

## Destroy

Virtual machines deleted using the following playbook:  

`vm_destroy.yml`  

The name of the virtual machine must be defined.  

`./vm_destroy.yml -e "vm_name=test-01"`  

This playbook does not handle the following:
- DNS records

