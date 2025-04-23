import subprocess
import os


def check_file_path():
    while True:
        path=input("Enter the absolute file path to audit: ")
        if not os.path.exists(path):
            print(f"❌ The specified path '{path}' does not exist.")
            continue
        return path


def get_valid_permissions():
    valid_permissions = {"r", "w", "x", "a"}
    while True:
        permissions = input("Enter the type of events to audit for (r, w, x, a): ").strip().lower()
        # Remove duplicates while preserving order
        unique_permissions = "".join(sorted(set(permissions), key=permissions.index))

         # Check if the input contains only valid characters
        if not set(unique_permissions).issubset(valid_permissions):
            print(f"❌ Invalid input. Only {', '.join(valid_permissions)} are allowed.")
            continue

        # Check if the number of unique permissions is within the specified range
        if not (1 <= len(unique_permissions) <= 4):
            print(f"❌ Invalid audit format..")
            continue

        return unique_permissions


def add_watch(path, permissions="rwxa", key="default_key"):
    """
    Add a watch to a file or directory using auditctl.    
    Parameters:
        path (str): The file or directory to watch
        permissions (str): Permissions to watch: r, w, x, a
        key (str): A custom key to identify this rule in logs
    """
    try:

        if not os.path.exists(path):
            print(f"❌ The specified path '{path}' does not exist.")
            input("Press Enter to go back to main menu")
            return                    

        # Define the audit rule
        audit_rule = f"-w {path} -p {permissions} -k {key}\n"

        # Path to the audit rules file
        audit_rules_file = '/etc/audit/rules.d/custom.rules'

        # Append the rule to the audit file
        with open(audit_rules_file, 'a') as file:
            file.write(audit_rule)

        # Reload the audit rules to apply the new rule
        subprocess.run(["sudo", "augenrules"], check=True)
        
        cmd = ["auditctl", "-w", path, "-p", permissions, "-k", key]
        subprocess.run(["sudo"] + cmd, check=True)
        
        print(f"\n✅ '{path}' successfully added for auditing.")
        
        input("\nPress Enter to go back to main men")
    except subprocess.CalledProcessError as e:
        print(f"❌  Failed to audit the file: {e}")
