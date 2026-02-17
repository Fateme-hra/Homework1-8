from flask import render_template, request, redirect, url_for, Flask, flash

import dbdoctor
import dbpatient
import dbreception

app = Flask(__name__, template_folder='templates')
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/receptions', methods=['GET', 'POST'])
def manage_receptions():
    receptions = dbreception.select_receptions()
    if receptions is None:
        receptions = []
    return render_template('receptions.html', receptions=receptions)


@app.route('/reception/delete/<int:id>')
def delete_reception(id):
    result = dbreception.delete_reception(id)
    if result:
        flash('پذیرش با موفقیت حذف شد', 'success')
        return redirect(url_for('manage_receptions'))
    else:
        flash('خطایی رخ داده است', 'danger')
        return redirect(url_for('manage_receptions'))


@app.route('/reception/edit/<int:id>', methods=['GET', 'POST'])
def edit_reception(id):
    error = None
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        date = request.form['date']
        hour = request.form['hour']
        minute = request.form['minute']
        time = f'{hour}:{minute}:00'

        doctor = dbdoctor.search_doctor(doctor_id)
        patient = dbpatient.search_patient(patient_id)

        if not doctor_id or not patient_id or not date or not time:
            error = "همه فیلد ها را باید پر کنید"
        elif doctor is None:
            error = 'پزشکی با شناسه وارد شده وجود ندارد'
        elif patient is None:
            error = 'بیماری با شناسه وارد شده وجود ندارد'
        else:
            result = dbreception.update_reception(id, doctor_id, patient_id, date, time)
            if result:
                flash('اطلاعات پذیرش با موفقیت بروزرسانی شد', 'success')
                return redirect(url_for('manage_receptions'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_receptions'))

    reception = dbreception.search_reception(id)
    return render_template('edit_reception.html', reception=reception, error=error)


@app.route('/reception/add', methods=['GET', 'POST'])
def add_reception():
    error = None
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        date = request.form['date']
        hour = request.form['hour']
        minute = request.form['minute']
        time = f'{hour}:{minute}:00'

        doctor = dbdoctor.search_doctor(doctor_id)
        patient = dbpatient.search_patient(patient_id)

        if not doctor_id or not patient_id or not date or not time:
            error = "همه فیلد ها را باید پر کنید"
        elif doctor is None:
            error = 'پزشکی با شناسه وارد شده وجود ندارد'
        elif patient is None:
            error = 'بیماری با شناسه وارد شده وجود ندارد'
        else:
            result = dbreception.add_reception(doctor_id, patient_id, date, time)
            if result:
                flash('پذیرش جدید با موفقیت اضافه شد', 'success')
                return redirect(url_for('manage_receptions'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_receptions'))

    return render_template('add_reception.html', error=error)


@app.route('/patients', methods=['GET', 'POST'])
def manage_patients():
    patients = dbpatient.select_patients()
    if patients is None:
        patients = []
    return render_template('patients.html', patients=patients)


@app.route('/patient/delete/<int:id>')
def delete_patient(id):
    result = dbpatient.delete_patient(id)
    if result:
        flash('بیمار با موفقیت حذف شد', 'success')
        return redirect(url_for('manage_patients'))
    else:
        flash('خطایی رخ داده است', 'danger')
        return redirect(url_for('manage_patients'))


@app.route('/patient/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    error = None
    if request.method == 'POST':
        national_code = request.form['national_code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone_number = request.form['phone_number']

        if not national_code or not firstname or not lastname or not phone_number:
            error = "همه فیلد ها را باید پر کنید"
        else:
            result = dbpatient.update_patient(id, national_code, firstname, lastname, phone_number)
            if result:
                flash('اطلاعات بیمار با موفقیت بروزرسانی شد', 'success')
                return redirect(url_for('manage_patients'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_patients'))

    patient = dbpatient.search_patient(id)
    return render_template('edit_patient.html', patient=patient, error=error)


@app.route('/patient/add', methods=['GET', 'POST'])
def add_patient():
    error = None
    if request.method == 'POST':
        national_code = request.form['national_code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone_number = request.form['phone_number']

        if not national_code or not firstname or not lastname or not phone_number:
            error = "همه فیلد ها را باید پر کنید"
        else:
            result = dbpatient.add_patient(national_code, firstname, lastname, phone_number)
            if result:
                flash('بیمار جدید با موفقیت اضافه شد', 'success')
                return redirect(url_for('manage_patients'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_patients'))

    return render_template('add_patient.html', error=error)


@app.route('/doctors', methods=['GET', 'POST'])
def manage_doctors():
    doctors = dbdoctor.select_doctors()
    if doctors is None:
        doctors = []
    return render_template('doctors.html', doctors=doctors)


@app.route('/doctor/delete/<int:id>')
def delete_doctor(id):
    result = dbdoctor.delete_doctor(id)
    if result:
        flash('پزشک با موفقیت حذف شد', 'success')
        return redirect(url_for('manage_doctors'))
    else:
        flash('خطایی رخ داده است', 'danger')
        return redirect(url_for('manage_doctors'))


@app.route('/doctor/edit/<int:id>', methods=['GET', 'POST'])
def edit_doctor(id):
    error = None
    if request.method == 'POST':
        national_code = request.form['national_code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone_number = request.form['phone_number']
        specialization = request.form['specialization']

        if not national_code or not firstname or not lastname or not phone_number or not specialization:
            error = "همه فیلد ها را باید پر کنید"
        else:
            result = dbdoctor.update_doctor(id, national_code, firstname, lastname, phone_number, specialization)
            if result:
                flash('اطلاعات پزشک با موفقیت بروزرسانی شد', 'success')
                return redirect(url_for('manage_doctors'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_doctors'))

    doctor = dbdoctor.search_doctor(id)
    return render_template('edit_doctor.html', doctor=doctor, error=error)


@app.route('/doctor/add', methods=['GET', 'POST'])
def add_doctor():
    error = None
    if request.method == 'POST':
        national_code = request.form['national_code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone_number = request.form['phone_number']
        specialization = request.form['specialization']

        if not national_code or not firstname or not lastname or not phone_number or not specialization:
            error = "همه فیلد ها را باید پر کنید"
        else:
            result = dbdoctor.add_doctor(national_code, firstname, lastname, phone_number, specialization)
            if result:
                flash('پزشک جدید با موفقیت اضافه شد', 'success')
                return redirect(url_for('manage_doctors'))
            else:
                flash('خطایی رخ داده است', 'danger')
                return redirect(url_for('manage_doctors'))

    return render_template('add_doctor.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
