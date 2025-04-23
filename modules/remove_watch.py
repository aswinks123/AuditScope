import subprocess
from modules.list_watch import list_audit_rules
from modules.list_with_header import display_rules_with_headings
from modules.clear_screen import clear_screen
from modules.ui import header
import os


def remove_function_data_input():     

    rules = list_audit_rules()                          
    if not rules:
        print("\n⚠️  No audit rules found.")
        input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
    else:
        # Display available rules
        display_rules_with_headings(rules)
    # Prompt user for index with validation
        while True:
            index_input = input("\nEnter the index number to remove (Press Enter to go back): ").strip()
            
            if not index_input:  # If user presses Enter without input
                print("Returning to main menu.")
                break  # Exit loop and return to main menu
            
            else:            

                try:
                    # Attempt to convert input to an integer index
                    index = int(index_input)

                    # Check if the index is valid
                    if index not in rules:
                        print(f"\n❌ Invalid index. Please enter a valid rule number")
                        continue  # Ask for input again

                    # If index is valid, proceed to remove the rule
                    rule_to_remove = rules[index]

                    while True:
                        option = input(f"\nAre you sure you want to remove rule  {index} '{rule_to_remove}' (y/n): ").strip().lower()
                        
                        if option == 'y':
                            remove_watch_by_index(index)
                            print(f"\n✅ Audit Rule {index} removed successfully.")
                            input("\nPress Enter to continue..")
                            rules = list_audit_rules()                          
                            if not rules:
                                clear_screen()
                                header()
                                print("\n⚠️  No audit rules found.")
                                input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
                                return
                            else:
                                # Display available rules
                                clear_screen()
                                header()
                                display_rules_with_headings(rules)


                            break  # Exit the loop after successful removal
                        elif option == 'n':
                            print("\n❌ Rule not removed.")
                            break  # Exit the loop without removing the rule
                        else:
                            print("\n⚠️ Invalid input. Please enter 'y' for yes or 'n' for no.")                                            

                except ValueError:
                    print(f"\n❌ Invalid index. Please enter a valid rule number")


def remove_watch_by_index(index):

    """
    Remove the watch rule by its index using -W (deletion syntax).
    
    Parameters:
        index (int): The index number of the rule to delete.
    """

    rules = list_audit_rules()
    
    if index in rules:
        rule_to_remove = rules[index]       
                    
        # Replace the first '-w' with '-W' for deletion
        rule_parts = rule_to_remove.strip().split()
        if '-w' in rule_parts:
            rule_parts[rule_parts.index('-w')] = '-W'
        else:
            print("Invalid rule format, missing '-w'")
            return

        cmd = ["sudo", "auditctl"] + rule_parts

        try:
            subprocess.run(cmd, check=True)

            # Now remove the rule from the configuration file as well
            audit_rules_file = '/etc/audit/rules.d/custom.rules'  # Update with correct path if needed
            if os.path.exists(audit_rules_file):
                with open(audit_rules_file, 'r') as file:
                    lines = file.readlines()
                 # Find the rule in the file and remove it
                with open(audit_rules_file, 'w') as file:
                    for line in lines:
                        if rule_to_remove.strip() not in line:
                            file.write(line)
                    # Optionally, reload audit rules
                subprocess.run(["sudo", "augenrules"], check=True)

       
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Failed to remove the rule: {e}")
    else:
        print("\n⚠️Invalid index number.")

    