from Pop_up_gui import PopUpGUI
import http.client
import json
import sys
import os

class GoogleAPI():
    def __init__(self):
        self.popup = PopUpGUI()
        
    def get_e2g_translation(self, engl_word):
        return self.translate(engl_word, source_lang="en", target_lang="ger")
    
    def get_g2e_translation(self, ger_word):
        return self.translate(ger_word, source_lang="ger", target_lang="en") 
    
    def translate(self, word, source_lang, target_lang):
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls/month.
        except Exception as e:
            print("Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            self.popup.createPopUp("Environment variables for Google API not set.")
            sys.exit(1) #crash
            
        #establish connection to API host   
        conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
        #Hello%2C%20world
        payload = f"q={word}&target={target_lang}&source={source_lang}"

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': api_host,
            'x-rapidapi-key': api_key
            }

        conn.request("POST", "/language/translate/v2", payload, headers)

        res = conn.getresponse()
        status = res.status # 200 for is found #302 not found
        print(f"status: {status}")
        
        if status != 200:
            print("Error with Google API: ")
            self.popup.createPopUp(f"Error with Google API: Status Code: {status}")
            return ""
        data = res.read()    
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json # convert result to json/dict
        print(result_json)
        try:
            translation = result_json["data"]["translations"][0]["translatedText"] #get translation from result
        except IndexError:
            print("Key error reading result.")
        print(f"translation: {translation}")
        return translation
            