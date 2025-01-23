import json
import math

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

def calculate_cosine_similarity(user_input, candidate):
    """
    Calculate cosine similarity between user input and a candidate string.
    :param user_input: User's input string.
    :param candidate: Candidate string from the JSON data.
    :return: Cosine similarity (float between 0 and 1).
    """
    # Convert the input strings into token frequencies
    user_tokens = user_input.lower().split()
    candidate_tokens = candidate.lower().split()

    # Create word frequency dictionaries
    user_freq = {}
    candidate_freq = {}

    for token in user_tokens:
        user_freq[token] = user_freq.get(token, 0) + 1

    for token in candidate_tokens:
        candidate_freq[token] = candidate_freq.get(token, 0) + 1

    # Calculate the dot product
    dot_product = sum(user_freq.get(token, 0) * candidate_freq.get(token, 0) for token in user_freq)

    # Calculate the magnitudes (L2 norms) of the vectors
    user_magnitude = math.sqrt(sum(value ** 2 for value in user_freq.values()))
    candidate_magnitude = math.sqrt(sum(value ** 2 for value in candidate_freq.values()))

    # Avoid division by zero
    if user_magnitude == 0 or candidate_magnitude == 0:
        return 0

    # Cosine similarity formula
    return dot_product / (user_magnitude * candidate_magnitude)

def find_best_match(user_input, qa_data, threshold=0.2, use_cosine=False):
    """
    Find the best match for the user input in the QA data.
    :param user_input: User's input string.
    :param qa_data: Dictionary of question-answer pairs.
    :param threshold: Minimum similarity ratio for a match.
    :param use_cosine: Whether to use cosine similarity (default False uses token-based).
    :return: Best match string or None if no match is found.
    """
    best_match = None
    highest_similarity = 0

    for question in qa_data.keys():
        if use_cosine:
            similarity = calculate_cosine_similarity(user_input, question)
        else:
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
        
        match = find_best_match(user_input, qa_data, use_cosine=True)  # Use cosine similarity

        if match:
            print(f"Chatbot: {qa_data[match]}")
        else:
            print("Chatbot: Bu konuda size yardımcı olamıyorum.")

if __name__ == "__main__":
    chatbot()
