from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# Load models only once (important for performance)
sentiment_analyzer = pipeline("sentiment-analysis")
similarity_model = SentenceTransformer("all-MiniLM-L6-v2")

def analyze_conversation(user_text, bot_text):
    # Sentiment analysis
    sentiment_result = sentiment_analyzer(user_text)[0]

    # Semantic similarity
    user_emb = similarity_model.encode(user_text, convert_to_tensor=True)
    bot_emb = similarity_model.encode(bot_text, convert_to_tensor=True)
    similarity_score = util.cos_sim(user_emb, bot_emb).item()

    # Convert similarity to 1–5 scale
    rating = round(similarity_score * 5, 2)

    return {
        "User Sentiment": sentiment_result["label"],
        "Sentiment Confidence": round(sentiment_result["score"], 2),
        "Relevance Score": round(similarity_score, 3),
        "Overall Conversation Rating (1-5)": rating
    }


# Run directly for testing
if __name__ == "__main__":
    user = "My internet is not working"
    bot = "Try restarting your router and check your cables."
    print(analyze_conversation(user, bot))
