import pyodbc

from db import get_db_connection


def select_receptions():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC select_receptions')
        results = cursor.fetchall()
        return results
    except pyodbc.Error:
        return None


def add_reception(doctor_id, patient_id, date, time):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC add_reception ?, ?, ?, ?', [doctor_id, patient_id, date, time])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def update_reception(reception_id, doctor_id, patient_id, date, time):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC update_reception ?, ?, ?, ?, ?', [reception_id, doctor_id, patient_id, date, time])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def delete_reception(reception_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC delete_reception ?', [reception_id])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def search_reception(reception_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC search_reception ?', [reception_id])
        result = cursor.fetchone()
        return result
    except pyodbc.Error:
        return None
