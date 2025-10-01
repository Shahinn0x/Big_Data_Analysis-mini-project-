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

Movie-Recommendation-System/
│
├─ app.py # Streamlit app
├─ prepare_data.py # Preprocessing and generating movie_data.pkl
├─ tmdb_5000_movies.csv # Original dataset (not pushed to GitHub)
├─ tmdb_5000_credits.csv # Original dataset (not pushed to GitHub)
├─ movie_data.pkl # Pickle file (ignored in GitHub)
├─ requirements.txt # Python dependencies
└─ README.md

---

## ⚡ How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/YourUsername/Movie-Recommendation-System.git
cd Movie-Recommendation-System

Install dependencies
<img width="798" height="99" alt="image" src="https://github.com/user-attachments/assets/82ac5e20-f3fe-4d5d-8b4a-a834fb2f15b7" />

Download TMDB dataset

Download tmdb_5000_movies.csv and tmdb_5000_credits.csv from Kaggle

Place the CSVs in the project root folder.

Generate the pickle file
<img width="815" height="82" alt="image" src="https://github.com/user-attachments/assets/88f6b0b2-dac1-489b-900c-5a8a881fc6d4" />

Run the Streamlit app
<img width="808" height="94" alt="image" src="https://github.com/user-attachments/assets/3ba05526-5d4d-4ca9-b757-5647ae4785b3" />
📝 Notes

movie_data.pkl is not included in the GitHub repo due to size restrictions (>100MB).

You can regenerate it anytime using prepare_data.py.

🔗 References

TMDB 5000 Movie Dataset

Streamlit documentation: https://docs.streamlit.io/

📌 License

This project is open-source and available under the MIT License.


---

### ✅ Optional Extras
- Add a screenshot of the Streamlit app at the top.
- Add a **GIF demo** of your app if you want it to look more professional.  
- Update `requirements.txt` with the exact versions of `pandas`, `scikit-learn`, `streamlit`, etc.  

---

If you want, I can also **write a ready-to-use `requirements.txt`** for this project so anyone can run it without errors. Do you want me to do that?



