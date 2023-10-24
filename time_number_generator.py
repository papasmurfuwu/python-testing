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
        try:
            user = int(input('Do you want time to be 12-hours or 24-hours (12/ 24)? '))
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

        except ValueError as e:
            print(e)
            continue


def num_generator():
    print('Please enter integers for the following inputs.')
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
                print(generated_number)
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

            try:
                again = input('Would you like to use the program again (y/n)? ').strip().lower()
                if again == 'y':
                    continue
                elif again == 'n':
                    print('Thanks for using us and have a great day!')
                    break
            except ValueError:
                print('Please enter y/n!')

        except ValueError:
            print('Please enter a valid string (time/ number)')





