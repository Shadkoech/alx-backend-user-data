#!/usr/bin/env python3
"""Module that uses regex to replace occurrences of certain
fields"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message
    """
    return re.sub(fr'\b({"|".join(fields)})\b', redaction, message)
