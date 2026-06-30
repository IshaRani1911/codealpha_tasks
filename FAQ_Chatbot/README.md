# 🤖 FAQ Chatbot using NLP

An intelligent FAQ Chatbot built using **Python, Flask, HTML, CSS, JavaScript, and NLP**. The chatbot answers user queries by comparing them with a predefined FAQ dataset using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Features

- 💬 Interactive chatbot interface
- 🧠 NLP-based question preprocessing
- 🔍 TF-IDF Vectorization for text representation
- 📊 Cosine Similarity for finding the best matching FAQ
- ⚡ Fast responses without reloading the page (AJAX/Fetch API)
- ❌ Handles unknown questions gracefully
- ⌨️ Press **Enter** to send messages
- 📱 Simple and responsive user interface

---

## 🛠 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- NLTK
- Scikit-learn
- NumPy

---

## 📂 Project Structure

```
FAQ_Chatbot/
│
├── app.py
├── matcher.py
├── nlp_utils.py
├── faqs.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/codealpha_tasks.git
```

### 2. Go to the project folder

```bash
cd codealpha_tasks/FAQ_Chatbot
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. The user enters a question.
2. The input is preprocessed by:
   - Converting text to lowercase
   - Removing punctuation
   - Removing stop words
   - Lemmatizing words
3. The cleaned question is converted into a TF-IDF vector.
4. Cosine Similarity compares it with all stored FAQ questions.
5. The chatbot returns the most relevant answer.
6. If no suitable match is found, it asks the user to rephrase the question.

---

## 📚 Sample Questions

- Hello
- Hi
- What is AI?
- What is Python?
- What is NLP?
- What is Flask?
- What is Machine Learning?
- What is Deep Learning?
- What is HTML?
- What is CSS?
- What is JavaScript?
- What is Git?
- What is GitHub?
- How does this chatbot work?
- Can this chatbot answer every question?
- Thank you
- Bye

---

## 📦 Python Libraries Used

- Flask
- NLTK
- Scikit-learn
- NumPy

---

## 🎯 Future Improvements

- Voice input
- Speech output
- Chat history
- Database integration
- Transformer-based NLP models
- Multi-language support
- User authentication
- Dark mode

---

## 👨‍💻 Developed By

**Isha**

CodeAlpha Internship Project