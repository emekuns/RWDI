from typing import List

with open("report_repair_test_data.txt") as file:
    expense_report = file.read().splitlines()

def report_repair(target: int) -> List[int]:
    num_dict = {}
    result = []
    for i in range(len(expense_report)):
        if target - int(expense_report[i]) in num_dict:
            result.append(i)
            result.append(num_dict[target - int(expense_report[i])])
        else:
            num_dict[int(expense_report[i])] = i

    return [int(expense_report[result[0]]), int(expense_report[result[1]]), int(expense_report[result[0]])*int(expense_report[result[1]])]

def report_repair_part_2(target: int) -> List[int] :
    for i in range(len(expense_report)):
        s = set()
        curr_sum = target - int(expense_report[i])
        for j in range(i + 1, len(expense_report)):
            if (curr_sum - int(expense_report[j])) in s:
                return [int(expense_report[i]), int(expense_report[j]), curr_sum - int(expense_report[j]), int(expense_report[i])*int(expense_report[j])*(curr_sum - int(expense_report[j]))]
            s.add(int(expense_report[j]))

def password_philosophy(low, high, letter, password):
    count = 0
    for char in password:
        if char == letter:
            count += 1
    return high >= count >= low

def password_philosophy_part_2(i, j, letter, password):
    return (password[i] == letter) ^ (password[j] == letter)

correct_password_count = 0
correct_password_count_part_2 = 0
with open("password_philosophy_test_data.txt") as file:
    for line in file:
        freq, letter, password = line.split(" ")
        letter = letter[:len(letter) - 1]
        low, high = map(int, freq.split('-'))
        if password_philosophy(low, high, letter, password):
            correct_password_count += 1

        if password_philosophy_part_2(low - 1, high - 1, letter, password):
            correct_password_count_part_2 += 1

with open("toboggan_trajectory_test_data.txt") as file:
    lines = file.read().splitlines()

def toboggan_trajectory() -> int:
    total = 0
    x = 0
    for line in lines:
        if line[x] == '#':
            total += 1
        x += 3
            
        x %= len(line)

    return total

def toboggan_trajectory_part_2_helper(new_x: int, new_y: int) -> int:
    total = 0
    x = 0
    y = 0

    while y < len(lines):
        line = lines[y]
        if line[x] == '#':
            total += 1
        x += new_x
        x %= len(line)
        y += new_y

    return total

def toboggan_trajectory_part_2() -> int:
    return (
        toboggan_trajectory_part_2_helper(1, 1)*
        toboggan_trajectory_part_2_helper(3, 1)*
        toboggan_trajectory_part_2_helper(5, 1)*
        toboggan_trajectory_part_2_helper(7, 1)*
        toboggan_trajectory_part_2_helper(1, 2)
        )

with open("passport_processing_test_data.txt") as file:
    data = []
    for passport in file.read().split('\n\n'):
        dict = {}
        for field in passport.split():
            key, _, value = field.partition(':')
            dict[key] = value
        data.append(dict)

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
hair_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def passport_processing() -> int:
    total = 0
    for passport in data:
        if set(passport.keys()).issuperset(required_fields):
            total += 1
    
    return total

def passport_processing_part_2() -> int:
    total = 0
    for passport in data:
        if not (set(passport.keys()).issuperset(required_fields)):
            continue
        if not (1920 <= int(passport['byr']) <= 2002):
            continue
        if not (2010 <= int(passport['iyr']) <= 2020):
            continue
        if not (2020 <= int(passport['eyr']) <= 2030):
            continue
        if not (passport['hgt'][-2:] == "cm" or passport['hgt'][-2:] == "in"):
            continue
        if (passport['hgt'][-2:] == "cm" and not (150 <= int(passport['hgt'][:-2]) <= 193)):
            continue
        if (passport['hgt'][-2:] == "in" and not (59 <= int(passport['hgt'][:-2])) <= 76):
            continue
        if not (passport['hcl'][0] == "#" and (passport['hcl'][1:].isnumeric() or passport['hcl'][1:].isalpha()) and len(passport['hcl'][1:]) == 6):
            continue
        if passport['ecl'] not in hair_colors:
            continue
        if not (passport['pid'].isnumeric() and len(passport['pid']) == 9):
            continue
        
        total += 1
    
    return total

print('Report Repair: ')
print(report_repair(2020))
print('\n')
print('Report Repair Part 2: ')
print(report_repair_part_2(2020))
print('\n')
print('Password Philosophy: ')
print(correct_password_count)
print('\n')
print('Password Philosophy Part 2: ')
print(correct_password_count_part_2)
print('\n')
print('Toboggan Trajectory: ')
print(toboggan_trajectory())
print('\n')
print('Toboggan Trajectory Part 2: ')
print(toboggan_trajectory_part_2())
print('\n')
print('Passport Processing: ')
print(passport_processing())
print('\n')
print('Passport Processing Part 2: ')
print(passport_processing_part_2())
print('\n')