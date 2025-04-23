from modules.list_watch import list_audit_rules
def header(): #To print UI header
    
    
        logo = r"""

   _               _  _  _    __                          
  /_\   _   _   __| |(_)| |_ / _\  ___  ___   _ __    ___ 
 //_\\ | | | | / _` || || __|\ \  / __|/ _ \ | '_ \  / _ \
/  _  \| |_| || (_| || || |_ _\ \| (__| (_) || |_) ||  __/
\_/ \_/ \__,_| \__,_||_| \__|\__/ \___|\___/ | .__/  \___|
                                             |_|                                                  

    """
    
        description = """
AuditScope is a command-line tool designed to simplify the management of Linux audit rules.

It allows users to easily add, view, and remove audit watch rules on files and directories for monitoring critical system changes.

Press Ctrl+C to go back

    """        

        print(logo)
        print(description)
        count_total_audits()
        print("-" * 130)

def count_total_audits():

    total = len(list_audit_rules())
    print(f"\n📊 Total file Auditing: {total}")

def print_about():
         
        logo = r"""

   _               _  _  _    __                          
  /_\   _   _   __| |(_)| |_ / _\  ___  ___   _ __    ___ 
 //_\\ | | | | / _` || || __|\ \  / __|/ _ \ | '_ \  / _ \
/  _  \| |_| || (_| || || |_ _\ \| (__| (_) || |_) ||  __/
\_/ \_/ \__,_| \__,_||_| \__|\__/ \___|\___/ | .__/  \___|
                                             |_|                                                  

    """
    
        description = """
AuditScope is a command-line tool designed to simplify the management of Linux audit rules.

It allows users to easily add, view, and remove audit watch rules on files and directories for monitoring critical system changes.

🧑  Developer: Aswin KS

🌐  GitHub: https://github.com/aswinks123/AuditScope

📌  LinkedIn: https://www.linkedin.com/in/aswinks-profile/

    """ 
        print(logo)
        print(description)

