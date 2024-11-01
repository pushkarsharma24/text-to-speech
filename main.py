import openai
from elevenlabs import generate, play, set_api_key, get_voices

# Set your API keys here


# Set up ElevenLabs API
set_api_key(elevenlabs_api_key)

def list_voices():
    voices = get_voices(api_key=elevenlabs_api_key)
    print("Available voices:")
    for voice in voices:
        print(f"Voice: {voice['name']}, ID: {voice['id']}")



def ask_question():
    while True:
        
        question = input("Enter your question or type exit: ")

        if question.lower() == 'exit':
            print("Goodbye!")
            break

       
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 1000 characters.'},
                {"role": "user", "content": question}
            ]
        )

        answer = response['choices'][0]['message']['content']
        print("\nAI:", answer)

        audio = generate(
            text=answer,
            voice="pNInz6obpgDQGcFmaJgB",  
            api_key=elevenlabs_api_key  
        )

       
        with open("response.wav", "wb") as f:
            f.write(audio)

        
        os.system("start response.wav") 
        

if __name__ == "__main__":
    ask_question()
