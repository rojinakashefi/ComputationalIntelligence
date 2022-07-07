def chest_pain(x):
  chest_pain = {'typical_anginal': 1 if x == '1' else 0,
                'atypical_anginal': 1 if x == '2' else 0,
                'non_anginal_pain': 1 if x == '3' else 0,
                'asymptomatic': 1 if x == '4' else 0}
  return chest_pain


def blood_pressure(x):
  blood_pressure = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}
  # low
  if x < 111:
    blood_pressure['low'] = 1
  elif 111 <= x < 134:
    blood_pressure['low'] = (134 - x) / 23

  # medium
  if 127 <= x < 139:
    blood_pressure['medium'] = (x - 127) / 12
  elif 139 <= x < 153:
    blood_pressure['medium'] = (153 - x) / 14

  # high
  if 142 <= x < 157:
    blood_pressure['high'] = (x - 142) / 15
  elif 157 <= x < 172:
    blood_pressure['high'] = (172 - x) / 15

  # very high
  if 154 <= x < 171:
    blood_pressure['very_high'] = (x - 154) / 17
  elif 171 < x:
    blood_pressure['very_high'] = 1

  return blood_pressure


def cholesterol(x):
  cholesterol = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}

  # low
  if x < 151:
    cholesterol['low'] = 1
  elif 151 <= x < 197:
    cholesterol['low'] = (197 - x) / 46

  # medium
  if 188 <= x < 215:
    cholesterol['medium'] = (x - 188) / 27
  elif 215 <= x < 250:
    cholesterol['medium'] = (250 - x) / 35

  # high
  if 217 <= x < 263:
    cholesterol['high'] = (x - 217) / 46
  elif 263 <= x < 307:
    cholesterol['high'] = (307 - x) / 44

  # very high
  if 281 <= x < 347:
    cholesterol['very_high'] = (x - 281) / 66
  elif 347 <= x:
    cholesterol['very_high'] = 1

  return cholesterol


def blood_sugar(x):
  blood_sugar = {'true': 1 if x > 120 else 0,
                 'false': 1 if x <= 120 else 0}
  return blood_sugar


def ecg(x):
  ecg = {'normal': 0, 'abnormal': 0, 'hypertrophy': 0}
  # normal
  if x < 0:
    ecg['normal'] = 1
  elif 0 <= x < 0.4:
    ecg["normal"] = (0.4 - x) / 0.4

  # abnormal
  if 0.2 <= x < 1:
    ecg["abnormal"] = (x - 0.2) / 0.8
  elif 1 <= x < 1.8:
    ecg["abnormal"] = (1.8 - x) / 0.8

  # hypertrophy
  if 1.4 <= x < 1.9:
    ecg["hypertrophy"] = (x - 1.4) / 0.5
  elif 1.9 <= x:
    ecg["hypertrophy"] = 1
  return ecg


def heart_rate(x):
  heart_rate = {'low': 0, 'medium': 0, 'high': 0}
  # low
  if x <= 100:
    heart_rate['low'] = 1
  elif 100 <= x < 141:
    heart_rate["low"] = (141 - x) / 41
  # medium
  if 111 <= x < 152:
    heart_rate["medium"] = (x - 111) / 41
  elif 152 <= x < 194:
    heart_rate["medium"] = (194 - x) / 42
  # high
  if 152 <= x < 210:
    heart_rate["high"] = (x - 152) / 58
  elif 210 <= x:
    heart_rate["high"] = 1
  return heart_rate


def exercise(x):
  exercise = {'true': 1 if x == '1' else 0,
              'false': 1 if x == '0' else 0}
  return exercise


def old_peak(x):
  old_peak = {'low': 0, 'risk': 0, 'terrible': 0}
  # low
  if x <= 1:
    old_peak['low'] = 1
  elif 1 <= x < 2:
    old_peak["low"] = (2 - x) / 1
  # risk
  if 1.5 <= x < 2.8:
    old_peak["risk"] = (x - 1.5) / 1.3
  elif 2.8 <= x < 4.2:
    old_peak["risk"] = (4.2 - x) / 1.4
  # terrible
  if 2.5 <= x < 4:
    old_peak["terrible"] = (x - 2.5) / 1.5
  elif 4 <= x:
    old_peak["terrible"] = 1
  return old_peak


def thallium(x):
  thallium = {'normal': 1 if x == str(3) else 0,
              'medium': 1 if x == str(6) else 0,
              'high': 1 if x == str(7) else 0}
  return thallium


def sex(x):
  sex = {'male': 1 if x == str(0) else 0,
         'female': 1 if x == str(1) else 0
         }
  return sex


def age(x):
  age = {'young': 0, 'mild': 0, 'old': 0, 'very_old': 0}
  # young
  if x <= 29:
    age["young"] = 1
  elif 29 <= x < 38:
    age["young"] = (38 - x) / 9

  # mild
  if 33 <= x < 38:
    age["mild"] = (x - 33) / 5
  elif 38 <= x < 45:
    age["mild"] = (45 - x) / 7

  # old
  if 40 <= x < 48:
    age["old"] = (x - 40) / 8
  elif 48 <= x < 58:
    age["old"] = (58 - x) / 10

  # very old
  if 52 <= x < 60:
    age["very_old"] = (x - 52) / 8
  elif x > 58:
    age["very_old"] = 1
  return age


def output(x):
  output = {'healthy': 0, 'sick_1': 0, 'sick_2': 0, 'sick_3': 0, 'sick_4': 0}

  # healthy
  if x <= 0.25:
    output['healthy'] = 1
  elif 0.25 <= x < 1:
    output['healthy'] = (1 - x) / 0.75

  # sick_1
  if 0 <= x < 1:
    output['sick_1'] = (x - 0) / 1
  elif 1 <= x < 2:
    output['sick_1'] = (2 - x) / 1

  # sick_2
  if 1 <= x < 2:
    output['sick_2'] = (x - 1) / 1
  elif 2 <= x < 3:
    output['sick_2'] = (3 - x) / 1

  # sick_3
  if 2 <= x < 3:
    output['sick_3'] = (x - 2) / 1
  elif 3 <= x < 4:
    output['sick_3'] = (4 - x) / 1

  # sick_4
  if 3 <= x < 3.75:
    output['sick_4'] = (x - 3) / 0.75
  elif x > 3.75:
    output['sick_4'] = 1
  return output


def fuzzification(input):
  return (chest_pain(input['chest_pain']),
          blood_pressure(float(input['blood_pressure'])),
          cholesterol(float(input['cholestrol'])),
          blood_sugar(float(input['blood_sugar'])),
          ecg(float(input['ecg'])),
          heart_rate(float(input['heart_rate'])),
          exercise(input['exercise']),
          old_peak(float(input['old_peak'])),
          thallium(input['thallium_scan']),
          sex(input['sex']),
          age(float(input['age'])))
