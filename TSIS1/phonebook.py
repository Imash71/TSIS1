from connect import connect
conn = connect()
cur = conn.cursor()
# ---------------- ADD CONTACT ----------------
def add_contact():
   name = input("Name: ")
   email = input("Email: ")
   phone = input("Phone: ")
   cur.execute("""
       INSERT INTO contacts(name, email)
       VALUES(%s, %s)
       RETURNING id
   """, (name, email))
   contact_id = cur.fetchone()[0]
   cur.execute("""
       INSERT INTO phones(contact_id, phone, type)
       VALUES(%s, %s, %s)
   """, (contact_id, phone, "mobile"))
   conn.commit()
   print("Contact added!")
# ---------------- SHOW ALL ----------------
def show_contacts():
   cur.execute("""
       SELECT c.name, c.email, p.phone
       FROM contacts c
       LEFT JOIN phones p ON c.id = p.contact_id
   """)
   rows = cur.fetchall()
   for r in rows:
       print(r)
# ---------------- SEARCH BY EMAIL ----------------
def search_email():
   email = input("Enter email keyword: ")
   cur.execute("""
       SELECT c.name, c.email, p.phone
       FROM contacts c
       LEFT JOIN phones p ON c.id = p.contact_id
       WHERE c.email ILIKE %s
   """, (f"%{email}%",))
   rows = cur.fetchall()
   if not rows:
       print("No results")
   else:
       for r in rows:
           print(r)
# ---------------- MENU ----------------
while True:
   print("\n1 Add contact")
   print("2 Show contacts")
   print("3 Search by email")
   print("4 Exit")
   choice = input(">> ")
   if choice == "1":
       add_contact()
   elif choice == "2":
       show_contacts()
   elif choice == "3":
       search_email()
   elif choice == "4":
       break