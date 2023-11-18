import speech_recognition as sr
import requests
from datetime import datetime

# Clé API OpenWeatherMap (obtenez la vôtre sur https://openweathermap.org/)
api_key = "04064b770955c32f56f17d1e2084be4d"

# Fonction pour obtenir l'heure actuelle


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

# Fonction pour obtenir la météo par ville


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "lang": "fr", "units": "metric"}
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if "weather" not in weather_data:
        return f"Impossible d'obtenir les données météorologiques pour {city}."

    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    return f"La météo à {city} est {description}. La température est d'environ {temperature} degrés Celsius."


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

            # Si l'écoute est activée, traitez la commande
            if listening:
                # Ajoutez cette ligne pour déboguer
                print("Commande audio: {}".format(text))

                if "arrêt" in text.lower():
                    print("Arrêt de l'écoute.")
                    listening = False
                    break  # Sortez de la boucle

                elif "quelle heure est-il" in text.lower():
                    current_time = get_current_time()
                    print("Il est actuellement {}".format(current_time))

                elif "comment est la météo à" in text.lower():
                    city = text.split("comment est la météo à")[-1].strip()
                    weather_response = get_weather(city)
                    print(weather_response)

                    # Ajoutez une vérification pour décider d'arrêter ou continuer
                    if "Impossible d'obtenir les données météorologiques" in weather_response:
                        print("Arrêt de l'écoute.")
                        listening = False
                        break

            # Activez l'écoute si nécessaire
            if "début" in text.lower():
                print("Activation de l'écoute...")
                listening = True

        except sr.UnknownValueError:
            print("Google Web Speech API n'a pas pu comprendre l'audio")
        except sr.RequestError as e:
            print(
                "Erreur lors de la requête à Google Web Speech API; {0}".format(e))
            break  # Sortez de la boucle en cas d'erreur de requête
