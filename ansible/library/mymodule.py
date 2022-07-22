#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import subprocess


def run_module():

    module_args = dict(
        name=dict(type='str', required=True)
    )   

    module = AnsibleModule(
        argument_spec=module_args
    )


    result = dict(
        object = module.params['name'],
        stdout=''
    )
    # proc=subprocess.run('ss -tunlp | grep ' + module.params['name'], shell=True)
    # result['stdout']=proc.stdout

    

    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()