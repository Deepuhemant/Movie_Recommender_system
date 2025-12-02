# 🎬 Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-green)]

An intelligent content-based movie recommendation engine that suggests movies based on similarity metrics of content, cast, and director information.

## 📋 Overview

This project implements a movie recommendation system using collaborative filtering and content-based filtering techniques. The system analyzes movie features like cast, director, and genres to recommend the 5 most similar movies to a given input.

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on similarity scores
- **Multiple Attributes**: Considers cast, director, and genre information
- **Interactive Web Interface**: Streamlit-based user-friendly application
- **Easy Integration**: Simple API for adding to other projects
- **Well-Documented**: Comprehensive Jupyter notebooks for learning

## 📁 Project Structure

```
├── movierecommendersystem.ipynb    # Main ML model notebook
├── app.py                           # Streamlit web application
├── tmdb_5000_movies.csv             # Movie dataset (TMDB)
├── README.md                        # This file
└── LICENSE                          # MIT License
```

## 🛠 Tech Stack

- **Python 3.8+**
- **Libraries**: Pandas, Scikit-learn, Streamlit
- **Data Source**: TMDB 5000 Movies Dataset

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas scikit-learn streamlit
```

### Running the Application

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to use the application.

### Using the Jupyter Notebook

```bash
jupyter notebook movierecommendersystem.ipynb
```

## 📊 Dataset

- **Source**: TMDB (The Movie Database)
- **Records**: 5000 movies
- **Features**: Title, cast, director, genres, plot, release year, and more

## 🎯 How It Works

1. **Data Preprocessing**: Clean and vectorize movie metadata
2. **Similarity Calculation**: Compute cosine similarity between movies
3. **Recommendation**: Return top 5 most similar movies
4. **User Interface**: Present recommendations through Streamlit app

## 📈 Model Performance

- Efficient similarity computation using sparse matrices
- Real-time recommendations with minimal latency
- Scalable architecture for larger datasets

## 💡 Future Enhancements

- [ ] Collaborative filtering for personalized recommendations
- [ ] User rating system and feedback mechanism
- [ ] Hybrid recommendation approach
- [ ] API deployment
- [ ] Docker containerization

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📧 Contact

For questions or feedback, please reach out through GitHub issues.
