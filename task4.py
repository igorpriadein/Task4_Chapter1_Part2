



def timestamp (hours, minutes, seconds):
    seconds1 = seconds
    return seconds1
    hours1 = 3600 * seconds
    return hours1
    minutes1 = 60 * seconds
    return minutes1
    overall = hours1 + minutes1 + seconds1
    return overall


num1 = timestamp(6, 12, 55)
num2 = timestamp(6, 12, 44)
res = num1 - num2

print(f'(6, 12, 55); (6, 12, 44) result {res} sec.')








# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. (На английском языке что бы Вы научились понимать 6, 1, 30, 6, 2, 10 result 40 sec.)