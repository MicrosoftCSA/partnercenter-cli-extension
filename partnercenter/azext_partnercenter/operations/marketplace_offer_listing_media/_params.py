# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing media') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('type', options_list=['--type'], help='The type of the uri.')
        c.argument('file', options_list=['--file'], help='The type of the uri.')
