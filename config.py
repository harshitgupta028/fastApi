import logging

from fastapi import HTTPException

from mysql.connector import connect, Error

logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        connection = connect(
            host = "localhost",
            user = "root",
            password = "qwsx##HG##123",
            database = "users_db"
        )
        return connection
    except Error as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")