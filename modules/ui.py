def header(): #To print UI header
    
        logo = r"""

                    _ _ _    _____                      
     /\            | (_) |  / ____|                     
    /  \  _   _  __| |_| |_| (___   ___ ___  _ __   ___ 
   / /\ \| | | |/ _` | | __|\___ \ / __/ _ \| '_ \ / _ \
  / ____ \ |_| | (_| | | |_ ____) | (_| (_) | |_) |  __/
 /_/    \_\__,_|\__,_|_|\__|_____/ \___\___/| .__/ \___|
                                            | |         
                                            |_|         
                                    
 ~ AuditScope - Created by Aswin KS ~
    """
    
        description = """
AuditScope is a command-line tool designed to simplify the management of Linux audit rules.
It allows users to easily add, view, and remove audit watch rules on files and directories for monitoring critical system changes.


Press Ctrl+C to go back

    """
        print(logo)
        print(description)
        print("-" * 130)