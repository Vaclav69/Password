import random
character = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}\|;:,<.>/?`~]'
password = int(input('How many Passwords do you want to generate?????'))
none = ''
for i in range(password):
    none += random.choice(character)
print(none)


