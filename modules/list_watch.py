import subprocess
from modules.clear_screen import clear_screen

def list_audit_rules():
    
    print("-" * 100)
    try:
        # Capture the output of 'auditctl -l'
        result = subprocess.run(['sudo', 'auditctl', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        
        # Split the output into lines and create a dictionary
        rules_dict = {i+1: line for i, line in enumerate(result.stdout.splitlines())}
        
        return rules_dict
        
    except subprocess.CalledProcessError:
        print("Failed to list audit rules.")
        return {}
    

