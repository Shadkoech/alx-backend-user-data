#!/usr/bin/env python3
"""Module that uses regex to replace occurrences of certain
fields"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate/jumble specified fields in a log message
    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string to use for obfuscating the fields
        message: string representing the log line
        separator: str rep the character separating fields in log line
    Returns:
        String: Log message with specified fields obfuscated.
        return re.sub(fr'\b({"|".join(fields)})\b', redaction, message)
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Applies filter_datum method to filter values in incoming
        log records"""
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


if __name__ == '__main__':
    main()
