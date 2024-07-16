import openai
from elevenlabs import GenerationConfig, play

# Set your API keys here
openai.api_key = "sk-proj-5MtJNwQ9l9lZDTsew4rMT3BlbkFJLy7GOWix6YztDmhTgEJX"
elevenlabs_api_key = "4f215a4c3e4731e0a73e4ac5d19490fa"

# Set up ElevenLabs API
from elevenlabs import set_api_key
set_api_key(elevenlabs_api_key)

def ask_question():
    while True:
        # Ask for user input
        question = input("Enter your question (or type 'exit' to quit): ")

        if question.lower() == 'exit':
            print("Goodbye!")
            break

        # Send the question to OpenAI for response generation
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 1000 characters.'},
                {"role": "user", "content": question}
            ]
        )

        answer = response['choices'][0]['message']['content']
        print("\nAI:", answer)

        # Convert the response to audio and play it
        audio = generate(
            text=answer,
            voice="Bella"  # You can choose a different voice if desired
        )

        # Play the audio
        play(audio)

if __name__ == "__main__":
    ask_question()
