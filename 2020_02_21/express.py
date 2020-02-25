'''
On a warm, sunny day, Nick glanced at a thermometer, and noticed something
quite interesting. When he toggled between the Fahrenheit and Celsius
scales, the digits of the temperature — when rounded to the nearest degree —
had switched. For example, this works for a temperature of 61 degrees
Fahrenheit, which corresponds to a temperature of 16 degrees Celsius.

However, the temperature that day was not 61 degrees Fahrenheit. What
was the temperature?
'''
import pandas as pd

def f_to_c(temp):
    return round(((temp-32)*5)/9)

def reverse_int(number):
    return int(''.join(list(reversed(str(number)))))

print('Test\nF Temp is 61')
print('C Temp is: ', f_to_c(61))
print('F Temp is reversed C Temp-->', 61 == reverse_int(f_to_c(61)))
print('\n')

df = pd.DataFrame({'f_temp':range(32,400)})
df['c_temp'] = df.f_temp.apply(f_to_c)
df['reverse_true'] = df.apply(lambda x: x.f_temp == reverse_int(x.c_temp), axis=1)

print(df[df.reverse_true==True])
