# Review Service Application 🌟

A professional Python GUI application built with Tkinter for collecting and managing customer reviews and ratings.

## Features ✨

- **Interactive Rating System**: Users can rate services on a scale of 0-10 using an intuitive slider interface
- **Beautiful Gradient UI**: Modern design with Aqua-to-Pink gradient backgrounds
- **Feedback Collection**: Comprehensive feedback mechanism for detailed customer reviews
- **Data Storage**: Automatically saves all reviews to a text file
- **Professional Interface**: Clean, responsive GUI built with Tkinter and Pillow
- **Error Handling**: Validates user input and prevents empty submissions

## Screenshots 📸

- Main window with service description and key features
- Interactive review window with gradient background
- Automatic file storage for all submissions

## Installation 🚀

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/review-service-app.git
cd review-service-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage 💡

Run the application:
```bash
python "tkinter day 19 Quiz Exercise.py"
```

### How to Use:
1. Launch the application
2. Click the **"Submit Review"** button
3. A new window will open with a rating slider
4. Select your rating (1-10 scale)
5. Click **"Enter your review"** button
6. See the thank you message and your review is saved!

### Features Explained:

- **Rating Scale**: 0-10 slider (0 shows error, 1-10 saves the review)
- **Data Persistence**: Reviews are saved to `Save Review.txt`
- **Validation**: Application prevents invalid (0 rating) submissions
- **Thank You Message**: Professional confirmation after submission

## Project Structure 📁

```
review-service-app/
│
├── tkinter day 19 Quiz Exercise.py    # Main application file
├── requirements.txt                    # Project dependencies
├── README.md                          # This file
└── Save Review.txt                    # Generated file (stores reviews)
```

## Technologies Used 🛠️

- **Tkinter**: GUI framework
- **Pillow (PIL)**: Image processing for gradient backgrounds
- **Python 3.x**: Core language

## File Format 📄

Reviews are saved in `Save Review.txt` with the following format:
```
5: This is user's review
7: This is user's review
9: This is user's review
```

## Requirements 📋

See `requirements.txt` for complete list:
- tkinter (built-in with Python)
- Pillow (for gradient graphics)

## UI Colors 🎨

- **Main Background**: Light Blue (#E8F4F8)
- **Inner Frame Gradient**: Aqua (#00FFFF) to Hot Pink (#FF69B4)
- **Buttons**: Green (#00AA00)
- **Text**: Professional fonts (Helvetica, Times New Roman, Arial)

## Error Handling ⚠️

- **Rating = 0**: Shows error message "Please enter your Review (Select 1-10)"
- **Valid Rating (1-10)**: Saves review and shows thank you message
- **File Operations**: Automatically creates file if it doesn't exist

## Future Enhancements 🚀

- [ ] Database integration (SQLite/MySQL)
- [ ] Export reviews to PDF/Excel
- [ ] Analytics dashboard
- [ ] User authentication
- [ ] Multiple review categories
- [ ] Star rating visualization
- [ ] Review editing capability

## Author 👨‍💻

Created as a learning project for Tkinter GUI development

## License 📜

This project is open source and available under the MIT License.

## Support 💬

For issues or questions, please open an issue on GitHub or contact the developer.

---

**Made with ❤️ using Python & Tkinter**
