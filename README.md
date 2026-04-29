# 📞 TSIS 1: PhoneBook — Extended Contact Management
## 📌 Project Description
This project is a console-based PhoneBook system built using Python and PostgreSQL.  
It allows managing contacts with extended features such as multiple phone numbers, groups, email, and birthday.
---
## ⚙️ Technologies Used
- Python
- PostgreSQL
- psycopg2
- SQL (PL/pgSQL)
---
## 🗄️ Database Structure
### Tables:
- **contacts**
 - id
 - name
 - email
 - birthday
 - group_id
- **phones**
 - id
 - contact_id
 - phone
 - type (mobile, home, work)
- **groups**
 - id
 - name
---
## 🚀 Features
- Add new contacts
- Store multiple phone numbers per contact
- Assign contacts to groups
- Search contacts by email
- Display all contacts
- PostgreSQL database integration
- Console-based interface
---
## 🔍 Search Feature
Supports searching contacts by email using SQL LIKE / ILIKE operator.
---
## 📂 Project Structure
TSIS1/
├── phonebook.py
├── connect.py
├── config.py
├── schema.sql
├── test.py
---
## ▶️ How to Run
1. Install dependencies:
```bash
pip install psycopg2-binary
