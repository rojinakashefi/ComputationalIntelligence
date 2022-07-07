import fuzzification as f
import inference as i
import defuzzification as d


class ProvideResult(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(ProvideResult, cls).__new__(cls)
    return cls.instance

  @staticmethod
  def get_final_result(input_dict: dict) -> str:
    chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, exercise, old_peak, thallium, sex, age = f.fuzzification(
      input_dict)
    healthy, sick_1, sick_2, sick_3, sick_4 = i.inference(chest_pain, blood_pressure, cholesterol, blood_sugar, ecg,
                                                          heart_rate, exercise, old_peak, thallium, sex, age)
    print(healthy,sick_1,sick_2,sick_3,sick_4)
    status = d.defuzzification(healthy, sick_1, sick_2, sick_3, sick_4)
    return_string = ''
    if status < 1.78:
      return_string += 'healthy'
    if 1 <= status <= 2.51:
      if return_string != '':
        return_string += '& '
      return_string += 'Sick1 '
    if 1.78 <= status <= 3.25:
      if return_string != '':
        return_string += '& '
      return_string += 'Sick2 '
    if 1.5 <= status <= 4.5:
      if return_string != '':
        return_string += '& '
      return_string += 'Sick3 '
    if status > 3.25:
      if return_string != '':
        return_string += '& '
      return_string += 'Sick4 '
    return_string += ': ' + str(status)
    return return_string
