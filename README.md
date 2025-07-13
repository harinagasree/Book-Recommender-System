## 📚 Book Recommendation System

A personalized Book Recommendation System built with **Python** and **Streamlit**, using **Collaborative Filtering** based on **Cosine Similarity**.
This project recommends books based on user preferences and also displays the **Top 50 most popular books**.

---

### 🚀 Features

* 🔍 **Collaborative Filtering** using cosine similarity between users
* 📈 **Top 50 Popular Books** section based on overall popularity
* 📚 **Personalized Recommendations** by analyzing similar user profiles
* 🖥️ **Interactive Web Interface** using Streamlit
* 📊 Clean UI for input, output, and recommendations

---

### 🛠️ Tech Stack

* **Python** 🐍
* **Streamlit** 🌐 for UI
* **Pandas** and **NumPy** for data processing
* **Cosine Similarity** from `sklearn.metrics.pairwise` for recommendation logic

---

### 📁 Project Structure

```
book-recommendation-system/
├── app.py                 # Streamlit web application
├── books.csv              # Books metadata (title, author, ratings)
├── users.csv              # User data
├── ratings.csv            # User ratings data
├── similarity.pkl         # Precomputed cosine similarity matrix
├── popular.pkl            # Data of top 50 popular books
├── pt.pkl                 # Data in pivot table based on book-title
├── README.md              # Project documentation
└── requirements.txt       # Dependencies list
```

---

### 🎯 How It Works

1. **Data Preparation**
   Loads books metadata and user rating datasets to create a user-item interaction matrix.

3. **Collaborative Filtering**

   * Computes **cosine similarity** between user vectors.
   * Recommends books liked by frequent readers.

4. **Popularity-Based Filtering**

   * Displays top 50 books based on user engagement and ratings.

5. **Streamlit UI**

   * User inputs book title or selects from dropdown.
   * Displays personalized recommendations with cover images and authors.

---

### 💻 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/harinagasree/book-recommendation-system.git
cd book-recommendation-system

# Install dependencies
pip install -r requirements.txt

streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2

# Run the app
streamlit run app.py
```

---

### 📸 Sample Output

> 💡 *User selects "The Alchemist" → Recommends books like "Brida", "Eleven Minutes", etc., based on similar user preferences.*

---

### 📦 Dataset Sources

* [Books Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
*  Data is available on kaggle books.csv, users.csv, ratings.csv
* Custom filtered datasets to include most-rated books

---

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---
