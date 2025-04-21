WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'понедельник'
WeeksDayTranslation['Tuesday'] = 'вторник'
WeeksDayTranslation['Wednesday'] = 'среда'
WeeksDay = ['Monday', 'Tuesday', 'Wednesday']
for Day in WeeksDayTranslation:
    print(Day, WeeksDayTranslation[Day])
for Day, val in WeeksDayTranslation.items():
    print(Day, val)