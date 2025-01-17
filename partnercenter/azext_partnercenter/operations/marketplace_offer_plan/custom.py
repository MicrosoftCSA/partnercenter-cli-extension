# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def list_plan(client, offer_id):
    return client.list(offer_id)


def create_plan(client, offer_id, plan_id, friendly_name):
    result = client.create(offer_id, plan_id, friendly_name)
    return result


def update_plan(instance):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(client, offer_id, plan_id):
    return client.delete(offer_id, plan_id)


def get_plan(client, offer_id, plan_id):
    return client.get(offer_id, plan_id)
