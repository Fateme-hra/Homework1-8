# Hospital Management System

## Overview
A simple educational hospital management system built with Flask and SQL Server. This project demonstrates basic CRUD operations (Create, Read, Update, Delete) for managing doctor and patient information through a web-based interface.

Note: This is an incomplete, educational project created for a university database course and is not production-ready.

## Project Status
⚠️ Status: Incomplete - Educational Project

This project was created as a university course assignment focused on database operations and SQL fundamentals. It requires further development and improvements to be suitable for production use.

## Features
- View list of doctors and patients
- Add new doctor information
- Add new patient information
- Edit existing doctor records
- Edit existing patient records
- Delete doctor records
- Delete patient records
- Simple web-based user interface
- Direct database integration for data persistence

## Technologies Used
- Backend: Python (Flask web fram
- ework)
- Database: SQL Server
- Frontend: HTML/CSS
- Template Engine: Jinja2
- Database Operations: SQL queries

## Project Structure

Hospital/
├── app.py                 # Main Flask application
├── db.py                  # Database connection
├── dbdoctor.py           # Doctor database operations
├── dbpatient.py          # Patient database operations
├── dbreception.py        # Reception database operations
├── sqlhopital.sql        # Database schema/initialization
└── templates/            # HTML templates
    ├── index.html
    ├── doctor.html
    ├── patient.html
    └── ...

## How to Use

### Viewing Records
1. Navigate to the "Doctors" or "Patients" page
2. View all existing records in the database

### Adding New Records
1. Click the "Add Doctor" or "Add Patient" button
2. Fill in all required fields in the form
3. Click "Submit" or "Save" to store the information in the database

### Editing Records
1. Find the record you want to modify
2. Click the "Edit" button next to the record
3. Update the information
4. Click "Update" or "Save" to apply changes

### Deleting Records
1. Find the record you want to remove
2. Click the "Delete" button
3. Confirm the deletion when prompted

## Limitations & Known Issues

### Current Limitations:
- Incomplete Features: The project has several planned features that are not yet implemented
- No User Authentication: No login system or user accounts
- Limited Input Validation: Form inputs may not be properly validated
- No Error Handling: Some error scenarios are not handled gracefully
- No Database Transactions: Operations are not atomic or transactional
- Limited UI/UX: Simple interface, not optimized for user experience
- Educational Code Quality: Code is not optimized for production use
- No Search/Filter: Limited ability to search or filter records

### Known Issues:
- Database connection errors may crash the application
- No backup functionality
- No audit logs for changes
- Sessions are not managed properly


## Future Improvements & TODO

- [ ] Implement user authentication and login system
- [ ] Add comprehensive input validation and error handling
- [ ] Implement database transactions for data consistency
- [ ] Add search and filtering functionality for records
- [ ] Create API endpoints for data access
- [ ] Write unit and integration tests
- [ ] Improve user interface and user experience
- [ ] Add appointment scheduling functionality
- [ ] Implement role-based access control (receptionist, doctor, admin)
- [ ] Add data export functionality (PDF, Excel)
- [ ] Implement database logging and audit trails
- [ ] Add data validation rules and constraints
- [ ] Optimize database queries for better performance
- [ ] Create comprehensive documentation

## Troubleshooting

### Issue: "Connection to SQL Server failed"
Solution: 
- Verify SQL Server is running
- Check connection string in db.py
- Ensure database name and credentials are correct

### Issue: "Module 'Flask' not found"
Solution:
pip install Flask

### Issue: "Database tables not found"
Solution:
Run the sqlhopital.sql script to create tables
Verify you're connecting to the correct database





