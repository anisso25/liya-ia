import speech_recognition as sr
import openai

# Assurez-vous que votre clé API OpenAI GPT est correctement configurée
openai.api_key = "04064b770955c32f56f17d1e2084be4d"


def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

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
            # Convertir l'audio en texte
            text = recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit: {}".format(text))

            # Si l'écoute est activée, envoyer la question à ChatGPT
            if listening:
                chat_response = chat_with_gpt(text)
                print("Réponse de ChatGPT: {}".format(chat_response))

            # Activer l'écoute si nécessaire
            if "début" in text.lower():
                print("Activation de l'écoute...")
                listening = True

        except sr.UnknownValueError:
            print("Google Web Speech API n'a pas pu comprendre l'audio")
        except sr.RequestError as e:
            print(
                "Erreur lors de la requête à Google Web Speech API; {0}".format(e))
            break  # Sortir de la boucle en cas d'erreur de requête