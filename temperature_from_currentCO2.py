def temperature_from_currentCO2(currentCO2_concentration):
    temperature_increase_from_preindustrial_levels=4*0.3*5.35*ln(currentCO2_concentration/278)
    return temperature_increase_from_preindustrial_levels
