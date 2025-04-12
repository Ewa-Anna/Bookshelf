# 📚 Bookshelf Web App

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Features
- Upload Books: Import book details from CSV or Excel files.
- Manage Collection: View, add, edit, and delete books in your collection.
- Export Data: Download your collection as CSV or Excel files for offline use.
- Search & Filter: Find books by title, author, genre, or publication year.
- Book Covers: Upload and display cover images for books (optional).
- Responsive UI: A clean and user-friendly interface to browse your bookshelf.

## Technologies
- Backend: Python, Django
- Database: SQLite (PostgreSQL for production)
- Frontend: Django Templates, Bootstrap

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Running the project locally
1. Clone the repository

` git clone https://github.com/Ewa-Anna/Bookshelf `

2. Install dependencies

` pip install -r requirements.txt `

3. Change the directory

` cd bookshelf `

4. Apply database migrations

` python manage.py makemigrations `

` python manage.py migrate `

5. Run the project

` python manage.py runserver `

Project will run on http://127.0.0.1:8000/

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

