'''
Created on 2012-6-4

@author: jiang
'''

months = [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th']\
        + ['st']
        
        

year = raw_input("year:")
month = raw_input('month:')



month_number = int(month)
if month_number <= 0 or month_number > 12:
    print '!!Error:month input error'
    exit(0)
    
day = raw_input("day(1-31):")
day_number = int(day)
print day_number
if day_number <= 0 or day_number > 31:
    print '!!Error:day number input error'
    exit(0)
    
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]
print month_name + ' ' + ordinal + ',' + year

raw_input("!!Error:press any key to continue")
