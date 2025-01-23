import json

def load_data(file_path):
    """
    Load the question-answer data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing question-answer pairs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found. Please check the file path.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return {}

def calculate_similarity(user_input, candidate):
    """
    Calculate token-based similarity between user input and a candidate string.
    :param user_input: User's input string.
    :param candidate: Candidate string from the JSON data.
    :return: Similarity ratio (float between 0 and 1).
    """
    user_tokens = set(user_input.lower().split())
    candidate_tokens = set(candidate.lower().split())
    common_tokens = user_tokens.intersection(candidate_tokens)
    total_tokens = user_tokens.union(candidate_tokens)
    return len(common_tokens) / len(total_tokens) if total_tokens else 0

def find_best_match(user_input, qa_data, threshold=0.5):
    """
    Find the best match for the user input in the QA data.
    :param user_input: User's input string.
    :param qa_data: Dictionary of question-answer pairs.
    :param threshold: Minimum similarity ratio for a match.
    :return: Best match string or None if no match is found.
    """
    best_match = None
    highest_similarity = 0

    for question in qa_data.keys():
        similarity = calculate_similarity(user_input, question)
        if similarity > highest_similarity and similarity >= threshold:
            best_match = question
            highest_similarity = similarity

    return best_match

def chatbot():
    """
    Run the chatbot.
    """
    file_path = "chatbot_hr_discussion.json"  # Ensure the file exists in the same directory
    qa_data = load_data(file_path)

    if not qa_data:
        return

    print("Chatbot: Merhaba! Size nasıl yardımcı olabilirim? (Çıkmak için 'çık' yazabilirsiniz.)")
    
    while True:
        user_input = input("Kullanıcı: ").strip()
        
        if user_input.lower() == "çık":
            print("Chatbot: Görüşmek üzere!")
            break
        
        match = find_best_match(user_input, qa_data)

        if match:
            print(f"Chatbot: {qa_data[match]}")
        else:
            print("Chatbot: Bu konuda size yardımcı olamıyorum.")

if __name__ == "__main__":
    chatbot()
