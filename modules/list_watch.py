import subprocess

def list_audit_rules():
    try:
        # Capture the output of 'auditctl -l'
        result = subprocess.run(['sudo', 'auditctl', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        
        # Clean up lines and remove any empty lines or the "No rules" line
        lines = [line.strip() for line in result.stdout.splitlines() if line.strip() and line.strip().lower() != "no rules"]
        
        if not lines:
            return {}  # Return empty dict if there are no actual rules
        
        # Create a dictionary of the audit rules
        rules_dict = {i+1: line for i, line in enumerate(lines)}
        
        return rules_dict
        
    except subprocess.CalledProcessError:
        print("❌ Failed to list audit rules.")
        return {}
