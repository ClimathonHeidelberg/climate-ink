import cdsapi
import cdstoolbox as ct

class Ecosystem():
    def __init__(self, model, year):
        self.year = year
        self.catastrophy = Catastrophy()
        self.model = model
        self.client = cdsapi.Client()
        

    def get_cds_data(self):
        if self.model == 0:
            file = ct.catalogue.retrieve(
            'projections-cmip5-monthly-single-levels',
            {
                'ensemble_member':'r1i1p1',
                'format':'zip',
                'experiment':'rcp_8_5',
                'variable':'2m_temperature',
                'period':'203601-204012',
                'model':'gfdl_esm2g'
            })

            print(file)


    def perform_timestep(self, model):
        if self.model != model:
            self.model = model
            self.get_cds_data()


class Catastrophy():
    def __init__(self):
        pass


    def check_catastrophy(self, temp):
        pass


