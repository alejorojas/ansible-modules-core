#!/usr/bin/python
#
# Copyright (c) 2016 Matt Davis, <mdavis@ansible.com>
#                    Chris Houseknecht, <house@redhat.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'committer',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: azure_rm_securitygroup_facts

version_added: "2.1"

short_description: Get security group facts.

description:
    - Get facts for a specific security group or all security groups within a resource group.

options:
    name:
        description:
            - Only show results for a specific security group.
        required: false
        default: null
    resource_group:
        description:
            - Name of the resource group to use.
        required: true
    tags:
        description:
            - Limit results by providing a list of tags. Format tags as 'key' or 'key:value'.
        required: false
        default: null

extends_documentation_fragment:
    - azure

author:
    - "Chris Houseknecht (@chouseknecht)"
    - "Matt Davis (@nitzmahone)"

'''

EXAMPLES = '''
    - name: Get facts for one security group
      azure_rm_securitygroup_facts:
        resource_group: Testing
        name: secgroup001

    - name: Get facts for all security groups
      azure_rm_securitygroup_facts:
        resource_group: Testing

'''

RETURN = '''
azure_securitygroups:
    description: List containing security group dicts.
    returned: always
    type: list
    example: [{
        "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
        "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001",
        "location": "eastus2",
        "name": "secgroup001",
        "properties": {
            "defaultSecurityRules": [
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/AllowVnetInBound",
                    "name": "AllowVnetInBound",
                    "properties": {
                        "access": "Allow",
                        "description": "Allow inbound traffic from all VMs in VNET",
                        "destinationAddressPrefix": "VirtualNetwork",
                        "destinationPortRange": "*",
                        "direction": "Inbound",
                        "priority": 65000,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "VirtualNetwork",
                        "sourcePortRange": "*"
                    }
                },
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/AllowAzureLoadBalancerInBound",
                    "name": "AllowAzureLoadBalancerInBound",
                    "properties": {
                        "access": "Allow",
                        "description": "Allow inbound traffic from azure load balancer",
                        "destinationAddressPrefix": "*",
                        "destinationPortRange": "*",
                        "direction": "Inbound",
                        "priority": 65001,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "AzureLoadBalancer",
                        "sourcePortRange": "*"
                    }
                },
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/DenyAllInBound",
                    "name": "DenyAllInBound",
                    "properties": {
                        "access": "Deny",
                        "description": "Deny all inbound traffic",
                        "destinationAddressPrefix": "*",
                        "destinationPortRange": "*",
                        "direction": "Inbound",
                        "priority": 65500,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "*",
                        "sourcePortRange": "*"
                    }
                },
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/AllowVnetOutBound",
                    "name": "AllowVnetOutBound",
                    "properties": {
                        "access": "Allow",
                        "description": "Allow outbound traffic from all VMs to all VMs in VNET",
                        "destinationAddressPrefix": "VirtualNetwork",
                        "destinationPortRange": "*",
                        "direction": "Outbound",
                        "priority": 65000,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "VirtualNetwork",
                        "sourcePortRange": "*"
                    }
                },
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/AllowInternetOutBound",
                    "name": "AllowInternetOutBound",
                    "properties": {
                        "access": "Allow",
                        "description": "Allow outbound traffic from all VMs to Internet",
                        "destinationAddressPrefix": "Internet",
                        "destinationPortRange": "*",
                        "direction": "Outbound",
                        "priority": 65001,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "*",
                        "sourcePortRange": "*"
                    }
                },
                {
                    "etag": 'W/"d036f4d7-d977-429a-a8c6-879bc2523399"',
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/secgroup001/defaultSecurityRules/DenyAllOutBound",
                    "name": "DenyAllOutBound",
                    "properties": {
                        "access": "Deny",
                        "description": "Deny all outbound traffic",
                        "destinationAddressPrefix": "*",
                        "destinationPortRange": "*",
                        "direction": "Outbound",
                        "priority": 65500,
                        "protocol": "*",
                        "provisioningState": "Succeeded",
                        "sourceAddressPrefix": "*",
                        "sourcePortRange": "*"
                    }
                }
            ],
            "networkInterfaces": [
                {
                    "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkInterfaces/nic004"
                }
            ],
            "provisioningState": "Succeeded",
            "resourceGuid": "ebd00afa-5dc8-446f-810a-50dd6f671588",
            "securityRules": []
        },
        "tags": {},
        "type": "Microsoft.Network/networkSecurityGroups"
    }]

'''


from ansible.module_utils.basic import *
from ansible.module_utils.azure_rm_common import *

try:
    from msrestazure.azure_exceptions import CloudError
    from azure.common import AzureMissingResourceHttpError, AzureHttpError
except:
    # This is handled in azure_rm_common
    pass


AZURE_OBJECT_CLASS = 'NetworkSecurityGroup'


class AzureRMSecurityGroupFacts(AzureRMModuleBase):

    def __init__(self):

        self.module_arg_spec = dict(
            name=dict(type='str'),
            resource_group=dict(required=True, type='str'),
            tags=dict(type='list'),
        )

        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_securitygroups=[])
        )

        self.name = None
        self.resource_group = None
        self.tags = None

        super(AzureRMSecurityGroupFacts, self).__init__(self.module_arg_spec,
                                                        supports_tags=False,
                                                        facts_module=True)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if self.name is not None:
            self.results['ansible_facts']['azure_securitygroups'] = self.get_item()
        else:
            self.results['ansible_facts']['azure_securitygroups'] = self.list_items()

        return self.results

    def get_item(self):
        self.log('Get properties for {0}'.format(self.name))
        item = None
        result = []

        try:
            item = self.network_client.network_security_groups.get(self.resource_group, self.name)
        except CloudError:
            pass

        if item and self.has_tags(item.tags, self.tags):
            grp = self.serialize_obj(item, AZURE_OBJECT_CLASS)
            grp['name'] = item.name
            result = [grp]

        return result

    def list_items(self):
        self.log('List all items')
        try:
            response = self.network_client.network_security_groups.list(self.resource_group)
        except Exception as exc:
            self.fail("Error listing all items - {0}".format(str(exc)))

        results = []
        for item in response:
            if self.has_tags(item.tags, self.tags):
                grp = self.serialize_obj(item, AZURE_OBJECT_CLASS)
                grp['name'] = item.name
                results.append(grp)
        return results


def main():
    AzureRMSecurityGroupFacts()

if __name__ == '__main__':
    main()

