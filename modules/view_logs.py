import subprocess
import re
import pwd
from modules.list_with_header import display_rules_with_headings
from modules.list_watch import list_audit_rules
def uid_to_username(uid):
    try:
        return pwd.getpwuid(int(uid)).pw_name
    except KeyError:
        return f"UID:{uid}"

def search_logs_by_key():

    try:
  
        #View audit logs in a clean and user-friendly format based on key name.
    
        rules = list_audit_rules()                          
        if not rules:
            print("\n⚠️  No audit rules found.")
            input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
            return
        else:
            # Display available rules

            display_rules_with_headings(rules)       

            while True:
                key = input("\nEnter the key name to view logs: ").strip()
                if key:
                    break
                print("\n⚠️ Key name cannot be empty. Please try again.")
                key = input("\nEnter the key name to view logs: ").strip()
            

        limit_input = input("\nHow many latest entries do you want to view (default is all): ").strip()

   # try:
        result = subprocess.run(
            ["sudo", "ausearch", "-k", key],
            capture_output=True,
            text=True,
            check=True
        )

        logs = result.stdout.strip().split("----")
        logs = [log.strip() for log in logs if log.strip()]

        # Filter logs to include only those with the exact key
        exact_logs = []
        for log in logs:
            key_match = re.search(r'key="([^"]+)"', log)
            if key_match and key_match.group(1) == key:
                exact_logs.append(log)

        if not exact_logs:
            print(f"\n ❌ No logs found for key '{key}'")
            input("\nPress Enter to return to menu...")
            return

        if limit_input.lower() != "all" and limit_input != "":
            try:
                limit = int(limit_input)
                exact_logs = exact_logs[-limit:]
            except ValueError:
                print("\n⚠️ Invalid number entered. Showing all entries.")

        print(f"\n📜 Displaying logs for key: '{key}'\n" + "-" * 130)
        for log in exact_logs:
            time = re.search(r'time->(.*)', log)
            comm = re.search(r'comm="([^"]+)"', log)
            exe = re.search(r'exe="([^"]+)"', log)
            file = re.search(r'name="([^"]+)"', log)
            op = re.search(r'op=([a-z_]+)', log)

            #uid = re.search(r'uid=(\d+)', log)
            #auid = re.search(r'auid=(\d+)', log)

            uid = re.search(r'\buid=(\d+)', log)
            auid = re.search(r'\bauid=(\d+)', log)
            ses = re.search(r'ses=(\d+)', log)
            tty = re.search(r'tty=([^\s]+)', log)
            key_match = re.search(r'key="([^"]+)"', log)

            uid_name = uid_to_username(uid.group(1)) if uid else "N/A"
            auid_name = uid_to_username(auid.group(1)) if auid else "N/A"
        

            print("🕒 Time:        ", time.group(1) if time else "N/A")
            print("⚙️  Operation:   ", op.group(1) if op else "N/A")
            print("📂 File:        ", file.group(1) if file else "N/A")
            print("👤 Command:     ", comm.group(1) if comm else "N/A")
            print("📍 Executable:  ", exe.group(1) if exe else "N/A")
            print("🔐 UID:         ", uid_name)
            print("🔐 AUID:        ", auid_name)
            print("🧾 Session ID:  ", ses.group(1) if ses else "N/A")
            print("🖥️  TTY:         ", tty.group(1) if tty else "N/A")
            print("🔑 Key Name:    ", key_match.group(1) if key_match else "N/A")
            print("-" * 130)
    except KeyboardInterrupt:
        print("\nOperation interrupted..")

    except subprocess.CalledProcessError as e:
        print(f"\n ❌ Error while searching logs or no logs found with the provided key")
    input("\nPress Enter to return to menu...")

    
