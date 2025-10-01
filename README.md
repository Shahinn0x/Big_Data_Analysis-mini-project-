# Movie Recommendation System

A simple Movie Recommendation System built with **Python**, **Streamlit**, and **TMDB dataset**.  
This app recommends movies similar to your chosen movie based on content similarity.

---

## 🚀 Features
- Search for any movie in the dataset
- Get a list of top 5 recommended movies
- Interactive and easy-to-use **Streamlit web interface**

---

## 🛠 Technology Stack
- Python 3.x
- Streamlit
- Pandas
- Scikit-learn (`CountVectorizer`, `cosine_similarity`)
- TMDB 5000 Movie Dataset

---

## 📂 Project Structure

<img width="796" height="468" alt="image" src="https://github.com/user-attachments/assets/c9ba7aab-31b9-4b5b-8405-a6847ecd6e4b" />


---

## ⚡ How to Run Locally

## 1.Clone the repo
```bash
git clone https://github.com/YourUsername/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Download TMDB dataset

-Download tmdb_5000_movies.csv and tmdb_5000_credits.csv from Kaggle
-Place the CSVs in the project root folder.

### Generate the pickle file
```bash
python prepare_data.py
```

### Run the Streamlit app
```bash
streamlit run app.py
```

## 📝 Notes

movie_data.pkl is not included in the GitHub repo due to size restrictions (>100MB).

You can regenerate it anytime using prepare_data.py.

## 🔗 References

TMDB 5000 Movie Dataset

Streamlit documentation: https://docs.streamlit.io/

## 📌 License

This project is open-source and available under the MIT License.


---
 

### Block Diagram

![The-recommendation-system-types](https://github.com/user-attachments/assets/b08f4f84-9210-4dfb-9734-860b353a3da7)


## Results
The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.

![Screenshot 2024-07-12 103743](https://github.com/user-attachments/assets/fbc357a1-a6e6-472a-892b-95fe96767743)

