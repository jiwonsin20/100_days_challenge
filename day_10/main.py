# Functions with Outputs

def format_name(f_name, l_name):
  first = f_name.title()
  last = l_name.title()
  return first + ' ' + last

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return False
        else:
            return True
    else:
        return False

def month_to_days(month):
  if month % 2 == 0:
    if month < 8:
      return 30
    else:
      return 31
  else: #uneven months
    if month > 8:
      return 30
    else:
      return 31


def days_in_month(year, month):
  if is_leap(year):
    if month == 2:
      return 29
    else:
      return month_to_days(month)
  else:
    if month == 2:
      return 28
    else:
      return month_to_days(month)

print(days_in_month(year=2022, month=2))