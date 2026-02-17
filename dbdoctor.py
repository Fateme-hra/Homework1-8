import pyodbc

from db import get_db_connection


def select_doctors():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC select_doctors')
        results = cursor.fetchall()
        return results
    except pyodbc.Error:
        return None


def add_doctor(national_id, firstname, lastname, phone, specialization):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC add_doctor ?, ?, ?, ?, ?', [national_id, firstname, lastname, phone, specialization])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def update_doctor(doctor_id, national_id, firstname, lastname, phone, specialization):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC update_doctor ?, ?, ?, ?, ?, ?',
                       [doctor_id, national_id, firstname, lastname, phone, specialization])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def delete_doctor(doctor_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC delete_doctor ?', [doctor_id])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def search_doctor(doctor_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC search_doctor ?', [doctor_id])
        result = cursor.fetchone()
        return result
    except pyodbc.Error:
        return None
