import json
from time import sleep

from ecosystem import Ecosystem
from faction import Faction
import matplotlib.pyplot as plt


class Game():

    def __init__(self, init_year=2019):
        self.init_year = init_year
        self.end_year = 2080

        self.faction = Faction(init_year)
        self.ecosystem = Ecosystem(0, init_year) 
        self.templist = []
    

    def play(self):
        for year in range(self.init_year, self.end_year):
            with open('data.text') as json_file:
                data = json.load(json_file)
                coal_year = data['coal']
                traffic_year = data['traffic']

            print('coal', coal_year)
            print(year)
            # model = self.fraction.get_current_state()
            # temp = self.ecosystem.perform_timestep(model, year)

            # self.ecosystem.update_co2()
            # print(self.ecosystem.current_CO2_concentration())
            # print('temp' ,self.ecosystem.temp_from_currentCO2())

            self.faction.compute_velocity()
            faction_emission = self.faction.compute_additional_co2_emission()
            self.ecosystem.update_co2(faction_emission)
            print('tem', self.ecosystem.temp_from_currentCO2())
            temp = self.ecosystem.temp_from_currentCO2()

            if coal_year is not None and traffic_year is not None:
                print(coal_year)
                self.faction.update_co2_acc('Kohlekraft', int(coal_year))
                self.faction.update_co2_acc('Traffic', int(traffic_year))

                data={}
                data['coal'] = None
                data['traffic'] = None
                
                with open('data.text','w') as outfile:
                    json.dump(data,outfile)

            # self.ecosystem.get_copernicus_data(self.init_year ,year)
            self.templist.append(temp)
            plt.plot(self.templist)
            plt.savefig('plot_temp.png')
            # plt.show()

            data = {}
            data['temp'] = temp
            data['year'] = year
            data['plot_temp'] = 'plot_temp.png'
            with open('output_game.txt', 'w') as outfile:
                json.dump(data, outfile)

            sleep(10)
