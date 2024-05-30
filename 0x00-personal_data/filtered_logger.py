#!/usr/bin/env python3
"""
Personal data
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Finction filter_datum

    Attributes:
        fields: list of fields to obfuscate
        redaction: string to obfuscate
        message: message to obfuscate
        separator: separator of fields

    Return:
        obfuscated message
    """
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(
        pattern,
        lambda match: match.group().split('=')[0] + '=' + redaction,
        message
    )
