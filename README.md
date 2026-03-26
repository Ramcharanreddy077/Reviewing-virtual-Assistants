#  AI Conversation Reviewer for Virtual Assistants
An AI-powered system that evaluates conversations between a user and a virtual assistant using **Natural Language Processing (NLP)** techniques.
This project analyzes conversations based on **sentiment, semantic similarity, and relevance**, and provides an overall rating of the assistant’s response.

## Features
* Sentiment Analysis of user input
* Semantic Similarity between user query and assistant response
* Relevance Scoring using embeddings
* Overall Conversation Rating (1–5 scale)
* Interactive Streamlit Web Interface

## 🛠 Tech Stack
* Python
* Streamlit (for UI)
* Hugging Face Transformers (sentiment analysis)
* Sentence Transformers (semantic similarity)
* Pandas
  
## 📂 Project Structure

Reviewing-virtual-Assistants/
│── app.py          # Streamlit UI
│── reviewer.py     # Core NLP logic
│── utils.py        # Dataset utilities
│── README.md
```
## ⚙️ How It Works

1. User enters:
   * A **message**
   * A **virtual assistant response**
2. The system:
   * Detects sentiment using NLP
   * Computes similarity using embeddings
   * Evaluates relevance
3. Outputs:
   * Sentiment label & confidence
   * Similarity score
   * Overall rating

👉 Example from your code:
* Sentiment is calculated using a transformer model 
* Similarity is computed using sentence embeddings 
* Results are displayed via Streamlit UI 

## ▶️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Ramcharanreddy077/Reviewing-virtual-Assistants.git
cd Reviewing-virtual-Assistants
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file, install manually:

```bash
pip install streamlit transformers sentence-transformers pandas
```
### 3. Run the App

```bash
streamlit run app.py
```
## Usage
* Enter user message
* Enter assistant reply
* Click **Analyze Conversation**

-> The system will display:

* Sentiment
* Confidence
* Relevance Score
* Overall Rating


## Example

**User:** My internet is not working
**Bot:** Try restarting your router

Output:

* Sentiment: Negative
* Relevance Score: High
* Rating: ~4.5

## Future Improvements

* Add support for **multi-turn conversations**
* Visual dashboards (graphs/charts)
* Compare multiple assistants (Alexa, Siri, etc.)
* Store and analyze conversation datasets
* Deploy as a web app

## Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

##  License

This project is open-source and free to use.
