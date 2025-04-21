import subprocess

import subprocess
import re
import pwd

def uid_to_username(uid):
    try:
        return pwd.getpwuid(int(uid)).pw_name
    except KeyError:
        return f"UID:{uid}"

def search_logs_by_key():
    """
    View audit logs in a clean and user-friendly format based on key name.
    """
    key = input("\nEnter the key name to view logs: ").strip()
    if not key:
        print("[✗] Key name cannot be empty.")
        return
    limit_input = input("How many entries do you want to view (defaulut is all): ").strip()

    try:
        result = subprocess.run(
            ["sudo", "ausearch", "-k", key],
            capture_output=True,
            text=True,
            check=True
        )

        logs = result.stdout.strip().split("----")
        if not logs or logs == ['']:
            print(f"[!] No logs found for key '{key}'")
            return
        
        # Apply limit if provided
        if limit_input.lower() != "all":
            try:
                limit = int(limit_input)
                logs = logs[-limit:]
            except ValueError:
                print("[!] Invalid number entered. Showing all entries.")
        


        if limit_input:

            print(f"\n📜 Last {limit_input} logs for key: '{key}'\n" + "-" * 80)
        else:
            print(f"\n📜 All logs for key: '{key}'\n" + "-" * 80)

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
            print("🔐 UID:        ", uid_name )
            print("🔐 AUID:       ", auid_name )
            print("🧾 Session ID: ", ses.group(1) if ses else "N/A")
            print("🖥️  TTY:        ", tty.group(1) if tty else "N/A")
            print("-" * 80)

    except subprocess.CalledProcessError as e:
        print(f"[✗] Error while searching logs: {e}")
