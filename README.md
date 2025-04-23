# AuditScope - Simplified Audit Manager for Linux

<div style="display: flex; align-items: center;">
    <img src="resources/logo.png" alt="NixVault Icon" width="50" style="margin-right: 10px;"/>
    <p>AuditScope is a feature-rich, user-friendly command-line tool designed to simplify and enhance the management of Linux audit rules. It empowers system administrators, DevOps engineers, and security professionals to efficiently monitor and protect critical files, directories, and system activities using the Linux Audit System.
With AuditScope, you can effortlessly add, view, and remove audit watch rules without memorizing complex auditctl syntax. Whether you're tracking unauthorized changes to sensitive files or ensuring compliance with security policies, AuditScope helps you maintain visibility and control over your system’s audit trail.</p>
</div>

```
   _               _  _  _    __                          
  /_\   _   _   __| |(_)| |_ / _\  ___  ___   _ __    ___ 
 //_\\ | | | | / _` || || __|\ \  / __|/ _ \ | '_ \  / _ \
/  _  \| |_| || (_| || || |_ _\ \| (__| (_) || |_) ||  __/
\_/ \_/ \__,_| \__,_||_| \__|\__/ \___|\___/ | .__/  \___|
                                             |_|               
                                    
 ~ AuditScope - Created by Aswin KS ~ 

```

## 🚀 Key Features


✨ Add Audit Rules Permanently

Monitor critical file or directory changes with custom permissions (r, w, x, a) and associate them with unique audit keys for streamlined tracking.

📋 List Active Rules in One Command

Display all currently active audit rules in a clean, readable format — no more deciphering raw auditctl output.

🗑️ Remove Rules by Index

Safely delete specific audit rules using an intuitive indexed list, minimizing the risk of removing the wrong rule.

🔍 Search Audit Logs by Key

Filter and display audit logs using specific audit keys — quickly identify changes, access attempts, or unauthorized actions.

📤 Export Logs to File

Export filtered audit logs to a timestamped .log file for further analysis, reporting, or incident documentation.

🧑‍💻 User-Friendly Interactive Interface

Guided prompts at every step ensure an intuitive experience for both beginners and advanced users.

🐧 Designed for Linux Systems

Built to work seamlessly with Linux’s auditctl and ausearch, providing native integration with the audit subsystem.

⚙️ Robust Error Handling

Built-in exception handling for invalid inputs, interruptions, and failed operations — ensuring a smooth user experience.

🐍 Powered by Python

Lightweight, fast, and easy to install with minimal dependencies — suitable for local or remote server environments.


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
2. 📌  List audit Rules
3. 🗑️  Remove audit Rule
4. 📑  View and Download Logs
5. 🌟  About
0. ⭕  Exit
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

### View and Download Logs

Enter the audit key to filter logs.

Optionally, specify the number of latest entries to view (default is all).

The logs will display detailed information, including time, operation, file, command, executable, UID, AUID, session ID, TTY, and key name.

Download the log file to local machine

### About

About the Developer and program

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

![alt text](/resources/audit-scope-live.gif)

## Sample Screenshots

### Home Page
![alt text](/resources/image.png)

### Add a new audit file
![alt text](/resources/add.png)

### View audit rules
![alt text](/resources/view.png)

### Delete file from auditing
![alt text](/resources/delete.png)

### View audit logs of the file
![alt text](/resources/logs.png)

### Export logs to a file
![alt text](/resources/export.png)

### About Section
![alt text](/resources/about.png)
