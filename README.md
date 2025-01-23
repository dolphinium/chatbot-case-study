# Simple Chatbot Application

## Overview
This is a simple chatbot application developed using Python. The chatbot is designed to respond to user inputs based on a predefined set of question-answer pairs stored in a JSON file(See: chatbot_hr_discussion.json). It uses a custom similarity algorithm to handle minor input variations.

## Features
- Greets the user and provides appropriate responses.
- Responds to user inputs based on a JSON knowledge base.
- Handles minor spelling errors or variations using token-based similarity matching.
- Provides a default response for unknown queries. "Bu konuda size yardımcı olamıyorum." used in this case.

## Tests
The chatbot has been tested with the following algorithms:
1. Cosine Similarity
2. Euclidean Distance
3. Manhattan Distance
4. Levenshtein Distance

After testing I decided to use <b>Cosine Similarity</b> as the similarity algorithm for this chatbot.

## How to Use
1. Clone this repository to your local machine.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the chatbot using:
   ```bash
   python chatbot.py
