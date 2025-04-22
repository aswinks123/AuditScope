# AuditScope - Simplified Audit Manager for Linux

<div style="display: flex; align-items: center;">
    <img src="resources/logo.png" alt="NixVault Icon" width="50" style="margin-right: 10px;"/>
    <p>AuditScope is a command-line tool designed to simplify the management of Linux audit rules. It allows users to easily add, view, and remove audit watch rules on files and directories for monitoring critical system changes.</p>
</div>

```
                    _ _ _    _____                      
     /\            | (_) |  / ____|                     
    /  \  _   _  __| |_| |_| (___   ___ ___  _ __   ___ 
   / /\ \| | | |/ _` | | __|\___ \ / __/ _ \| '_ \ / _ \
  / ____ \ |_| | (_| | | |_ ____) | (_| (_) | |_) |  __/
 /_/    \_\__,_|\__,_|_|\__|_____/ \___\___/| .__/ \___|
                                            | |         
                                            |_|         
                                    
 ~ AuditScope - Created by Aswin KS ~ 

```

## Features

✨ Add Audit Rules: Monitor file or directory changes with custom permissions and keys.

✨ List Existing Rules: View all active audit rules in a structured format.

✨ Remove Audit Rules: Safely delete specific audit rules by index.

✨ View Audit Logs: Search and display logs filtered by audit key.

✨ User-Friendly Interface: Interactive prompts guide users through each operation.

✨ Cross-Platform Compatibility: Designed for Linux systems using auditctl and ausearch.​

✨ Efficient error handling mechanism.​

✨ Built using Python



## Installation

### Prerequisites

Ensure the following packages are installed:
```bash
auditd  #It will be installed automatically

sudo

python3
```

### Steps

```bash
git clone https://github.com/aswinks123/AuditScope
cd Auditscope
python3 auditscope.py
```

## Usage

```bash
1. 🗂️  Add a file to audit
2. 📌 List all audit Rules
3. 🗑️  Remove an audit Rule
4. 📑 View detailed audit log
0. ⭕ Exit
```

### Add a File to Audit

Enter the absolute path of the file or directory.

Specify the permissions to monitor (e.g., r, w, x, a).

Provide a custom key name for the audit rule.​

### List All Audit Rules

Displays a table of all active audit rules with their index, file name, permissions, and key name.​

### Remove an Audit Rule

View the list of active rules.

Enter the index number of the rule you wish to remove.

Confirm the deletion when prompted.​

### View Detailed Audit Log

Enter the audit key to filter logs.

Optionally, specify the number of latest entries to view (default is all).

The logs will display detailed information, including time, operation, file, command, executable, UID, AUID, session ID, TTY, and key name.

## Code Structure

```bash
├── auditscope.py         # Entry point for the application
├── requirements.txt      # Python dependencies
├── modules/
│   ├── add_watch.py      # Functions for adding audit rules
│   ├── install_auditd.py # Checks and installs auditd if necessary
│   ├── list_watch.py     # Lists all active audit rules
│   ├── remove_watch.py   # Removes specified audit rules
│   ├── view_logs.py      # Views audit logs filtered by key
│   └── ui.py             # User interface components
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a new Pull Request.

## Acknowledgments

Inspired by various open-source audit tools.

Thanks to contributors and the open-source community for their support.​

## Live Demo

![alt text](/resources/auditscope.gif)

## Sample Screenshot

### Home Page
![alt text](/resources/image.png)


### Add a new Audit file
![alt text](/resources/image-1.png)

### Delete file from Auditing
![alt text](/resources/image3.png)

### View audit logs of the file
![alt text](/resources/image-2.png)