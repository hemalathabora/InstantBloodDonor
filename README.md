# Instant Blood Donor

## Live Demo

🔗 **Project Live Link:**
https://instantblooddonor.onrender.com/

---

## Overview

**Instant Blood Donor** is a Flask-based web application designed to help people quickly find blood donors during emergency situations. The platform allows volunteers to register as donors and enables users to search for available donors based on **blood group and location**.

The goal of this project is to reduce the time required to locate blood donors and promote awareness about the importance of blood donation.

---

## Features

### Donor Registration

Volunteers can register themselves as blood donors by providing details such as name, blood group, contact information, and location.

### Search Donors

Users can search for available donors by selecting:

* Required **blood group**
* **Location**

The system displays a list of donors who match the search criteria.

### Emergency Support

Patients or hospitals can quickly locate donors during emergencies.

### Blood Donation Awareness

The platform promotes awareness and encourages voluntary blood donation.

### Feedback System

Users can submit feedback about their experience using the system.

---

## Technologies Used

**Backend**

* Python
* Flask

**Frontend**

* HTML
* CSS
* Jinja2 Templates

**Database**

* SQLite

---

## Project Structure

```id="sxtq8e"
InstantBloodDonors
│
├── index.py
├── main.py
├── feedback.py
├── user_db.py
├── volunterDetails.py
│
├── database.db
├── feedback.db
├── volunteer.db
│
├── templates/
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## Installation

### Clone the Repository

```id="78i0xf"
git clone https://github.com/YOUR_USERNAME/InstantBloodDonors.git
cd InstantBloodDonors
```

### Install Dependencies

```id="suz88x"
pip install -r requirements.txt
```

### Run the Application

```id="a7p0r4"
python index.py
```

Open in browser:

```id="0jti5u"
http://127.0.0.1:5000
```

---

## Deployment

This project is deployed using **Render**.

Start command used for deployment:

```id="ofnsvy"
gunicorn index:app
```

---

## Future Enhancements

* Authentication system
* Location-based donor search
* SMS or email notifications
* Admin dashboard

---

## License

This project is developed for **educational purposes**.
