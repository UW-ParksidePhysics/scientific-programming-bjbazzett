"""
Equation of Time(eot)
"""
from math import pi, radians, pow, sin, asin, cos

def ecc_gen(eccentricity, p, peri_day, orb_per, day_nums):
  return eot_gen(eccentricity, p, 0, peri_day, orb_per, day_nums)

def obl_gen(p, axis_norm_rads, peri_day, orb_per, day_nums):
  return eot_gen(0, p, axis_norm_rads, peri_day, orb_per, day_nums)

def eot_gen(e, p_degs, axis_norm_degs, peri_day, orb_per, day_nums):
  eot_mins = []
  time_mins = (24 * 60) / (2 * pi)
  p = radians(p_degs)
  axis_norm_rads = radians(axis_norm_degs)
  t1 = (axis_norm_rads/2)*(1-4*pow(e, 2))
  tan2_1_4e2 = (1-cos(2*t1)) / (1+cos(2*t1))
  tan2 = (1-cos(axis_norm_rads)) / (1+cos(axis_norm_rads))
  e2 = 2*e
  tan2_2e = 2*e*tan2
  tan4_1_2 = (1/2)*pow(tan2, 2)
  e2_5_4 = (5/4)*(pow(e, 2))
  tan4_2e = 2*e*pow(tan2, 2)
  tan2_2e_13_4 = (13/4)*(pow(e, 2))*tan2
  tan6_1_3 = (1/3)*pow(tan2, 3)
  for d in day_nums:
    m = 2 * pi * ((d - peri_day) / orb_per)
    eot_mins.append(((-(tan2_1_4e2 * sin(2 * (m + p)) + e2 * sin(m) -
                      tan2_2e * sin(m + 2 * p) + tan2_2e * sin(3 * m + 2 * p) +
                      tan4_1_2 * sin(4 * (m + p)) + e2_5_4 * sin(2 * m) - tan4_2e * sin((3 * m) + (4 * p)) +
                      tan4_2e * sin((5 * m) + (4 * p)) + tan2_2e_13_4 * sin(4 * m + 2 * p) +
                      tan6_1_3 * sin(6 * (m + p))) * time_mins) * 1.1675675675) + 16.75)
  return eot_mins



def dec_gen(eccentricity, axis_norm_degs, orb_per, day_nums, p_degs):
  dec_degs = []
  sin_axis_norm = sin(radians(axis_norm_degs))
  ratio360 = 360 / orb_per
  ratio_pi_e = (360 / pi) * eccentricity
  days_btw_peri_solst = p_degs / ratio360

  for d in day_nums:
      d_offset = d - 1
      dec_degs.append(((-(asin(sin_axis_norm *
                             cos(radians(ratio360*(d_offset+(days_btw_peri_solst-2)) +
                                 ratio_pi_e*sin(radians(ratio360*(d_offset-2))))))*360/(2*pi))) * 1.936) + 45.5)
  return dec_degs

def analemma_gen(eccentricity, p_degs, axis_norm_degs, peri_day, orb_per, day_nums):
  dec_degs = dec_gen(eccentricity, axis_norm_degs, orb_per, day_nums, p_degs)
  eot_mins = eot_gen(eccentricity, p_degs, axis_norm_degs, peri_day, orb_per, day_nums)
  return eot_mins, dec_degs