"""
Equation of Time(eot)
"""
from math import pi, radians, pow, sin, asin, cos

"""
Generates the EoT component caused by eccentricity, parameters like;
(eccentricity, perihelion day/long, orbit period, and number of days)
with returns being list of floats in analemma inches
"""
def generate_eccentricity_component(eccentricity, perihelion_longitude_deg, perihelion_day, orbital_period_days,
                                    day_numbers):
    return generate_equation_of_time(eccentricity, perihelion_longitude_deg, 0, perihelion_day, orbital_period_days,
                                     day_numbers)

"""
Generates EoT component for obliquity, parameters like;
(perihelion long, obliquity, perihelion day, orbit period in days, and number of days)
with returns being float for obliquity in analemma inches
"""
def generate_obliquity_component(perihelion_longitude_deg, axial_tilt_deg, perihelion_day, orbital_period_days,
                                 day_numbers):
    return generate_equation_of_time(0, perihelion_longitude_deg, axial_tilt_deg, perihelion_day, orbital_period_days,
                                     day_numbers)

"""
 Computes the EoT with a fourier adjacent expansion based on axial tilt/eccentricity, with parameters like;
 (eccentricity, perihelion long, axial tilt, day of perihelion, orbital period in days, and number of days)
 with returns being float for EoT values in analemma inches
"""
def generate_equation_of_time(eccentricity, perihelion_longitude_deg, axial_tilt_deg,
                              perihelion_day, orbital_period_days, day_numbers):
    equation_of_time_minutes = []
    minutes_per_radian = (24 * 60) / (2 * pi)
    minutes_to_inches_adjustment = 1.1675675675
    x_axis_analemma_centering_variable = 16.75

    perihelion_longitude_rad = radians(perihelion_longitude_deg)
    axial_tilt_rad = radians(axial_tilt_deg)

    # Component due to obliquity and eccentricity (scaled)
    obliquity_component_base = (axial_tilt_rad / 2) * (1 - 4 * pow(eccentricity, 2))
    tan2_obliquity_base = (1 - cos(2 * obliquity_component_base)) / (1 + cos(2 * obliquity_component_base))
    tan2_axial_tilt = (1 - cos(axial_tilt_rad)) / (1 + cos(axial_tilt_rad))

    # Precompute terms used in Fourier-like expansion
    eccentricity_term_2 = 2 * eccentricity
    ecc_times_tan2 = 2 * eccentricity * tan2_axial_tilt
    tan2_squared_half = 0.5 * pow(tan2_axial_tilt, 2)
    eccentricity_squared = pow(eccentricity, 2)
    ecc_squared_5_4 = (5 / 4) * eccentricity_squared
    ecc_times_tan2_squared = 2 * eccentricity * pow(tan2_axial_tilt, 2)
    ecc_squared_times_tan2_13_4 = (13 / 4) * eccentricity_squared * tan2_axial_tilt
    tan2_cubed_third = (1 / 3) * pow(tan2_axial_tilt, 3)

    for day in day_numbers:
        mean_anomaly_rad = 2 * pi * ((day - perihelion_day) / orbital_period_days)

        # Fourier expansion representing the Equation of Time (EoT)
        eot_minutes = (
                              -(
                                      tan2_obliquity_base * sin(2 * (mean_anomaly_rad + perihelion_longitude_rad))
                                      + eccentricity_term_2 * sin(mean_anomaly_rad)
                                      - ecc_times_tan2 * sin(mean_anomaly_rad + 2 * perihelion_longitude_rad)
                                      + ecc_times_tan2 * sin(3 * mean_anomaly_rad + 2 * perihelion_longitude_rad)
                                      + tan2_squared_half * sin(4 * (mean_anomaly_rad + perihelion_longitude_rad))
                                      + ecc_squared_5_4 * sin(2 * mean_anomaly_rad)
                                      - ecc_times_tan2_squared * sin(
                                  3 * mean_anomaly_rad + 4 * perihelion_longitude_rad)
                                      + ecc_times_tan2_squared * sin(
                                  5 * mean_anomaly_rad + 4 * perihelion_longitude_rad)
                                      + ecc_squared_times_tan2_13_4 * sin(
                                  4 * mean_anomaly_rad + 2 * perihelion_longitude_rad)
                                      + tan2_cubed_third * sin(6 * (mean_anomaly_rad + perihelion_longitude_rad))
                              ) * minutes_per_radian * minutes_to_inches_adjustment
                      ) + x_axis_analemma_centering_variable

        equation_of_time_minutes.append(eot_minutes)

    return equation_of_time_minutes
"""
 Computes solar declination in the year, account for axial tilt/eccentricity, with parameters like;
 (eccentricity, obliquity, orbital period, number of days, perihelion longitude)
 with returns being list of float for solar declination, adjusted for inches
"""
def generate_declination(eccentricity, axial_tilt_deg, orbital_period_days, day_numbers, perihelion_longitude_deg):
    declination_degrees = []
    sin_axial_tilt = sin(radians(axial_tilt_deg))
    deg_per_day = 360 / orbital_period_days
    deg_to_inches_scale = 1.936
    y_axis_analemma_centering_variable = 45.5

    # Phase correction for Earth's orbit eccentricity
    eccentricity_phase_deg = (360 / pi) * eccentricity

    # Shift from perihelion to solstice (longitude)
    days_to_solstice = perihelion_longitude_deg / deg_per_day

    for day in day_numbers:
        day_index = day - 1

        # Approximation of solar declination using axial tilt and orbital phase
        solar_declination_deg = (
                                        -asin(
                                            sin_axial_tilt * cos(
                                                radians(
                                                    deg_per_day * (day_index + (days_to_solstice - 2))
                                                    + eccentricity_phase_deg * sin(
                                                        radians(deg_per_day * (day_index - 2)))
                                                )
                                            )
                                        ) * 360 / (2 * pi)
                                ) * deg_to_inches_scale + y_axis_analemma_centering_variable

        declination_degrees.append(solar_declination_deg)

    return declination_degrees

"""
Computes the EoT and solar declination for the year to produce the analemma, with parameters like;
(eccentricity, perihelion long/dat, obliquity, orbit period, number of days)
return being a 2 list tuple, EoT values being x axis, and Solar declination being y axis
"""
def generate_analemma(eccentricity, perihelion_longitude_deg, axial_tilt_deg,
                      perihelion_day, orbital_period_days, day_numbers):
    declination_degrees = generate_declination(
        eccentricity, axial_tilt_deg, orbital_period_days, day_numbers, perihelion_longitude_deg
    )
    equation_of_time_minutes = generate_equation_of_time(
        eccentricity, perihelion_longitude_deg, axial_tilt_deg,
        perihelion_day, orbital_period_days, day_numbers
    )
    return equation_of_time_minutes, declination_degrees