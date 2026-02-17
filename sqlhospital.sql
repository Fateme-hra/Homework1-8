--
-- Table structure for table `doctors`
--

CREATE TABLE doctors
(
    id             INT         NOT NULL PRIMARY KEY IDENTITY (1,1),
    national_code  VARCHAR(10) NOT NULL,
    firstname      VARCHAR(50) NOT NULL,
    lastname       VARCHAR(50) NOT NULL,
    phone          VARCHAR(11) NOT NULL,
    specialization VARCHAR(50) NOT NULL
);
GO

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE patients
(
    id            INT         NOT NULL PRIMARY KEY IDENTITY (1,1),
    national_code VARCHAR(10) NOT NULL,
    firstname     VARCHAR(50) NOT NULL,
    lastname      VARCHAR(50) NOT NULL,
    phone         VARCHAR(11) NOT NULL,
);
GO
-- --------------------------------------------------------

--
-- Table structure for table `receptions`
--

CREATE TABLE receptions
(
    id         INT  NOT NULL PRIMARY KEY IDENTITY (1,1),
    date       DATE NOT NULL,
    time       TIME NOT NULL,
    doctor_id  INT  NOT NULL,
    patient_id INT  NOT NULL
);
GO

-- اضافه کردن کلیدهای خارجی
ALTER TABLE receptions
    ADD CONSTRAINT FK_reception_doctor FOREIGN KEY (doctor_id) REFERENCES doctors (id)
        ON DELETE CASCADE
GO

ALTER TABLE receptions
    ADD CONSTRAINT FK_reception_patient FOREIGN KEY (patient_id) REFERENCES patients (id)
        ON DELETE CASCADE
GO

-- Procedures
--
-- Procedure: add_doctor
CREATE PROCEDURE add_doctor @in_national_code VARCHAR(10), @in_firstname VARCHAR(50), @in_lastname VARCHAR(50),
                            @in_phone VARCHAR(11), @in_specialization VARCHAR(50)
AS
BEGIN
    INSERT INTO doctors (national_code, firstname, lastname, phone, specialization)
    VALUES (@in_national_code, @in_firstname, @in_lastname, @in_phone, @in_specialization);
END;
GO

-- Procedure: select_doctors
CREATE PROCEDURE select_doctors
AS
BEGIN
    SELECT * FROM doctors;
END;
GO

-- Procedure: delete_doctor
CREATE PROCEDURE delete_doctor @in_doctor_id INT
AS
BEGIN
    DELETE
    FROM doctors
    WHERE id = @in_doctor_id;
END;
GO

-- Procedure: update_doctor
CREATE PROCEDURE update_doctor @in_doctor_id INT,
                               @in_national_code VARCHAR(10), @in_firstname VARCHAR(50), @in_lastname VARCHAR(50),
                               @in_phone VARCHAR(11), @in_specialization VARCHAR(50)
AS
BEGIN
    UPDATE doctors
    SET national_code  = @in_national_code,
        firstname      = @in_firstname,
        lastname       = @in_lastname,
        phone          = @in_phone,
        specialization = @in_specialization
    WHERE id = @in_doctor_id;
END;
GO

-- Procedure: search_doctor
CREATE PROCEDURE search_doctor @in_doctor_id INT
AS
BEGIN
    SELECT *
    FROM doctors
    WHERE id = @in_doctor_id;
END;
GO

-- Procedure: add_patient
CREATE PROCEDURE add_patient @in_national_code VARCHAR(10), @in_firstname VARCHAR(50), @in_lastname VARCHAR(50),
                             @in_phone VARCHAR(11)
AS
BEGIN
    INSERT INTO patients (national_code, firstname, lastname, phone)
    VALUES (@in_national_code, @in_firstname, @in_lastname, @in_phone);
END;
GO

-- Procedure: select_patients
CREATE PROCEDURE select_patients
AS
BEGIN
    SELECT * FROM patients;
END;
GO

-- Procedure: delete_patient
CREATE PROCEDURE delete_patient @in_patient_id INT
AS
BEGIN
    DELETE
    FROM patients
    WHERE id = @in_patient_id;
END;
GO

-- Procedure: search_patient
CREATE PROCEDURE search_patient @in_patient_id INT
AS
BEGIN
    SELECT *
    FROM patients
    WHERE id = @in_patient_id;
END;
GO

-- Procedure: update_patient
CREATE PROCEDURE update_patient @in_patient_id INT,
                                @in_national_code VARCHAR(10), @in_firstname VARCHAR(50), @in_lastname VARCHAR(50),
                                @in_phone VARCHAR(11)
AS
BEGIN
    UPDATE patients
    SET national_code = @in_national_code,
        firstname     = @in_firstname,
        lastname      = @in_lastname,
        phone         = @in_phone
    WHERE id = @in_patient_id;
END;
GO

-- Procedure: add_reception
CREATE PROCEDURE add_reception @in_doctor_id INT,
                               @in_patient_id INT,
                               @in_date DATE,
                               @in_time TIME
AS
BEGIN
    INSERT INTO receptions (patient_id, doctor_id, date, time)
    VALUES (@in_patient_id, @in_doctor_id, @in_date, @in_time);
END;
GO

-- Procedure: delete_reception
CREATE PROCEDURE delete_reception @in_reception_id INT
AS
BEGIN
    DELETE
    FROM receptions
    WHERE id = @in_reception_id;
END;
GO

-- Procedure: select_receptions
CREATE PROCEDURE select_receptions
AS
BEGIN
    SELECT *
    FROM receptions;
END;
GO

-- Procedure: update_reception
CREATE PROCEDURE update_reception @in_reception_id INT,
                                  @in_doctor_id INT,
                                  @in_patient_id INT,
                                  @in_date DATE,
                                  @in_time TIME
AS
BEGIN
    UPDATE receptions
    SET doctor_id  = @in_doctor_id,
        patient_id = @in_patient_id,
        date       = @in_date,
        time       = @in_time
    WHERE id = @in_reception_id;
END;
GO

-- Procedure: search_reception
CREATE PROCEDURE search_reception @in_reception_id INT
AS
BEGIN
    SELECT *
    FROM receptions
    WHERE id = @in_reception_id;
END;
GO
