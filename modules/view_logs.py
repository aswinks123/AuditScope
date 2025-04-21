import subprocess

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
    """
    View audit logs in a clean and user-friendly format based on key name.
    """
    rules = list_audit_rules()                          
    if not rules:
        print("⚠️  No audit rules found.")
        input("\nPress Enter to go back to main menu")  # Wait for user input before returning to the menu
        return
    else:
        # Display available rules

        display_rules_with_headings(rules)
        key = input("\nEnter the key name to view logs: ").strip()
        if not key:
            print("[✗] Key name cannot be empty.")
            input("\nPress Enter to return to menu...")
            return

    limit_input = input("How many entries do you want to view (default is all): ").strip()

    try:
        result = subprocess.run(
            ["sudo", "ausearch", "-k", key],
            capture_output=True,
            text=True,
            check=True
        )

        logs = result.stdout.strip().split("----")
        logs = [log.strip() for log in logs if log.strip()]
        if not logs:
            print(f"[!] No logs found for key '{key}'")
            input("\nPress Enter to return to menu...")
            return

        if limit_input.lower() != "all" and limit_input != "":
            try:
                limit = int(limit_input)
                logs = logs[-limit:]
            except ValueError:
                print("[!] Invalid number entered. Showing all entries.")

        print(f"\n📜 Displaying logs for key: '{key}'\n" + "-" * 80)
        for log in logs:
            time = re.search(r'time->(.*)', log)
            comm = re.search(r'comm="([^"]+)"', log)
            exe = re.search(r'exe="([^"]+)"', log)
            file = re.search(r'name="([^"]+)"', log)
            op = re.search(r'op=([a-z_]+)', log)
            uid = re.search(r'uid=(\d+)', log)
            auid = re.search(r'auid=(\d+)', log)
            ses = re.search(r'ses=(\d+)', log)
            tty = re.search(r'tty=([^\s]+)', log)

            uid_name = uid_to_username(uid.group(1)) if uid else "N/A"
            auid_name = uid_to_username(auid.group(1)) if auid else "N/A"

            print("🕒 Time:       ", time.group(1) if time else "N/A")
            print("⚙️  Operation:  ", op.group(1) if op else "N/A")
            print("📂 File:       ", file.group(1) if file else "N/A")
            print("👤 Command:    ", comm.group(1) if comm else "N/A")
            print("📍 Executable: ", exe.group(1) if exe else "N/A")
            print("🔐 UID:        ", uid_name)
            print("🔐 AUID:       ", auid_name)
            print("🧾 Session ID: ", ses.group(1) if ses else "N/A")
            print("🖥️  TTY:        ", tty.group(1) if tty else "N/A")
            print("-" * 80)

    except subprocess.CalledProcessError as e:
        print(f"[✗] Error while searching logs: {e}")
    input("\nPress Enter to return to menu...")
