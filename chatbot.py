import json
from difflib import get_close_matches

def chatbot():
    # Load the JSON data
    file_path = "chatbot_hr_discussion.json"  # Ensure the file is in the same directory
    with open(file_path, "r", encoding="utf-8") as file:
        qa_data = json.load(file)
    
    print("Chatbot: Merhaba! Size nasıl yardımcı olabilirim? (Çıkmak için 'çık' yazabilirsiniz.)")
    
    while True:
        # Get user input
        user_input = input("Kullanıcı: ").strip()
        
        # Exit condition
        if user_input.lower() == "çık":
            print("Chatbot: Görüşmek üzere!")
            break
        
        # Check for an exact match in the JSON data
        if user_input in qa_data:
            print(f"Chatbot: {qa_data[user_input]}")
        else:
            # Try to find the closest match using a similarity metric
            closest_matches = get_close_matches(user_input, qa_data.keys(), n=1, cutoff=0.6)
            
            if closest_matches:
                # Provide the response for the closest match
                print(f"Chatbot: {qa_data[closest_matches[0]]}")
            else:
                # Default response for unknown inputs
                print("Chatbot: Bu konuda size yardımcı olamıyorum.")

if __name__ == "__main__":
    chatbot()
