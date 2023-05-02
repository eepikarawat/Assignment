import random
import string

def otp(x):
    gen_otp="".join([random.choice(string.ascii_uppercase+string.digits) for n in range(x)])
    return gen_otp

l=(4,6)
x=random.choice(l)
output=otp(x)
print(output)