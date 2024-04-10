#!/usr/bin/env python3
"""Module that uses regex to replace occurrences of certain
fields"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message
    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string to use for obfuscating the fields
        message: string representing the log line
        separator: str rep the character separating fields in log line
    Returns:
        String: Log message with specified fields obfuscated.
    """

    return re.sub(fr'\b({"|".join(fields)})\b', redaction, message)
