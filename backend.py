import openai

class Chatbot:
    def __init__(self):
        openai.api_key = ''
        
    def get_response(self, user_input):
        response =  openai.Completion.create(
            engine = "gpt-3.5-turbo",
            prompt = user_input,
            max_tokens = 2000,
            temperature=0.5,
        ).choice[0].text
        return response
    
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response('Tell me a joke')
    print(response)