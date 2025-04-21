from modules.add_watch import add_watch
from modules.install_auditd import check_and_install_auditctl
from modules.list_watch import list_audit_rules
from modules.remove_watch import remove_watch_by_index
from modules.clear_screen import clear_screen
from modules.view_logs import search_logs_by_key
from modules.ui import header
from modules.list_with_header import display_rules_with_headings

def welcome():
    while True:
        clear_screen()  # Clear the screen first
        header()  # Display the header
        print("1.🗂️  Add a file to audit   2.📌 List all audit files   3.🗑️  Remove an audit file   4.📑 View detailed audit log   0.⭕ Exit")
        print("-" * 130)
        print("")
        choice = input("Choose an option: ")
        print("-" * 130)
        
        if choice == "1":
            path = input("Enter full path of file to audit: ")
            perm = input("Enter the type of events to audit for (r, w, x, a): ")
            key = input("Enter a key name (e.g my_watch): ")
            add_watch(path, perm, key=key)

        elif choice == "2":
            rules = list_audit_rules()                          
            if not rules:
                print("⚠️  No audit rules found.")
                input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
            else:
                # Display available rules

                display_rules_with_headings(rules)
                # for index, rule in rules.items():
                #     print(f"{index}: {rule}")
            
                input("\nPress Enter to continue...")  # Wait for user input before returning to the menu
                

        elif choice == "3":
           
            rules = list_audit_rules()                          
            if not rules:
                print("⚠️  No audit rules found.")
                input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
            else:
                # Display available rules

                display_rules_with_headings(rules)
            # Prompt user for index with validation
            while True:
                index_input = input("\nEnter the rule numner to remove (press Enter to go back): ").strip()
                
                if not index_input:  # If user presses Enter without input
                    print("Returning to main menu.")
                    break  # Exit loop and return to main menu
                
                else:
                

                    try:
                        # Attempt to convert input to an integer index
                        index = int(index_input)

                        # Check if the index is valid
                        if index not in rules:
                            print(f"Invalid index. Please enter a valid rule number")
                            continue  # Ask for input again



                        # If index is valid, proceed to remove the rule
                        rule_to_remove = rules[index]
                        option=input(f"Are you sure you want to remove rule {index} {rule_to_remove} (y/n):")
                        if option.lower() == 'n':
                    
                            input("\nRule not removed. Press Enter to go back to main menu")  # Optional: prevent screen flash
                            break  # Exit the function or loop and return to the main menu
                        else:

                            remove_watch_by_index(index)
                            
                            print(f"Rule {index} removed successfully.")
                            input("\nPress Enter to go back to main menu")
                            break  # Exit loop after successful removal

                    except ValueError:
                        print("[✗] Invalid input. Please enter a valid number.")
            
        elif choice == "4":

            search_logs_by_key()

        elif choice == '0':
            exit(0)

if __name__ == "__main__":
    check_and_install_auditctl()
    welcome()
