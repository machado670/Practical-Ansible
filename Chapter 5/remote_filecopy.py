#!/usr/bin/env python 
# 

# Copyright: (c) 2018, Jesse Keating <jesse.keating@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = ''' 
---
module: remote_filecopy
version_added: "2.15"
short_description: Copy a file on the remote host
description:
  - The remote_copy module copies a file on the remote host from a given source to a provided destination.
options:
  source:
    description:
      - Path to a file on the source file on the remote host
    required: True
  dest:
    description:
      - Path to the destination on the remote host for the copy
    required: True
author:
- Jesse Keating (@omgjlk)
''' 
EXAMPLES = '''
   # Example from Ansible Playbooks
   - name: backup a config file
     remote_copy:
       source: /etc/herp/derp.conf
       dest: /root/herp-derp.conf.bak
'''
RETURN = '''
source:
  description: source file used for the copy
  returned: success
  type: str
  sample: "/path/to/file.name"
dest:
  description: destination of the copy
  returned: success
  type: str
  sample: "/path/to/destination.file"
gid:
  description: group ID of destination target
  returned: success
  type: int
  sample: 502
group:
  description: group name of destination target
  returned: success
  type: str
  sample: "users"
uid:
  description: owner ID of destination target
  returned: success
  type: int
  sample: 502
owner:
  description: owner name of destination target
  returned: success
  type: str
  sample: "fred"
mode:
  description: permissions of the destination target
  returned: success
  type: int
  sample: 0644
size:
  description: size of destination target
  returned: success
  type: int
  sample: 20
state:
  description: state of destination target
  returned: success
  type: str
  sample: "file"
'''

import shutil 

def main(): 
    module = AnsibleModule( 
        argument_spec = dict( 
            source=dict(required=True, type='str'), 
            dest=dict(required=True, type='str') 
        ), 
    ) 
    shutil.copy(module.params['source'], 
                module.params['dest']) 
 
    module.exit_json(changed=True) 

from ansible.module_utils.basic import * 
if __name__ == '__main__': 
    main() 
