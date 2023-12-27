import pyttsx3

if __name__ == '__main__':
    print("******Welcome to Robo Speaker*********")

    engine = pyttsx3.init()  #initializing an engine to convert text to speech

    while True:
        text = input("Enter what you want me to speak (type 'q' to quit): ")

        if text.lower() == 'q': # if entered text is small q
            break               # then the loop breaks

        engine.say(text)      #else the loop continue with taking inputs
        engine.runAndWait()   #it uses the engine.say() method to convert
                              # the text to speech and the engine.runAndWait()
                              #method to make the program wait until the speech is complete.


