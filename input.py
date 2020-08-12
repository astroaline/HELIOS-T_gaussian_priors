import numpy as np
import os

## Constants ##

kboltz = 1.38064852e-16    # Boltzmann's constant
amu = 1.660539040e-24      # atomic mass unit
gamma = 0.57721
rjup = 7.1492e9            # equatorial radius of Jupiter
rsun = 6.9566e10           # solar radius
rearth = 6.378e8            # earth radius
pressure_probed = 1e-2      # probed pressure in bars
# pressure_cia = 1e-2         # pressure for cia in bars
# m = 2.4*amu                 # assummed hydrogen-dominated atmosphere
m_water = 18.0*amu          # mean molecular mass of any molecules you want to consider
m_cyanide = 27.0*amu
m_ammonia = 17.0*amu


## Planet Data ##

planet_name = 'TRAPPIST-1g'

g = 854
g_uperr = 39
g_loerr = 38
g_uncertainty = (g_uperr+g_loerr)/2
rstar = 0.121
rstar_uncertainty = 0.003
r0 = 0.09580
r0_uncertainty = 0.09

wavelength_bins = np.array([1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65]) # must be 1 longer than transit_depth and transit_depth_error
transit_depth = np.array([0.7805000000000001,0.7742,0.7888000000000001,0.7771,0.774,0.7851,0.7808,0.7305,0.7711,0.778])
transit_depth_error = np.array([0.035,0.033100000000000004,0.030600000000000002,0.034,0.0396,0.0436,0.0376,0.0332,0.034800000000000005,0.0303])




## Retrieval info ##

molecules = ['01']  # list of molecules (determines which opacity tables are loaded)
parameters = ["T", "log_xh2o", "log_kappa_cloud", "log_P0", "Rstar", "G"]   # parameters you wish to retrieve (MUST MATCH MOLECULES)
res = 5         # resolution used for opacities
live = 1000     # live points used in nested sampling
wavenumber=True     # True if opacity given in terms of wavenumber, False if wavelength

priors = {"T": [2800, 100], "log_xh2o": [13,-13], "log_xhcn": [13,-13], "log_xnh3": [13,-13], "log_kappa_cloud": [14,-12],
          "log_P0": [4,-1], "log_kappa_0": [9,-10], "Q0": [99,1], "a": [3,3],
          "log_r_c": [6,-7], "log_p_cia": [3,-3], "Rstar": [2*rstar_uncertainty,rstar-rstar_uncertainty], "G": [g_uperr+g_loerr,g-g_loerr]} # priors for all possible parameters



## info for all possible parameters ##
molecular_abundance_dict = {"01":"log_xh2o", "23":"log_xhcn", "11":"log_xnh3"}  # dictionary list of all possible molecules and corresponding abundance names

parameter_dict = {"T": 1000, "log_xh2o": "Off", "log_xhcn": "Off", "log_xnh3": "Off", "log_kappa_cloud": "Off", "R0": r0, "Rstar": rstar,
                  "log_P0": 1, "log_kappa_0": "Off", "Q0": "Off", "a": "Off", "log_r_c": "Off", "log_p_cia": -2, "G": g}    # default parameter values used if not retrieved

molecular_mass_dict = {"01": m_water, "23": m_cyanide, "11": m_ammonia}   # dictionary of molecules and their mean molecular masses
temperature_array = np.r_[50:700:50, 700:1500:100, 1500:3100:200]
temp_dict = {'01': temperature_array, '23': temperature_array, '11': temperature_array[:22]}   # temperature values for corresponding opacity tables
temperature_array_cia = np.r_[200:3025:25]          # temperature array for CIA table
opacity_path = os.environ['HOME'] + "/Desktop/PhD/EXOMOL/"  # path to opacity binary files
cia_path = os.environ['HOME'] + "/Desktop/PhD/HITRAN/"      # path to CIA files

