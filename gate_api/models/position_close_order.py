# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class PositionCloseOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'price': 'str',
        'is_liq': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'price': 'price',
        'is_liq': 'is_liq'
    }

    def __init__(self, id=None, price=None, is_liq=None, local_vars_configuration=None):  # noqa: E501
        """PositionCloseOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._price = None
        self._is_liq = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if price is not None:
            self.price = price
        if is_liq is not None:
            self.is_liq = is_liq

    @property
    def id(self):
        """Gets the id of this PositionCloseOrder.  # noqa: E501

        Close order ID  # noqa: E501

        :return: The id of this PositionCloseOrder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PositionCloseOrder.

        Close order ID  # noqa: E501

        :param id: The id of this PositionCloseOrder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def price(self):
        """Gets the price of this PositionCloseOrder.  # noqa: E501

        Close order price  # noqa: E501

        :return: The price of this PositionCloseOrder.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PositionCloseOrder.

        Close order price  # noqa: E501

        :param price: The price of this PositionCloseOrder.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def is_liq(self):
        """Gets the is_liq of this PositionCloseOrder.  # noqa: E501

        Is the close order from liquidation  # noqa: E501

        :return: The is_liq of this PositionCloseOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_liq

    @is_liq.setter
    def is_liq(self, is_liq):
        """Sets the is_liq of this PositionCloseOrder.

        Is the close order from liquidation  # noqa: E501

        :param is_liq: The is_liq of this PositionCloseOrder.  # noqa: E501
        :type: bool
        """

        self._is_liq = is_liq

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PositionCloseOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PositionCloseOrder):
            return True

        return self.to_dict() != other.to_dict()
