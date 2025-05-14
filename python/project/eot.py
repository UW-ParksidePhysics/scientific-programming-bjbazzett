"""
Equation of Time(eot)
"""
from math import pi, radians, pow, sin, asin, cos

def generate_eccentricity_component(eccentricity, perihelion_longitude_deg, perihelion_day, orbital_period_days, day_numbers):
    return generate_equation_of_time(eccentricity, perihelion_longitude_deg, 0, perihelion_day, orbital_period_days, day_numbers)

def generate_obliquity_component(perihelion_longitude_deg, axial_tilt_radians, perihelion_day, orbital_period_days, day_numbers):
    return generate_equation_of_time(0, perihelion_longitude_deg, axial_tilt_radians, perihelion_day, orbital_period_days, day_numbers)

def generate_equation_of_time(eccentricity, perihelion_longitude_deg, axial_tilt_deg,
                               perihelion_day, orbital_period_days, day_numbers):
    equation_of_time_minutes = []
    minutes_per_radian = (24 * 60) / (2 * pi)

    perihelion_longitude_rad = radians(perihelion_longitude_deg)
    axial_tilt_rad = radians(axial_tilt_deg)

    t1 = (axial_tilt_rad / 2) * (1 - 4 * pow(eccentricity, 2))
    tan2_half_t1 = (1 - cos(2 * t1)) / (1 + cos(2 * t1))
    tan2_axial = (1 - cos(axial_tilt_rad)) / (1 + cos(axial_tilt_rad))

    eccentricity_times_2 = 2 * eccentricity
    e_tan2 = 2 * eccentricity * tan2_axial
    tan2_squared_half = 0.5 * pow(tan2_axial, 2)
    eccentricity_squared = pow(eccentricity, 2)
    eccentricity_squared_5_4 = (5 / 4) * eccentricity_squared
    e_tan2_squared = 2 * eccentricity * pow(tan2_axial, 2)
    e_squared_tan2_13_4 = (13 / 4) * eccentricity_squared * tan2_axial
    tan2_cubed_third = (1 / 3) * pow(tan2_axial, 3)

    for day in day_numbers:
        mean_anomaly = 2 * pi * ((day - perihelion_day) / orbital_period_days)
        equation = (
            -(
                tan2_half_t1 * sin(2 * (mean_anomaly + perihelion_longitude_rad))
                + eccentricity_times_2 * sin(mean_anomaly)
                - e_tan2 * sin(mean_anomaly + 2 * perihelion_longitude_rad)
                + e_tan2 * sin(3 * mean_anomaly + 2 * perihelion_longitude_rad)
                + tan2_squared_half * sin(4 * (mean_anomaly + perihelion_longitude_rad))
                + eccentricity_squared_5_4 * sin(2 * mean_anomaly)
                - e_tan2_squared * sin(3 * mean_anomaly + 4 * perihelion_longitude_rad)
                + e_tan2_squared * sin(5 * mean_anomaly + 4 * perihelion_longitude_rad)
                + e_squared_tan2_13_4 * sin(4 * mean_anomaly + 2 * perihelion_longitude_rad)
                + tan2_cubed_third * sin(6 * (mean_anomaly + perihelion_longitude_rad))
            ) * minutes_per_radian * 1.1675675675
        ) + 16.75
        equation_of_time_minutes.append(equation)
    return equation_of_time_minutes
#the minor adjustments at the end are to change the degrees to inches, then offset to align the widest/tallest parts of the analemma with 0 for x,y

def generate_declination(eccentricity, axial_tilt_deg, orbital_period_days, day_numbers, perihelion_longitude_deg):
    declination_degrees = []
    sin_axial_tilt = sin(radians(axial_tilt_deg))
    deg_per_day = 360 / orbital_period_days
    eccentricity_phase_correction = (360 / pi) * eccentricity
    days_between_perihelion_and_solstice = perihelion_longitude_deg / deg_per_day

    for day in day_numbers:
        day_offset = day - 1
        declination = (
            -asin(
                sin_axial_tilt * cos(
                    radians(
                        deg_per_day * (day_offset + (days_between_perihelion_and_solstice - 2))
                        + eccentricity_phase_correction * sin(radians(deg_per_day * (day_offset - 2)))
                    )
                )
            ) * 360 / (2 * pi)
        ) * 1.936 + 45.5
        declination_degrees.append(declination)
    return declination_degrees

def generate_analemma(eccentricity, perihelion_longitude_deg, axial_tilt_deg,
                      perihelion_day, orbital_period_days, day_numbers):
    declination_degrees = generate_declination(eccentricity, axial_tilt_deg, orbital_period_days,
                                               day_numbers, perihelion_longitude_deg)
    equation_of_time_minutes = generate_equation_of_time(eccentricity, perihelion_longitude_deg, axial_tilt_deg,
                                                         perihelion_day, orbital_period_days, day_numbers)
    return equation_of_time_minutes, declination_degrees