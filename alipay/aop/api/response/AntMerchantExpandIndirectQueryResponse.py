#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.BankCardInfo import BankCardInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo


class AntMerchantExpandIndirectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectQueryResponse, self).__init__()
        self._address_info = None
        self._alias_name = None
        self._bankcard_info = None
        self._business_license = None
        self._business_license_type = None
        self._category_id = None
        self._contact_info = None
        self._external_id = None
        self._indirect_level = None
        self._logon_id = None
        self._mcc = None
        self._memo = None
        self._name = None
        self._org_pid = None
        self._pay_code_info = None
        self._service_phone = None
        self._source = None
        self._sub_merchant_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, list):
            self._address_info = list()
            for i in value:
                if isinstance(i, AddressInfo):
                    self._address_info.append(i)
                else:
                    self._address_info.append(AddressInfo.from_alipay_dict(i))
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def bankcard_info(self):
        return self._bankcard_info

    @bankcard_info.setter
    def bankcard_info(self, value):
        if isinstance(value, list):
            self._bankcard_info = list()
            for i in value:
                if isinstance(i, BankCardInfo):
                    self._bankcard_info.append(i)
                else:
                    self._bankcard_info.append(BankCardInfo.from_alipay_dict(i))
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def business_license_type(self):
        return self._business_license_type

    @business_license_type.setter
    def business_license_type(self, value):
        self._business_license_type = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, list):
            self._contact_info = list()
            for i in value:
                if isinstance(i, ContactInfo):
                    self._contact_info.append(i)
                else:
                    self._contact_info.append(ContactInfo.from_alipay_dict(i))
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def indirect_level(self):
        return self._indirect_level

    @indirect_level.setter
    def indirect_level(self, value):
        self._indirect_level = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        if isinstance(value, list):
            self._logon_id = list()
            for i in value:
                self._logon_id.append(i)
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
    @property
    def pay_code_info(self):
        return self._pay_code_info

    @pay_code_info.setter
    def pay_code_info(self, value):
        if isinstance(value, list):
            self._pay_code_info = list()
            for i in value:
                self._pay_code_info.append(i)
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectQueryResponse, self).parse_response_content(response_content)
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'alias_name' in response:
            self.alias_name = response['alias_name']
        if 'bankcard_info' in response:
            self.bankcard_info = response['bankcard_info']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'business_license_type' in response:
            self.business_license_type = response['business_license_type']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'contact_info' in response:
            self.contact_info = response['contact_info']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'indirect_level' in response:
            self.indirect_level = response['indirect_level']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'mcc' in response:
            self.mcc = response['mcc']
        if 'memo' in response:
            self.memo = response['memo']
        if 'name' in response:
            self.name = response['name']
        if 'org_pid' in response:
            self.org_pid = response['org_pid']
        if 'pay_code_info' in response:
            self.pay_code_info = response['pay_code_info']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'source' in response:
            self.source = response['source']
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
