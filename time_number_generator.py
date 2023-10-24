# random time/ number generator
# make it where you can select time or number format
# e.g. (time: 14:56 OR number: 1234)
# Time: 12hr or 24hr, how many generate
# 12hr (0, 1, 2), (0-9)

import random
again = True
print('Welcome to the time/ number generator program!')


# defining functions
def time_generator():
    again_time = True
    while again_time:
        while True:
            try:
                user = int(input('Do you want time to be 12-hours or 24-hours (12/ 24)? '))
                if user == 12 or user == 24:
                    break
                else:
                    print('Invalid input. Please enter either 12 or 24.')
                    continue
            except ValueError:
                print('Invalid input. Please enter a valid integer. ')
                continue

        user_times = int(input('How many times do you want? '))

        if user == 24:
            for i in range(user_times):
                hours = random.randint(0, 23)
                minutes = random.randint(0, 59)
                print(f"{hours:02}:{minutes:02}")
            break

        elif user == 12:
            for i in range(user_times):
                hours = random.randint(1, 12)
                minutes = random.randint(0, 59)
                am_pm = random.choice(['AM', 'PM'])
                print(f"{hours:02}:{minutes:02} {am_pm}")
            break

        else:
            raise ValueError('Please enter either 12 or 24!')


def num_generator():
    print('Please enter integers for the following inputs.')
    i = 0
    again_num = True
    while again_num:
        try:
            num_digit = int(input('How many digits for each number? '))
            num_count = int(input('How many numbers do you want? '))

            for count in range(num_count):
                generated_number = ""
                for num in range(num_digit):
                    digit = str(random.randint(1, 9))
                    generated_number += digit
                formatted_number = "{:,}".format(int(generated_number))
                print(formatted_number)
            break

        except ValueError as e:
            print(e)
            print('Please enter valid integers!')
            continue


if __name__ == '__main__':
    while again:
        try:
            user_choice = input('Do you want to generate time or a number? (time/ number) ').strip().lower()

            if user_choice == 'time':
                time_generator()

            elif user_choice == 'number':
                num_generator()

            while True:
                try:
                    again = input('Would you like to use the program again (y/n)? ').strip().lower()
                    if again == 'y':
                        break

                    elif again == 'n':
                        print('Thanks for using us and have a great day!')
                        again = False
                        break
                    break
                except ValueError:
                    print('Please enter y/n!')
                    continue

        except ValueError:
            print('Please enter a valid string (time/ number)')
            continue
