import fuzzification


def defuzzification(healthy, sick_1, sick_2, sick_3, sick_4):
  step, new_x, numerator, denominator = (0.001, 0, 0, 0)
  while new_x <= 4:
    y = m_result(new_x, healthy, sick_1, sick_2, sick_3, sick_4)
    denominator += y
    numerator += y * new_x
    new_x += step
  return numerator / denominator


def m_result(x, healthy, sick_1, sick_2, sick_3, sick_4):
  y = fuzzification.output(x)
  output = max(min(healthy, y['healthy']), min(sick_1, y['sick_1']), min(sick_2, y['sick_2']), min(sick_3, y['sick_3']),
               min(sick_4, y['sick_4']))
  return output
