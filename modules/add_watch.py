import subprocess
from modules.list_with_header import display_rules_with_headings
from modules.list_watch import list_audit_rules


def add_watch(path, permissions="rwxa", key="default_key"):
    """
    Add a watch to a file or directory using auditctl.
    
    Parameters:
        path (str): The file or directory to watch
        permissions (str): Permissions to watch: r, w, x, a
        key (str): A custom key to identify this rule in logs
    """
    try:
                
        cmd = ["auditctl", "-w", path, "-p", permissions, "-k", key]
        subprocess.run(["sudo"] + cmd, check=True)
        print("✅ File successfully added for auditing.")
        
        input("\nPress Enter to go back to main menu")
    except subprocess.CalledProcessError as e:
        print(f"❌  Failed to audit the file: {e}")
