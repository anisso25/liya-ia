import speech_recognition as sr

# Créer un objet Recognizer
recognizer = sr.Recognizer()

# Variable d'état
listening = False

while True:
    with sr.Microphone() as source:
        print("Dites quelque chose...")

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit: {}".format(text))

            # Si l'utilisateur dit "jarvis", activez l'écoute
            if "jarvis" in text.lower():
                print("Activation de l'écoute...")
                listening = True

            # Si l'écoute est activée, traitez les commandes
            if listening:
                try:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(
                        audio, language="fr-FR")
                    print("Commande détectée: {}".format(command))

                    # Traitez la commande ou ajoutez d'autres conditions pour sortir de l'écoute
                    if "arrêt" in command.lower():
                        print("Arrêt de l'écoute.")
                        listening = False

                    # Ajoutez d'autres conditions de commande ici

                except sr.UnknownValueError:
                    print("Google Web Speech API n'a pas pu comprendre l'audio")
                except sr.RequestError as e:
                    print(
                        "Erreur lors de la requête à Google Web Speech API; {0}".format(e))
                    break  # Sortez de la boucle en cas d'erreur de requête

        except sr.UnknownValueError:
            print("Google Web Speech API n'a pas pu comprendre l'audio")
        except sr.RequestError as e:
            print(
                "Erreur lors de la requête à Google Web Speech API; {0}".format(e))
