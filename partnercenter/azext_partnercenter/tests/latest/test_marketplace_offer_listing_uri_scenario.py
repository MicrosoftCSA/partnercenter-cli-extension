# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest
from knack.log import get_logger

logger = get_logger(__name__)

class PartnerCenterMarketplaceOfferListingUriScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5 # delay each cmd by 5 sec, default
        self._setup_arg()
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_uri_listing(self):
        self.cmd('partnercenter marketplace offer listing uri add --offer-id {offer_id} --type {uri_type} --subtype {uri_sub_type} --display-text {uri_display_text} --uri {uri}',
                checks=[self.check('[0].type', '{uri_type}'),
                        self.check('[0].subtype', '{uri_sub_type}'),
                        self.check('[0].displayText', '{uri_display_text}'),
                        self.check('[0].uri', '{uri}')])

        self.cmd('partnercenter marketplace offer listing uri delete --offer-id {offer_id} --type {uri_type} --subtype {uri_sub_type} --display-text {uri_display_text} --uri {uri} --yes', delay=5)
        self.cmd('az partnercenter marketplace offer listing show --offer-id {offer_id}', checks=[self.check('uris', [])])

    def _setup_arg(self):
        self.kwargs.update({
            'uri': 'https://testuri',
            'uri_display_text': self.create_random_name('dt-', 10),
            'uri_type': 'PrivacyUri',
            'uri_sub_type': 'SubTypeUri'
        })
