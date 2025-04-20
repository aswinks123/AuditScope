import subprocess
import subprocess
import subprocess
from modules.list_watch import list_audit_rules
from modules.clear_screen import clear_screen


def remove_watch_by_index(index):
    """
    Remove the watch rule by its index using -W (deletion syntax).
    
    Parameters:
        index (int): The index number of the rule to delete.
    """
    rules = list_audit_rules()
    
    if index in rules:
        rule_to_remove = rules[index]
        print(f"Removing watch: {rule_to_remove}")

        # Replace the first '-w' with '-W' for deletion
        rule_parts = rule_to_remove.strip().split()
        if '-w' in rule_parts:
            rule_parts[rule_parts.index('-w')] = '-W'
        else:
            print("[✗] Invalid rule format, missing '-w'")
            return

        cmd = ["sudo", "auditctl"] + rule_parts

        try:
            subprocess.run(cmd, check=True)
            print(f"[✓] Watch rule removed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"[✗] Failed to remove the rule: {e}")
    else:
        print("[✗] Invalid index.")