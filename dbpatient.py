import pyodbc

from db import get_db_connection


def select_patients():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC select_patients')
        results = cursor.fetchall()
        return results
    except pyodbc.Error:
        return None


def add_patient(national_id, firstname, lastname, phone):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC add_patient ?, ?, ?, ?', [national_id, firstname, lastname, phone])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def update_patient(patient_id, national_id, firstname, lastname, phone):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC update_patient ?, ?, ?, ?, ?', [patient_id, national_id, firstname, lastname, phone])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def delete_patient(patient_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC delete_patient ?', [patient_id])
        cursor.commit()
        return True
    except pyodbc.Error:
        return False


def search_patient(patient_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'EXEC search_patient ?', [patient_id])
        result = cursor.fetchone()
        return result
    except pyodbc.Error:
        return None
