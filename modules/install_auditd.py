import shutil
import subprocess
import sys

def check_and_install_auditctl():

    if shutil.which("auditctl") is None:
        print("auditctl is not installed.")
        choice = input("Do you want to install it now? (y/n): ").strip().lower()
        if choice == "y":
            try:                
                print("[...] Installing auditd...Please wait..")
                devnull = open('/dev/null', 'w')
                subprocess.run(["sudo", "apt", "update"], stdout=devnull, stderr=devnull, check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "auditd"], stdout=devnull, stderr=devnull, check=True)
                print("[✓] 'auditd' has been installed Scuessfully.")
            except subprocess.CalledProcessError as e:
                print(f"[✗] Installation failed: {e}")
                sys.exit(1)
        else:
            print("Failed!. Please install 'auditd' manually and try again.")
            sys.exit(1)
    else:
        pass
