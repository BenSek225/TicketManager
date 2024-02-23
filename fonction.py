import sqlite3
import random
import string
from datetime import datetime



# Connexion aux bases de données pour chaque type de ticket
conn_standard = sqlite3.connect('ticket_standard_database.db')
cursor_standard = conn_standard.cursor()

conn_vip = sqlite3.connect('ticket_vip_database.db')
cursor_vip = conn_vip.cursor()

conn_vvip = sqlite3.connect('ticket_vvip_database.db')
cursor_vvip = conn_vvip.cursor()



# Création de la table Tickets (si elle n'existe pas) pour chaque type de ticket
cursor_standard.execute('''
    CREATE TABLE IF NOT EXISTS Tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference_code TEXT,
        is_paid INTEGER,
        created_at TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        ticket_type TEXT DEFAULT 'Standard'
    )
''')
conn_standard.commit()

cursor_vip.execute('''
    CREATE TABLE IF NOT EXISTS Tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference_code TEXT,
        is_paid INTEGER,
        created_at TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        ticket_type TEXT DEFAULT 'VIP'
    )
''')
conn_vip.commit()

cursor_vvip.execute('''
    CREATE TABLE IF NOT EXISTS Tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference_code TEXT,
        is_paid INTEGER,
        created_at TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        ticket_type TEXT DEFAULT 'VVIP'
    )
''')
conn_vvip.commit()



def generate_reference_code():
    # Génère un code de référence aléatoire
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))




def create_ticket(conn, cursor):
    # Crée un nouveau ticket dans la base de données avec des informations personnelles du client
    reference_code = generate_reference_code()
    is_paid = 1  # 0 pour non payé, 1 pour payé
    created_at = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    first_name = input("Entrez le prénom du client : ")
    last_name = input("Entrez le nom du client : ")
    phone_number = input("Entrez le numéro de téléphone du client : ")

    cursor.execute('''
        INSERT INTO Tickets (reference_code, is_paid, created_at, first_name, last_name, phone_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (reference_code, is_paid, created_at, first_name, last_name, phone_number))

    conn.commit()
    print(f"Ticket créé avec succès. Référence : {reference_code}")




def check_ticket_existence(conn, cursor, reference_code):
    # Vérifie si un ticket avec le code de référence donné existe dans la base de données
    cursor.execute('SELECT * FROM Tickets WHERE reference_code = ?', (reference_code,))
    ticket = cursor.fetchone()

    if ticket:
        ticket_type = ticket[7]  # Le champ 'ticket_type' est à l'index 7 (zéro indexé)
        print(f"Le ticket de type {ticket_type} existe. Détails : {ticket}")
        return ticket_type, ticket
    else:
        print("Aucun ticket trouvé.")
        return None




def display_ticket_count(conn, cursor, ticket_type):
    # Affiche le nombre de tickets pour un type donné
    cursor.execute('SELECT COUNT(*) FROM Tickets')
    count = cursor.fetchone()[0]
    print(f"Nombre de tickets {ticket_type}: {count}")




def display_tickets_by_type(conn, cursor, ticket_type):
     # Affiche tous les tickets pour un type donné
    cursor.execute('SELECT * FROM Tickets WHERE ticket_type = ?', (ticket_type,))
    tickets = cursor.fetchall() # Récupère tous les résultats de la requête

    if not tickets:
        print(f"Aucun ticket {ticket_type} trouvé.")
    else:
        # Si des tickets sont trouvés, itère sur chaque ticket et affiche les détails
        for ticket in tickets:
            # Détermine le statut payé ('Oui' ou 'Non') en fonction de la valeur dans la colonne 'is_paid'
            paid_status = 'Oui' if ticket[2] else 'Non'
            # Affiche les détails du ticket formatés
            print(f"ID: {ticket[0]}, Référence: {ticket[1]}, Payé: {paid_status}, "
                  f"Créé le: {ticket[3]}, Prénom: {ticket[4]}, Nom: {ticket[5]}, Téléphone: {ticket[6]}")




def display_all_tickets(conn, cursor):
    # Affiche tous les tickets de toutes les bases de données
    try:
        cursor.execute("SELECT * FROM tickets")
        tickets = cursor.fetchall()
        
        if not tickets:
            print("Aucun ticket trouvé.")
        else:
            print("ID: Référence: Payé: Créé le: Prénom: Nom: Téléphone: Type:")
            for ticket in tickets:
                ticket_id, reference, paid, created_at, first_name, last_name, phone, ticket_type = ticket
                print(f"{ticket_id}, {reference}, {paid}, {created_at}, {first_name}, {last_name}, {phone}, {ticket_type}")
    except Exception as e:
        print(f"Erreur lors de l'affichage des tickets : {e}")

