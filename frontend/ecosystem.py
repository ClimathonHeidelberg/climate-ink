# import cdsapi
# import cdstoolbox as ct
import numpy as np
import h5py as h5

class Ecosystem():
    def __init__(self, model, year):
        self.year = year
        self.catastrophy = Catastrophy()
        self.model = model
        # self.client = cdsapi.Client()
        self.dict_temp = {'2019': 1.0, '2020': 1.1, '2021':1.2, '2022':1.2, '2023':1.3, '2024':1.5, '2025':1.6, '2026':1.9}
        self.co2_concentration = self.init_CO2_concentration()
        self.path = 'data.h5'

    def get_cds_data(self):
        if self.model == 0:

            temp = self.dict_temp[str(self.year)]
            self.catastrophy.check_catastrophy(temp)


    def perform_timestep(self, model, year):
        self.year = year
        if self.model != model:
            self.model = model
        self.get_cds_data()

    def init_CO2_concentration(self):
        years_diff = int(self.year) - 1970
        print(years_diff)
        return 326.675+1.48262*((years_diff/10)**(2.3))

    def temp_from_currentCO2(self):
        temp_increase_from_preindustrial_lvls=0.3*5.35*np.log(self.co2_concentration/278)
        return temp_increase_from_preindustrial_lvls

    def update_co2(self, faction_emission):
        #per year
        self.co2_concentration += faction_emission
        print(self.co2_concentration, 'co2 concentration')

    def get_copernicus_data(self, first_year, year):
        data = h5.File(self.path, 'r')
        year = year - 2006
        for keys in data:
            if year == first_year:
                diff = 0
            else:
                diff = data[keys][1, year] - data[keys][1, year-1]
            print(diff)

            # print(data[keys][1, year] - 273.15)


class Catastrophy():
    def __init__(self):
        pass

    def check_catastrophy(self, temp):
        # proba = 1/(1+ np.exp(-10 (temp - 1.8) ))
        proba = 1/(1+np.exp(-10 *(temp -1.8 ) ))
        is_happening = np.random.uniform() < proba
        # print(proba, is_happening)
        # return proba, is_happening

    def check_ExtremeWeather(self, temp):
        proba = 0.1+ temp*0.4/15
        is_happening = np.randum.uniform() < probas

