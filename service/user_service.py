import logging

from fastapi import HTTPException

from mysql.connector import Error

from config import get_db_connection

logger = logging.getLogger(__name__)


def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "select * from users"
    cursor.execute(query)
    users = cursor.fetchall()
    logger.debug(f"Users received from the database: {users}")
    all_users = {"user": users}
    return all_users

def add_user(request: dict):
    logging.debug(f"Add new user record: {request}")
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "insert into users (name, email) values (%s, %s)"
    try:
        cursor.execute(query, (request.name, request.email))
        connection.commit()
        user_id = cursor.lastrowid
    except Error as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=400, detail="Error inserting user")
    except Exception as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        cursor.close()
        connection.close()
    
    return {"id": user_id, "name": request.name, "email": request.email}

def get_user_by_id(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "select * from users where id = %s Limit 1;"
    try:
        cursor.execute(query, [id])
        users = cursor.fetchall()
        logger.debug(users)
    except Error as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=400, detail="Error inserting user")
    except Exception as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"user": users}

def update_user(request: dict, id: int):
    logger.debug(f"Request received to update: {request}")
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    if request.name != None and request.email != None:
        query = "update users set name = %s, email = %s where id = %s"
        params = (request.name, request.email, id)
    elif request.name != None:
        query = "update users set name = %s where id = %s"
        params = (request.name, id)
    elif request.email != None:
        query = "update users set email = %s where id = %s"
        params = (request.email, id)
    try:
        cursor.execute(query, params)
        connection.commit()
        user = get_user_by_id(id)
    except Error as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=400, detail="Error inserting user")
    except Exception as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        cursor.close()
        connection.close()
    logger.info(f"User is: {user}")
    return user

def delete_user(id: int):
    
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "delete from users where id = %s"
    param = [id]

    try:
        cursor.execute(query, param)
        row_count = cursor.rowcount
        connection.commit()
    except Error as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=400, detail="Error inserting user")
    except Exception as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        cursor.close()
        connection.close()
    if row_count != 0:
        return {"id": id}
    else:
        raise HTTPException(status_code=500, detail="user can not be deleted")
    


