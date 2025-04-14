# 📚 Bookshelf Web App

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)

## Features

### Basic features
- Responsive UI - A clean and user-friendly interface to browse your bookshelf.
- Upload Books - Import book details from CSV or Excel files.
- Export Data - Download your collection as CSV or Excel files.
- User Authentication - Secure login and registration to manage your personal bookshelf.
- Manage Collection - View, add, edit, and delete books in your collection.
- Book Covers - Upload and display cover images for books.
- Search & Filter - Find books by title, author, genre, or publication year.

### Future plans
- Reading Progress Tracking - Track your progress, save page numbers, or mark books as "Reading", "Finished", or "Want to Read".
- Book Synopsis & Quotes - Save summaries or your favorite quotes from books for later reference.
- Book Ratings & Reviews - Rate and review books to share your thoughts on what you liked or disliked.
- Wishlist - Create and manage a wishlist of books you'd like to read in the future.
- Reading Goals - Set and track reading goals.
- Recommendations - Get book recommendations based on your reading history or preferences.
- Dark Mode - Switch to dark mode for a more comfortable reading experience.
- Interactive Calendar - Use a calendar to mark your reading schedule and track your progress.
- View Other User's Bookshelves - Explore bookshelves of other users, unless they are marked private.
- Privacy Settings - Set your bookshelf as public or private, depending on your preference.
- Friends & Social Features - Add friends to follow their bookshelves, share recommendations, and interact with others.

## Technologies
- Backend: Python, Django
- Database: SQLite
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

## Acknowledgments
- [djangoproject](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.