Role Name
=========

Applying my standard configuration.

Requirements
------------

None.

Role Variables
--------------

None

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- name: standardized configurations for all servers
  hosts: tags_ansible

  roles:
    - role: standard_configs
```

License
-------

MIT

Author Information
------------------

[Harry Purdue](https://github.com/harrypurdue)
