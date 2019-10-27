# import cdsapi
# import cdstoolbox as ct
import numpy as np
import h5py as h5
import matplotlib.pyplot as plt 

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
        #print(years_diff)
        return 326.675+1.48262*((years_diff/10)**(2.3))

    def temp_from_currentCO2(self):
        temp = 285.8 - 273.15 + 3.92 * 0.3 * 5.35 *np.log(self.co2_concentration/278)
        return temp

    def update_co2(self, faction_emission):
        #per year
        self.co2_concentration += faction_emission
        print(self.co2_concentration, 'co2 concentration')

    def compare_copernicus_data(self, first_year,end_year, year,temp_diff, temperatures):
        data = h5.File(self.path, 'r')
        year = year - 2006
        diff = np.zeros(4)
        i = 0
        key_m = {'bla':None}
        plotdata = np.zeros(end_year - first_year)

        temperatures = np.append(temperatures,temperatures[-1] + temp_diff)

        time = np.arange(first_year,end_year)
        fig, ax = plt.subplots(figsize=(12,8))

        for keys in data:

            if year == first_year:
                diff[i] = 0

            else:
                diff[i] = data[keys][1, year] - data[keys][1, year-1]
                if (np.abs(diff[i] - temp_diff) < np.abs(diff[i-1] - temp_diff) and i > 0 ):  
                    key_m['bla'] = keys

            for j in range(end_year - first_year):
                plotdata[j] = data[keys][1,j] - 273.15


            i = i + 1
            
            ax.plot(time,plotdata,label=keys)

        ax.plot(time[0:len(temperatures)],temperatures[0:len(temperatures)],'k-',label='your trajectory')
        ax.set_xlabel('time in years',fontsize=14)
        ax.set_ylabel(r'temperature in $^{\circ} \  C $',fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        ax.legend(fontsize=14)
        plt.title('mean surface temperature per year',fontsize=14)
        fig.savefig('temp_plots.png')
          
        











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

