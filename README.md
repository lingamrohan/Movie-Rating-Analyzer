# Movie-Rating-Analyzer
 Movie Ratings Analyzer — A Python project using pandas, numpy, and matplotlib to explore and visualize movie ratings with filtering by genre and user analysis.
# 🎬 Movie Ratings Analyzer

A beginner-friendly Python project that loads a sample movie ratings dataset and performs simple data analysis using **pandas**, **numpy**, and **matplotlib**.

> 🔍 Analyze movie ratings, filter by genre, and visualize average ratings — all in a few lines of code!

---

## 📌 Features

- ✅ Load sample movie and ratings data
- ✅ Find top-rated movies
- ✅ Filter movies by genre
- ✅ Show average rating by user
- ✅ Visualize average rating per movie with a bar chart

---

## 🛠️ Built With

- [pandas](https://pandas.pydata.org/) - For data manipulation
- [numpy](https://numpy.org/) - For numerical operations
- [matplotlib](https://matplotlib.org/) - For data visualization

---

## ▶️ Getting Started

### Prerequisites

Make sure you have Python installed with the following libraries:

```bash
pip install pandas matplotlib numpy
python movie_analyzer.py
🎥 Top Rated Movies:
The Dark Knight    5.0
Interstellar       4.5
The Matrix         4.5
Parasite           4.0
Inception          4.0

Enter a genre to filter (e.g., Sci-Fi, Action, Drama): Sci-Fi

🎬 Movies in Genre 'Sci-Fi':
           title  rating
0     The Matrix       5
1     The Matrix       4
2      Inception       5
3      Inception       3
4   Interstellar       4
5   Interstellar       5

👤 Average Rating by User:
userId
101    5.0
102    4.0
103    5.0
104    3.0
105    4.0
106    5.0
https://1drv.ms/i/c/d85a33a04ae7b885/EQHY4tHykVBEi4a51H9VKiwBndX4DNfvpYnqbSDAzAU7Yg?e=hIAD5l
107    5.0
108    4.0
movie-analyzer/
│
├── movie_analyzer.py     # Main Python script
└── README.md             # This file
