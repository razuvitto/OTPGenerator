# package 
import math
import random

# function
def generate():
    digits = "0123456789"
    resOTP = ""
    for i in range(4):
        resOTP += digits[math.floor(random.random() * 10)]
    return resOTP

print("Generated OTP for {}".format(generate()))