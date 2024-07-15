import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine
    
    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)   
        self.engine.setProperty('volume', volume) 
        
    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]
        
        for i, voice in enumerate(voices[0]):
             print(f'{i+ 1} {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [{voice.id}]')
             
             
             
    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text) 
        print('I am speaking')     
        
        if save:
            self.engine.save_to_fike(text, file_name)
            
        self.engine.runAndWait()     
     
     
     
     
     
             
                
if __name__ == '__main__':
     tts = TextToSpeech(None, 200, 1.0)
     tts.text_to_speech('The solar system has one star, eight planets, five dwarf planets, at least 290 planetary moons, about 1.4 million asteroids, and about 4,000 comets (including fragments). Our solar system is located in the Milky Way, a barred spiral galaxy with two major arms, and two minor arms')