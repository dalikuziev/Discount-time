import datetime
import time

now = datetime.datetime.now()
now = now.replace(microsecond=0)
date1 = datetime.datetime(2024, 1, 1)
date2 = datetime.datetime(2024, 1, 11)
'''Dastur qanday ishlashini ko'rishingiz uchun pastda 5 soniyalik ishni ham qoldirib ketdim'''
# date1 = datetime.datetime(2024, 1, 1, 1, 1, 1)
# date2 = datetime.datetime(2024, 1, 1, 1, 1, 5)
date = date2 - date1
end = now + date

print('Bizning yangi chegirmalarimiz 10 kun davom etadi va bunga start berdik')

while True:
    now = datetime.datetime.now()
    now = now.replace(microsecond=0)
    if end < now:
        break
    print(end - now)
    time.sleep(1)

print('chegirma tugadi')
