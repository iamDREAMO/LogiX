<div align="center">

# LogiX - Student Records Manager

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)

![hero](<app screenshots(png)/hero.gif>)

*A desktop application for student record management*

</div>

## Overview

LogiX is a desktop application designed for student record management. Built with Python's Tkinter framework and SQLite3 database, it provides an intuitive graphical interface to manage student academic records such as subject-wise performance metrics.

## Features

### Core Functionality

- **User Authentication System**
  - With secure registration, login, and session management
  

- **Student Record Management**
  - **Create**: Add new student records with roll number, name, and subject scores
  - **Read**: View all student records in an organized tabular format
  - **Update**: Modify existing student information with data validation
  - **Delete**: Remove student records with confirmation
  - **Search**: Query student records by roll number with instant results

- **Academic Performance Tracking**
  - Academic performance tracking with subject-wise scores and real-time data synchronization


## System Requirements

### Prerequisites

- **Python**: Version 3.10 or higher
- **Operating System**: Windows, Linux, or macOS
- **Display**: Minimum resolution of 800x600 pixels
- `tkinter` - GUI framework (pre-installed with most Python distributions)
- `sqlite3` - Database management (included in Python standard library)

**Note**: LogiX utilizes only Python's standard library modules. No external package installations are required.

## Downloads

Get the latest release here:
https://github.com/iamDREAMO/LogiX/releases/tag/v1.0.0

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/LogiX.git
cd LogiX
```

### Step 2: Verify Python Installation

```bash
python --version
```

Ensure the version is 3.10 or higher.

### Step 3: Verify Tkinter Installation

```bash
python -c "import tkinter"
```

If Tkinter is not installed, refer to the [Tkinter Installation Guide](https://docs.python.org/3/library/tkinter.html) below.

### Step 4: Run the Application

```bash
python main.py
```

## Project Structure

```
LogiX/
├── app_screenshots(png)/     # Application screenshots and demo GIFs
│   ├── hero.gif             # Hero GIF showing app workflow
│   ├── home.png             # Welcome/home screen
│   ├── dashboard.png        # ShowAll tab with student records
│   ├── insert.png           # Insert student form
│   ├── search.png           # Search functionality
│   ├── update.png           # Update student form
│   └── delete.png           # Delete functionality
│
├── src/                      # Source code directory
│   ├── gui.py               # GUI components and screen layouts
│   └── database.py          # Database operations and queries
│
├── .gitignore               # Git ignore rules (Python, DB, IDE files)
├── LICENSE                  # MIT License
├── README.md                # Project documentation
├── main.py                  # Application entry point
└── pyproject.toml           # Project metadata and dependencies
```

## Usage Guide

### Initial Setup

1. **Launch the Application**
   ```bash
   python main.py
   ```
![home](<app screenshots(png)/home.png>)

2. **Register a New Account**
   - Click "Register" on the home screen
   - Enter username, password, and contact number
   - Click "Register" to create your account

3. **Login**
   - Enter your registered credentials
   - Click "Login" to access the main dashboard

### Managing Student Records

#### Adding a Student
![insert](<app screenshots(png)/insert.png>)

1. Navigate to the **Insert** tab
2. Fill in the required fields:
   - Roll Number (unique identifier)
   - Student Name
   - Physics Score
   - Chemistry Score
   - Mathematics Score
3. Click "Insert Data"
4. Confirmation message will appear upon successful insertion

#### Viewing All Records
![dashboard](<app screenshots(png)/dashboard.png>)

- Navigate to the **ShowAll** tab
- All student records are displayed in a tabular format
- Data automatically refreshes after any modification

#### Searching for a Student
![search](<app screenshots(png)/search.png>)

1. Navigate to the **Search** tab
2. Enter the student's roll number
3. Click "Search"
4. Student details will be displayed if found

#### Updating Student Information
![update](<app screenshots(png)/update.png>)

1. Navigate to the **Update** tab
2. Enter the roll number of the student to update
3. Click "Retrieve" to load existing data
4. Modify the required fields
5. Click "Update" to save changes

#### Deleting a Student Record
![delete](<app screenshots(png)/delete.png>)

1. Navigate to the **Delete** tab
2. Enter the roll number of the student to delete
3. Click "Delete"
4. Record will be permanently removed from the database

### Logging Out

- Navigate to the **LogOut** tab
- You will be automatically redirected to the home screen

## Database Schema

### Students Table (`students`)

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| roll_no | TEXT | Student roll number | PRIMARY KEY |
| name | TEXT | Student name | - |
| phys| TEXT | Physics score | - |
| chem| TEXT | Chemistry score | - |
| maths | TEXT | Mathematics score | - |

### Users Table (`users`)

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| username | TEXT | Username | - |
| password | TEXT | Password | - |

## Future Enhancements (Open to Contributors!)

- [ ] Advanced search filters (by name, score range)
- [ ] Data export functionality (CSV, PDF)
- [ ] Graphical analytics and performance reports
- [ ] Batch import of student records
- [ ] Password encryption using hashing algorithms
- [ ] User role management (admin, teacher, viewer)
- [ ] Backup and restore functionality
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

 - Follow PEP 8 style guidelines, include docstrings, comment complex logic, and write meaningful commit messages


## Developer/Support
For support, questions, or feedback:
 - **Benedict Kofi Amofah** - [LinkedIn](https://www.linkedin.com/in/benedict-kofi-amofah) | [GitHub](https://github.com/iamDREAMO)
- **Email**: benedictkofiamofah@gmail.com
- **Issues**: [GitHub Issues](https://github.com/iamDREAMO/LogiX/issues)

## Project Evolution

LogiX began as a Python-based CLI application before evolving into a full desktop GUI with cross-platform executables.

- **v0.1.x** — Command-line interface (CLI) prototype (2025-10-27)
- **v0.5.x** — Tkinter-based desktop GUI (2025-10-28)
- **v1.0.0** — Linux and Windows executables (2026-01-14/2026-01-19)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This application is intended for educational and small-scale institutional use. For production deployment with sensitive data, additional security measures and thorough testing are recommended.
