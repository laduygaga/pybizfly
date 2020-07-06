from constants.services import (CLOUD_SERVER_DISK_TYPES, AVAILABILITY_ZONES, CLOUD_SERVER_SERVER_TYPES,
                                CLOUD_SERVER_OS_TYPES)
from utils.exceptions import ExcludeValueException, InvalidTypeException, BizFlyClientException, InvalidDictException


def validate_str_list(str_list: list) -> list:
    """
    Validate list with string instance items
    :param str_list:
    :return:
    """
    validate_list = []
    for item in str_list:
        try:
            item = str(item)
            validate_list.append(item)
        except ValueError:
            continue
    return validate_list


def validate_dict_list(dict_list: list) -> list:
    """
    Validate list with dict  instance items
    :param dict_list:
    :return:
    """
    validate_list = [] = list()
    for item in dict_list:
        if isinstance(item, dict):
            validate_list.append(item)
    return validate_list


def validate_firewall_rules() -> list:
    """
    pass
    :return:
    """


def validate_disk_type(disk_type, name_to_call: str = None):
    if disk_type not in CLOUD_SERVER_DISK_TYPES:
        if not name_to_call:
            name_to_call = 'disk_type'
        raise ExcludeValueException(name_to_call, CLOUD_SERVER_DISK_TYPES)


def validate_server_type(server_type):
    if server_type not in CLOUD_SERVER_SERVER_TYPES:
        raise ExcludeValueException('server_type', CLOUD_SERVER_SERVER_TYPES)


def validate_availability_zone(availability_zone):
    if availability_zone not in AVAILABILITY_ZONES:
        raise ExcludeValueException('availability_zone', AVAILABILITY_ZONES)


def validate_os_type(os_type):
    if os_type not in CLOUD_SERVER_OS_TYPES:
        raise ExcludeValueException('os_type', CLOUD_SERVER_OS_TYPES)


def validate_data_disks(data_disks):
    count = 0
    for data_disk in data_disks:
        try:
            if not isinstance(data_disk, dict):
                raise InvalidTypeException('data_disks[{}]'.format(count), dict)
            validate_disk_type(data_disk['type'])
            if not isinstance(data_disk['size'], int):
                raise InvalidTypeException('data_disks[{}][size]'.format(count), int)
            count += 1
        except KeyError:
            raise InvalidDictException('data_disks', ['type', 'size'])


def validate_firewall_bounds(bounds_rules, name_to_call: str = None):
    count = 0
    if not name_to_call:
        name_to_call = 'bound_rules'
    insisted = ['type', 'protocol', 'port_range', 'cidr']
    for bound in bounds_rules:
        try:
            if not isinstance(bound, dict):
                raise InvalidTypeException('{}[{}]'.format(name_to_call, count), dict)
            for key in insisted:
                if key not in bound.keys():
                    raise KeyError()
        except KeyError:
            raise InvalidDictException(name_to_call, insisted)
