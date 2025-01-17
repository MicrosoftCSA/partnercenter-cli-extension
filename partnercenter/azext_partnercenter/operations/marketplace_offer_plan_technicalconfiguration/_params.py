# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan technical-configuration') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer id.')
        c.argument('plan_id', options_list=['--plan-id'], help='The Plan id.')

    with commands_loader.argument_context('partnercenter marketplace offer plan technical-configuration bundle add') as c:
        c.argument('cluster_extension_type', options_list=['--cluster-extension-type'], help='The Cluster Extension Type')
        c.argument('tenant_id', arg_group='CNAB Resource', options_list=['--tenant-id', '-t'], help='The Cluster Extension Type')
        c.argument('subscription_id', arg_group='CNAB Resource', options_list=['--subscription-id', '-s'], help='The Cluster Extension Type')
        c.argument('resource_group_name', arg_group='CNAB Resource', options_list=['--resource-group', '-g'], help='The Cluster Extension Type')
        c.argument('registry_name', arg_group='CNAB Resource', options_list=['--registry'], help='The name of the container registry.')
        c.argument('repository_name', arg_group='CNAB Resource', options_list=['--repository'], help='The name of the image repository.')
        c.argument('tag', arg_group='CNAB Resource', options_list=['--tag'], help='The name of the image repository.')
        c.argument('digest', arg_group='CNAB Resource', options_list=['--digest'], help='The digest of the bundle with a format of sha256:<hashcode>')
