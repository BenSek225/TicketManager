import sqlite3
import random
import string
from datetime import datetime
from fonction import *



def main():
    while True:
        # Afficher le menu principal
        print("\n1. Créer un nouveau ticket (Standard)")
        print("2. Créer un nouveau ticket (VIP)")
        print("3. Créer un nouveau ticket (VVIP)")
        print("4. Vérifier l'existence d'un numéro de ticket")
        print("5. Afficher le nombre de tickets par type")
        print("6. Afficher tous les tickets d'un type")
        print("7. Afficher le nombre de tickets total")
        print("8. Afficher tous les tickets")
        # print("9. Marquer un ticket comme payé")
        print("9. Quitter")

        # Obtenir le choix de l'utilisateur
        choice = input("Choisissez une option (1/2/3/4/5/6/7/8/9): ")



        if choice in ['1', '2', '3']:
            # Créer un nouveau ticket en fonction du type sélectionné
            if choice == '1':
                create_ticket(conn_standard, cursor_standard)
            elif choice == '2':
                create_ticket(conn_vip, cursor_vip)
            elif choice == '3':
                create_ticket(conn_vvip, cursor_vvip)


                
        elif choice == '4':
            # Vérifier l'existence d'un numéro de ticket dans chaque base de données
            reference_code = input("Entrez le numéro de ticket à vérifier : ")
            check_ticket_existence(conn_standard, cursor_standard, reference_code)
            check_ticket_existence(conn_vip, cursor_vip, reference_code)
            check_ticket_existence(conn_vvip, cursor_vvip, reference_code)


            
        elif choice == '5':
            # Afficher le nombre de tickets pour un type donné
            ticket_type = input("Entrez le type de ticket (Standard/VIP/VVIP) : ")
            if ticket_type.lower() == 'standard':
                display_ticket_count(conn_standard, cursor_standard, "Standard")
            elif ticket_type.lower() == 'vip':
                display_ticket_count(conn_vip, cursor_vip, "VIP")
            elif ticket_type.lower() == 'vvip':
                display_ticket_count(conn_vvip, cursor_vvip, "VVIP")
            else:
                print("Type de ticket invalide. Veuillez entrer Standard, VIP ou VVIP.")



        elif choice == '6':
            # Afficher tous les tickets pour un type donné
            ticket_type = input("Entrez le type de ticket (Standard/VIP/VVIP) : ")
    
            if ticket_type.lower() == 'standard':
                display_tickets_by_type(conn_standard, cursor_standard, ticket_type)
            elif ticket_type.lower() == 'vip':
                display_tickets_by_type(conn_vip, cursor_vip, ticket_type)
            elif ticket_type.lower() == 'vvip':
                display_tickets_by_type(conn_vvip, cursor_vvip, ticket_type)
            else:
                print("Type de ticket invalide. Veuillez entrer Standard, VIP ou VVIP.")



        elif choice == '7':
            # Afficher le nombre total de tickets dans chaque base de données
            display_ticket_count(conn_standard, cursor_standard, "total")
            display_ticket_count(conn_vip, cursor_vip, "total")
            display_ticket_count(conn_vvip, cursor_vvip, "total")



        elif choice == '8':
            # Afficher tous les tickets de chaque base de données
            display_all_tickets(conn_standard, cursor_standard)
            display_all_tickets(conn_vip, cursor_vip)
            display_all_tickets(conn_vvip, cursor_vvip)


   
        elif choice == '9':
            # Quitter le programme
            break
        
        else:
            print("Option invalide. Veuillez entrer un nombre entre 1 et 9.")



    # Fermer les connexions à la base de données lorsque le programme se termine
    conn_standard.close()
    conn_vip.close()
    conn_vvip.close()



if __name__ == "__main__":
    main()
