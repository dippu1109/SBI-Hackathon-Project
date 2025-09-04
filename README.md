# Anti-India Campaign Detection on digital platforms

## 📌 Problem Statement
**Detecting Anti-India Campaigns on Digital Platforms**

This project is our prototype submission for the **National CyberShield Hackathon 2025**.  
The solution focuses on identifying and classifying anti-India and hate speech content on social media using Machine Learning.

---

## 🚀 Our Solution
We built a pipeline that:
1. **Collects Data** – from open-source datasets (Hindi, Hinglish, English hate speech datasets).
2. **Preprocesses Text** – clean, normalize, and vectorize social media posts.
3. **ML Model** – trained with TF-IDF + ML classifier to detect Anti-India/Hate vs Neutral content.
4. **App Interface** – a Streamlit app where users can input text and get classification results in real time.

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **ML Libraries:** scikit-learn, pandas, numpy
- **Vectorization:** TF-IDF
- **Deployment:** Streamlit
- **Visualization:** matplotlib, wordcloud
- **Dataset Sources:** Indo-HateSpeech, Tweets

---

## 📂 Project Structure
```
SBI-Hackathon-Project/
│── data/
│   └── merged_anti_india_dataset.csv
│── models/
│   ├── hate_speech_model.pkl
│   └── tfidf_vectorizer.pkl
│── src/
│   ├── Hate_Speech_ML_model.ipynb   # Training Notebook
│   └── Hate_speech_detecting_app.py # Streamlit App
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/Venki01a/SBI-Hackathon-Project.git
cd SBI-Hackathon-Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run Hate_speech_detecting_app.py
```

---

## 📊 Results
- The model achieves ~85% accuracy on test data.  
- Detects hate/anti-India vs neutral posts.  
- Demo app provides real-time classification.  

---

## 🔮 Future Scope
To make the solution more powerful for **campaign detection**, we plan to add:
- Hashtag & keyword trend analysis
- Bot detection (frequent/automated accounts)
- Network graphs of coordinated accounts
- Multilingual improvements (IndicBERT / XLM-RoBERTa)

---

## 👥 Team Cyber Rakshak
- Venkatesh Garg (Team Lead)
- Anuradha Singh
- Dipankar Rao Jeurkar

---

## 📜 License
This project is licensed under the Apache 2.0 License.
