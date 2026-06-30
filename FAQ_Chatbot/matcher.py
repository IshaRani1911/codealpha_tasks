import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nlp_utils import preprocess

class FAQMatcher:
    def __init__(self, faq_path="faqs.json"):
        with open(faq_path, "r", encoding="utf-8") as f:
            self.faqs = json.load(f)

        # Preprocess all stored questions once at startup
        self.questions = [preprocess(item["question"]) for item in self.faqs]
        self.answers = [item["answer"] for item in self.faqs]

        # Fit TF-IDF vectorizer on the FAQ questions
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_best_match(self, user_input, threshold=0.3):
        cleaned_input = preprocess(user_input)
        if cleaned_input.strip() == "":
            return "Please enter a valid question."

        user_vector = self.vectorizer.transform([cleaned_input])
        similarities = cosine_similarity(user_vector, self.question_vectors)[0]

        best_idx = similarities.argmax()
        best_score = similarities[best_idx]

        if best_score < threshold:
            return "Sorry, I couldn't find a good answer. Could you rephrase your question?"

        return self.answers[best_idx]