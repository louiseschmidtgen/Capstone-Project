from Pop_up_gui import PopUpGUI
import requests
import json
import os


class GoogleAPI():
    def __init__(self):
        self.popup = PopUpGUI()
        self.api_host = str(os.getenv('X_RapidAPI_Host'))
        self.api_key = str(os.getenv('X_RapidAPI_Key'))

    def get_e2g_translation(self, engl_word):
        """This function calls the translate function to translate its input   """
        return self.translate(engl_word, source_lang="en", target_lang="de")

    def get_g2e_translation(self, ger_word):
        """This function calls the translate function to translate its input """
        return self.translate(ger_word, source_lang="de", target_lang="en")

    def translate(self, word, source_lang, target_lang):
        """This function calls Google API to translate a Word from a given source language to a target language. """
        if not self.api_host or not self.api_key:
            print("Environment variables for Google API not set.")
            return None

        # url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        # payload = {
        #     "source": source_lang,
        #     "target": target_lang,
        #     "q": word
        # }

        # headers = {
        #     'content-type': "application/x-www-form-urlencoded",
        #     'Accept-Encoding': "application/gzip",
        #     'X-RapidAPI-Key': self.api_host,
        #     'X-RapidAPI-Host': self.api_key
        # }
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = {
            "source": source_lang,
            "target": target_lang,
            "q": word
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        try:
            print(">>>>>>>>>>>>>>", payload, headers)
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            print(">>>>>>>>>>>>>>", response.text,
                  response.status_code, response.url)
            result_json = response.json()

            translations = result_json.get("data", {}).get("translations", [])

            if translations:
                translation = translations[0]["translatedText"]
                return translation
            else:
                print("Translation not found in response.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error with Google API: {e}")
            self.popup.createPopUp(f"Error with Google API: {e}")
            return None

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            self.popup.createPopUp(f"Error decoding JSON response: {e}")
            return None
