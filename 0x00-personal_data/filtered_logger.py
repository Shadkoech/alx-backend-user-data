#!/usr/bin/env python3
"""Module that uses regex to replace occurrences of certain
fields"""

import re
import os
import logging
import mysql.connector
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Gets configured logger object for logging user data
    Returns:
        Logger: Logger obj configured to log user data """

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Method obtaining database credentials from env variables
    Returns:
        Connector to MySQL database"""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    # Connect to the MySQL database
    connector = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return connector


def main():
    """Main function getting database connection using get_db()
    and retrieves all the rows from users table then displays
    them under a filtered format"""
    db = get_db()
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    # Retrieve the field names from the cursor's description
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    # Iterate over each row fetched by the cursor
    for row in cursor:
        # Create string representation of the row, \
        # concatenating field name and value pairs
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_names))
        # Log the formatted row using the logger
        logger.info(str_row.strip())

    # Close the cursor to release resources
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
