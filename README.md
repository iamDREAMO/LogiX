<div align="center">

# LogiX - Student Records Manager

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)

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

### Dependencies

LogiX utilizes only Python's standard library modules:

- `tkinter` - GUI framework (pre-installed with most Python distributions)
- `sqlite3` - Database management (included in Python standard library)

Note:_No external package installations are required._

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
├── main.py              # Application entry point
├── gui.py               # GUI components and screen layouts
├── database.py          # Database operations and queries
├── requirements.txt     # Project dependencies documentation
├── README.md            # Project documentation
└── demo.db             # SQLite database (auto-generated on first run)
```

## Usage Guide

### Initial Setup

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Register a New Account**
   - Click "Register" on the home screen
   - Enter username, password, and contact number
   - Click "Register" to create your account

3. **Login**
   - Enter your registered credentials
   - Click "Login" to access the main dashboard

### Managing Student Records

#### Adding a Student

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

- Navigate to the **ShowAll** tab
- All student records are displayed in a tabular format
- Data automatically refreshes after any modification

#### Searching for a Student

1. Navigate to the **Search** tab
2. Enter the student's roll number
3. Click "Search"
4. Student details will be displayed if found

#### Updating Student Information

1. Navigate to the **Update** tab
2. Enter the roll number of the student to update
3. Click "Retrieve" to load existing data
4. Modify the required fields
5. Click "Update" to save changes

#### Deleting a Student Record

1. Navigate to the **Delete** tab
2. Enter the roll number of the student to delete
3. Click "Delete"
4. Record will be permanently removed from the database

### Logging Out

- Navigate to the **LogOut** tab
- You will be automatically redirected to the home screen

## Database Schema

### Students Table (`ins`)

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| URNO | TEXT | Student roll number | PRIMARY KEY |
| UNAME | TEXT | Student name | - |
| UPHY | TEXT | Physics score | - |
| UCHE | TEXT | Chemistry score | - |
| UMATHS | TEXT | Mathematics score | - |

### Users Table (`regis`)

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| UNAME | TEXT | Username | - |
| UPASS | TEXT | Password | - |
| CN | TEXT | Contact Number | - |

## Troubleshooting

### Common Issues

#### Tkinter Not Found

**Error**: `ModuleNotFoundError: No module named 'tkinter'`

**Solution**:

- **Ubuntu/Debian**:
  ```bash
  sudo apt-get install python3-tk
  ```

- **Fedora**:
  ```bash
  sudo dnf install python3-tkinter
  ```

- **macOS**: Tkinter comes pre-installed with Python from python.org

- **Windows**: Reinstall Python and ensure "tcl/tk and IDLE" is selected

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

 - **Benedict Kofi Amofah** - [LinkedIn](https://www.linkedin.com/in/benedict-kofi-amofah) | [GitHub](https://github.com/iamDREAMO)
## Support

For support, questions, or feedback:

- **Email**: benedictkofiamofah@gmail.com
- **Issues**: [GitHub Issues](https://github.com/iamDREAMO/LogiX/issues)

## Version History

- **v1.0.0** (2025-10-28)
  - Initial release
  - Core CRUD functionality
  - User authentication system
  - Basic student record management

---

**Note**: This application is intended for educational and small-scale institutional use. For production deployment with sensitive data, additional security measures and thorough testing are recommended.