import pandas as pd
import numpy as np

if __name__ == "__main__":
    power_plants = pd.read_csv("/Users/b1017579/Documents/PhD/Projects/11-carbon_optimiser/data/raw/power_plants_2018.csv")
    
    power_plants.Capacity = pd.to_numeric(power_plants.Capacity.str.replace(",",""))
    power_plants = power_plants[power_plants.Capacity>0]

    power_plants['Simplified_Type'] = power_plants['Fuel'].map(lambda x: "Coal" if "Coal" in x else "PV" if "PV" in x else "EfW" if "EfW" in x
                                          else "AD" if "AD" in x else "ACT" if "ACT" in x else "Offshore" if "Offshore" in x
                                        #   else "Biomass" if "Biomass" in x else "Conversions" if "Conversions" in x 
                                          else "Onshore" if "Onshore" in x else "Landfill" if "Landfill" in x
                                          else "Sewage" if "Sewage" in x else "Geothermal" if "Geothermal" in x 
                                          else "Hydro_Store" if all(check in x for check in ['Hydro','Store'])
                                          else "Hydro" if "Hydro" in x
                                          else "Wave" if "Wave" in x else "Tidal" if "Tidal" in x 
#                                           else "OCGT_2000hr" if all(check in x for check in ["OCGT", "2000"]) 
                                          else "OCGT" if all(check in x for check in ["OCGT", "2000"]) 
                                          else "OCGT_500hr" if all(check in x for check in ["OCGT", "500"])
                                          else "CCGT" if "CCGT" in x
                                          else "OCGT" if "OCGT" in x
                                          else "Recip_gas" if "Recip Gas" in x else "Recip_gas" if "RECIP GAS" in x else "Nuclear" if "Nuclear" in x 
                                          else "Pumped_storage" if "Pumped" in x
                                          else "PV" if "Solar" in x else "Recip_diesel" if "Recip Diesel" in x 
                                          else "Onshore" if "Wind" in x
                                          else "Offshore" if "Wind (offshore)" in x
                                          else "EfW" if "Waste" in x
                                          else "Recip_diesel" if "Diesel" in x
                                          else "Biomass_wood" if "Biomass_wood" in x
                                          else "Biomass_poultry_litter" if "Biomass_poultry_litter" in x
                                          else "Recip_gas" if "Gas"
                                          else "Recip_gas" if "Gas oil"
                                          else "")


    power_plants.Company = power_plants.Company.str.replace("Scottish Power", "Scottish power")
    northern_ireland = power_plants[power_plants.Location=="Northern Ireland"]
    northern_ireland_sum = northern_ireland.Capacity.sum()
    print("Northern Ireland Capacity: {}".format(northern_ireland_sum))

    northern_ireland.drop('Location', axis=1)
    northern_ireland.to_csv('/Users/b1017579/Documents/PhD/Projects/11-carbon_optimiser/data/processed/power_plants/northern_ireland_plants.csv')

    scotland = power_plants[power_plants.Location=="Scotland"]
    scotland_sum = scotland.Capacity.sum()
    print("Scotland Capacity: {}".format(scotland_sum))
    scotland.drop('Location', axis=1)
    scotland.to_csv('/Users/b1017579/Documents/PhD/Projects/11-carbon_optimiser/data/processed/power_plants/scotland_plants.csv')
