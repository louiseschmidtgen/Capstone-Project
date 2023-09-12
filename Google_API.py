from Pop_up_gui import PopUpGUI
import http.client
import json
import sys
import os


class GoogleAPI():
    def __init__(self):
        self.popup = PopUpGUI()

    def get_e2g_translation(self, engl_word):
        """This function calls the translate function to translate its input
        Args:
            engl_word (str): Users input that needs to be translated.

        Returns:
            str: The German translation of the Word.
        """
        return self.translate(engl_word, source_lang="en", target_lang="ger")

    def get_g2e_translation(self, ger_word):
        """This function calls the translate function to translate its input

        Args:
            ger_word (str): Users input that needs to be translated.

        Returns:
            str: The English translation of the Word.
        """
        return self.translate(ger_word, source_lang="ger", target_lang="en")

    def translate(self, word, source_lang, target_lang):
        """This function calls Google API to translate a Word from a given source language to a target language.

        Args:
            word (str): word that should be translated
            source_lang (str): has either value ger/en
            target_lang (str): has either value ger/en
        Returns:
            str: The translation of the Word.
        """
        # get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            # This key is limited to 500 calls/month.
            api_key = str(os.getenv('X_RapidAPI_Key'))
        except Exception as e:
            print(
                "Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            self.popup.createPopUp(
                "Environment variables for Google API not set.")
            sys.exit(1)  # crash

        # establish connection to API host
        conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
        # Hello%2C%20world
        payload = f"q={word}&target={target_lang}&source={source_lang}"

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': api_host,
            'x-rapidapi-key': api_key
        }

        conn.request("POST", "/language/translate/v2", payload, headers)

        res = conn.getresponse()

        status = res.status  # 200 for is found #302 not found
        print(f"status: {status}")

        if status != 200:
            print("Error with Google API: ")
            self.popup.createPopUp(
                f"Error with Google API: Status Code: {status}")
            return ""
        data = res.read()
        # dump it in json # convert result to json/dict#dump it in json # convert result to json/dict
        result_json = json.loads(data.decode("utf-8"))
        print(result_json)
        try:
            # get translation from result
            translation = result_json["data"]["translations"][0]["translatedText"]
        except IndexError:
            print("Key error reading result.")
        print(f"translation: {translation}")
        return translation
