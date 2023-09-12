import os
from Google_API import GoogleAPI


def main():
    # set environ
    # export variables to environment for google api
    os.environ["X_RapidAPI_Host"] = "google-translate1.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"] = '9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc'
    google_api = GoogleAPI()
    # test 1
    # google_api.translate("Sky", source_lang="en", target_lang="ger")
    # result: Himmel
    # test 2
    # google_api.translate("Himmel", source_lang="en", target_lang="ger")
    # result: Himmel
    # google_api.translate("Häuser", source_lang="ger", target_lang="en")
    # result: Huser
    # google_api.translate("Haeuser", source_lang="ger", target_lang="en")
    # result: Houses
    # google_api.translate("Blumentrauß", source_lang="ger", target_lang="en")
    # result: bouquet of flowers
    # google_api.translate("Blumentrauss", source_lang="ger", target_lang="en")
    # result: bouquet
    google_api.translate("Übergrößengeschäft",
                         source_lang="de", target_lang="en")
    # result: mountain business
    google_api.translate("Uebergroeßengeschaeft",
                         source_lang="de", target_lang="en")
    # result: Huge closeness
    google_api.translate("Käsesoßenrührlöffel",
                         source_lang="de", target_lang="en")
    # result: K seso enr hrl ffel
    google_api.translate("Kaesesoßenruehrloeffel",
                         source_lang="de", target_lang="en")
    # result: Cheese stirrer spoon


main()
