from modules.add_watch import add_watch
from modules.install_auditd import check_and_install_auditctl
from modules.list_watch import list_audit_rules
from modules.remove_watch import remove_function_data_input
from modules.clear_screen import clear_screen
from modules.view_logs import search_logs_by_key
from modules.ui import header
from modules.list_with_header import display_rules_with_headings
from modules.add_watch import get_valid_permissions, check_file_path

def welcome():
    while True:
        clear_screen()  # Clear the screen first
        header()  # Display the header
        print("1.🗂️  Add a file to audit   2.📌 List all audit Rules   3.🗑️  Remove an audit Rule   4.📑 View detailed audit log   0.⭕ Exit")
        print("-" * 130)
        print("")
        choice = input("Choose an option: ")
        print("-" * 130)
        
        if choice == "1":
                
            try:   
                    
                path = check_file_path() #Function to check whether path exist                    
                perm = get_valid_permissions() #Function to check whether permission is valid    
                key = input("Enter a key name (e.g my_watch): ")
                add_watch(path, perm, key=key)
            except KeyboardInterrupt:
                
                input("\nOperation cancelled. Press enter to go back..")
                
                

        elif choice == "2":
            rules = list_audit_rules()                          
            if not rules:
                print("⚠️  No audit rules found.")
                input("\nPress Enter to go back to main menu.")  # Wait for user input before returning to the menu
            else:
                # Display available rules
                display_rules_with_headings(rules)            
                input("\nPress Enter to go back to main menu.")  # Wait for user input before returning to the menu
                

        elif choice == "3":

            remove_function_data_input()           
            
        elif choice == "4":

            search_logs_by_key()

        elif choice == '0':
            exit(0)

if __name__ == "__main__":
    
    welcome()
    check_and_install_auditctl()
