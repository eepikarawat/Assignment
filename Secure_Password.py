import random
import string
    
def rand_pass(size):
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.punctuation+
                                            string.digits)
                                            for n in range(size)])
                            
    return generate_pass
print('SECURE PASSWORD')
num=random.randrange(8,12);
password = rand_pass(num)
print(password)