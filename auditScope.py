from modules.add_watch import add_watch
from modules.install_auditd import check_and_install_auditctl
from modules.list_watch import list_audit_rules
from modules.remove_watch import remove_watch_by_index
from modules.list_watch import list_audit_rules
from modules.clear_screen import clear_screen
from modules.ui import header



def welcome():
    while True:
        header()
        print("1. Add Watch 2. List all Watches 3. Remove Watch 0. Exit")

     

        
        choice = input("Choose an option: ")
        if choice == "1":
            clear_screen()
            header()
            path = input("Enter file/service path to watch: ")
            perm = input("Enter the type of events to watch for (r, w, x, a): ")
            key = input("Enter a key name (e.g., my_watch): ")
            add_watch(path,perm, key=key)
        if choice == "2":
             clear_screen()
             header()
             rules = list_audit_rules()
             if rules:
                for index, rule in rules.items():
                    print(f"{index}: {rule}")

        if choice == "3":
            clear_screen()
            header()
            rules = list_audit_rules()
            if rules:
                for index, rule in rules.items():
                    print(f"{index}: {rule}")
            list_audit_rules()
            index=int(input("\nEnter the index number to remove: "))
            remove_watch_by_index(index)

        if choice == '0':
            exit(0)



if __name__ == "__main__":
  
  check_and_install_auditctl()
  welcome()
