import re

def display_rules_with_headings(rules_dict):
    if not rules_dict:
        print("⚠️  No audit rules found.")
        return

    print(f"{'Index':<6} {'File name':<40} {'Permissions':<12} {'Audit key name':<20}")
    print("-" * 130)

    for index, rule in rules_dict.items():
        file = perm = key = "N/A"

        match_file = re.search(r"-w\s+(\S+)", rule)
        match_perm = re.search(r"-p\s+(\w+)", rule)
        match_key = re.search(r"-k\s+(\S+)", rule)

        if match_file:
            file = match_file.group(1)
        if match_perm:
            perm = match_perm.group(1)
        if match_key:
            key = match_key.group(1)

        print(f"{index:<6} {file:<40} {perm:<12} {key:<20}")
