
from geniusgermanapp.Pop_up_gui import PopUpGUI


class GermanHolidaysController():
    def __init__(self, dashboard_controller):
        self.dashboard_controller = dashboard_controller
        self.holidaysdict = {
            "Carnival": ["Carnival is a traditional German celebration occuring between 11 November at 11:11a.m. and Ash Wednesday. \
                It is also known as Fasching or Fastnacht. During the carnival parades people wear masks and costumes and have a good time.", "url"],
            "Christmas": ["Christmas celebrations start on the 24th of December when gifts are exchanged. \
                Leading up to Christmas is the Advent celebration where each sunday before Christmas a new candle is lit. \
                The fourth one is lit on Christmas Eve. During the Christmas time Christmas markets sell traditional German delicatessen and decorations", "url"],
            "Oktoberfest": ["Oktoberfest celebrations take place between the end of September and the beginning of Oktober. \
                The biggest Oktoberfest takes place in Munich. It is the world's largest Volksfest. This festival includes a lot of beer and a funfair.", "url"],
            "NationalUnity": ["The German Unity Day is celebrated on the 3rd of October as a public holiday. \
                It commemorates the German reunification in 1990 of east and west Germany.", "url"],
            "HolocaustMemorial": ["This Memorial day is on the 27th of February. This date remembers the liberation of the concentration camp Auschwitz in the year 1945. \
                On this day the victims of the NS regime are remembered.", "url"],
        }
        self.popup = PopUpGUI()
    def display_pop_up_with_info_on_holiday(self, holiday):
        info = self.holidaysdict[holiday][0]
        img_url = self.holidaysdict[holiday][0]        
        self.popup.create_pop_up_with_picture(info, img_url)
        
        
