import numpy as np
import h5py

class Faction():
    def __init__(self, year):
        self.budget = self.get_budget()
        self.year = year 
        #acc = input
        self.sector = {'Kohlekraft': [0.7, 0.5], 'Traffic': [0.2, 0.5]}
        self.output_generator = {'Kohlekraft':[0, 0], 'Traffic':[0, 0]}

        init_co2_vel = self.init_CO2_vel() 
        init_co2_acc = self.init_CO2_acc()

        for key in self.output_generator:
            self.output_generator[key][0] = init_co2_vel * self.sector[key][0]
            self.output_generator[key][1] = init_co2_acc * self.sector[key][1]

    def get_decision(self):
        pass

    def update(self):
        pass

    def get_budget(self):
        return 100

    def get_current_state(self):

        rcp_model = 1

        return rcp_model 

    def compute_velocity(self):
        #every loop
        for key in self.output_generator:
            self.output_generator[key][0] = self.output_generator[key][0] + self.output_generator[key][1] * 1
            if self.output_generator[key][0] <= 1e-06:
                self.output_generator[key][1] = 0
                self.output_generator[key][0] = 0
        print(self.output_generator)

    def compute_additional_co2_emission(self):
        out = np.sum((self.output_generator['Kohlekraft'][0], self.output_generator['Traffic'][0]))
        return out

    def init_CO2_vel(self):
        years_diff = int(self.year) - 1970
        return 3.41/10*(years_diff/10)**(1.3)

    def init_CO2_acc(self):
        years_diff = int(self.year) - 1970
        return 3.41*1.3/100*(years_diff/10)**0.3

    def update_co2_acc(self, name, user_input):
        self.output_generator[name][1] = - self.output_generator[name][0] / user_input
