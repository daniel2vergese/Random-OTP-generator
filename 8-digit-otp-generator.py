import random

num_otps = 100000
otp_length = 8

with open('otp_list.txt', 'w') as f:
    for i in range(num_otps):
        otp = ''
        for j in range(otp_length):
            otp += str(random.randint(0, 9))
        f.write(otp + '\n')
