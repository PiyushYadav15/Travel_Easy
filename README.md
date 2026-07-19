# 🌍 Travel Easy

**Travel Easy** is a Django-based Travel Management System that allows users to discover destinations, explore activities, and manage travel information through a clean and modern web interface. The project includes secure user authentication and complete CRUD functionality with soft delete and restore features.

---

## 📸 Screenshots
### Deployment
- Render 
https://travel-easy-ix12.onrender.com

---

# ✨ Features

### 🔐 Authentication
- User Registration
- User Login
- User Logout
- Update Profile
- Change Password
- Authentication Protected Pages

### 🌍 Destination Management
- Add Destination
- View Destination Details
- Update Destination
- Soft Delete Destination
- Restore Deleted Destination
- Destination History

### 🎯 Activity Management
- Add Activity
- View Activity Details
- Update Activity
- Soft Delete Activity
- Restore Deleted Activity
- Activity History

### 🖼 Image Upload
- Upload destination images
- Upload activity images

### 💻 User Interface
- Responsive Design
- Modern Card Layout
- Hover Effects
- Beautiful Forms
- Professional Navigation Bar
- Footer Section

---

# 🛠 Tech Stack

### Backend
- Python 3
- Django 5

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite3

### Libraries
- WhiteNoise
- Pillow

### Version Control
- Git
- GitHub


---

# 📂 Project Structure

```
Travel_Easy/
│
├── authentication/
├── destination/
├── activity/
├── media/
├── static/
├── templates/
├── myproject/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/PiyushYadav15/Travel_Easy.git
```

Move into project

```bash
cd Travel_Easy
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Run Server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

---

# 📁 Main Modules

## Authentication

- Register
- Login
- Logout
- Update Profile
- Change Password

---

## Destination Module

- Create Destination
- View Destination
- Update Destination
- Delete Destination
- Restore Destination

---

## Activity Module

- Create Activity
- View Activity
- Update Activity
- Delete Activity
- Restore Activity

---

# 🗃 Database Models

### Destination

- Name
- Location
- Type
- Description
- Rating
- Image
- is_deleted

### Activity

- Name
- Description
- Image
- is_deleted

### User

- Username
- Email
- Password

---

# 🚀 Future Improvements

- Search Destinations
- Search Activities
- Wishlist
- Travel Packages
- Hotel Booking
- Flight Booking
- Google Maps Integration
- Reviews & Ratings
- Online Payment
- Email Notifications
- Admin Dashboard
- REST API
- JWT Authentication
- AI Travel Recommendation System

---

# 📦 Requirements

```text
Django
Pillow
whitenoise
gunicorn
```

---

# 👨‍💻 Author

**Piyush Yadav**

📧 Email: piyushyadav2915@gemail.com

GitHub:
https://github.com/PiyushYadav15


---

# ⭐ Support

If you like this project, don't forget to ⭐ star this repository.

---

## 📜 License

This project is developed for educational and learning purposes.
