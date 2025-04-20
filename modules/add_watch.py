import subprocess
from modules.clear_screen import clear_screen

def add_watch(path, permissions="rwxa", key="default_key"):
    """
    Add a watch to a file or directory using auditctl.
    
    Parameters:
        path (str): The file or directory to watch
        permissions (str): Permissions to watch: r, w, x, a
        key (str): A custom key to identify this rule in logs
    """
    try:
        clear_screen()
        print(f"Adding watch: {path} with permissions={permissions}, key={key}")
        cmd = ["auditctl", "-w", path, "-p", permissions, "-k", key]
        subprocess.run(["sudo"] + cmd, check=True)
        print("[✓] Watch added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[✗] Failed to add watch: {e}")
