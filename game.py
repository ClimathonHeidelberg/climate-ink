from time import sleep
import json
import numpy as np
from faction import Faction
from ecosystem import Ecosystem


class Game():

    def __init__(self, init_year):
        self.init_year = init_year
        self.end_year = 2080
        self.faction = Faction(init_year)
        self.ecosystem = Ecosystem(0, init_year) 
    

    def play(self):
    	temperatures = np.array([])
    	for year in range(self.init_year, self.end_year):
            # with open('input.txt') as json_file:
            #     data = json.load(json_file)
            #     model = data['model']

            #print(year)
            # model = self.fraction.get_current_state()
            # temp = self.ecosystem.perform_timestep(model, year)

            # self.ecosystem.update_co2()
            # print(self.ecosystem.current_CO2_concentration())
            # print('temp' ,self.ecosystem.temp_from_currentCO2())

            #self.faction.update_co2_acc('Kohlekraft', 10)
            #self.faction.update_co2_acc('Traffic', 20)


            self.faction.compute_velocity()
            faction_emission = self.faction.compute_additional_co2_emission()

            

            T1 = self.ecosystem.temp_from_currentCO2()
            temperatures = np.append(temperatures,T1)
            self.ecosystem.update_co2(faction_emission)
            T2 = self.ecosystem.temp_from_currentCO2()
            
            
                
            self.ecosystem.compare_copernicus_data(self.init_year ,self.end_year, year, T2 - T1, temperatures)


            # data = {}
            # data['temp'] = temp
            # data['plot_temp'] = 'plot_temp.png'
            # with open('output.txt', 'w') as outfile:
            #     json.dump(data, outfile)

            # sleep(10)


init_year = 2006

game = Game(init_year)
game.play()
