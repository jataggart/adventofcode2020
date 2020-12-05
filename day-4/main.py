from functools import reduce


def get_sample_input() -> str:
    return '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''


def get_sample_strict_input() -> str:
    return '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''


def get_real_input() -> str:
    with open('input.txt', 'r') as f:
        return f.read()


def find_passports(input: str) -> list[str]:
    return input.split('\n\n')


def is_passport_valid(passport: str) -> bool:
    return all(x in passport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def is_passport_valid_with_strict_checks(passport: str) -> bool:
    import re

    hcl_pattern = re.compile('^#[0-9a-f]{6}$')
    pid_pattern = re.compile('^[0-9]{9}$')

    def is_byr_valid(byr: str) -> bool:
        return len(byr) == 4 and byr.isnumeric() and 1920 <= int(byr) <= 2002

    def is_iyr_valid(iyr: str) -> bool:
        return len(iyr) == 4 and iyr.isnumeric() and 2010 <= int(iyr) <= 2020

    def is_eyr_valid(eyr: str) -> bool:
        return len(eyr) == 4 and eyr.isnumeric() and 2020 <= int(eyr) <= 2030

    def is_hgt_valid(hgt: str) -> bool:
        return (
                       hgt.endswith('cm') and hgt.rstrip('cm').isnumeric() and 150 <= int(hgt.rstrip('cm')) <= 193
               ) or (
                       hgt.endswith('in') and hgt.rstrip('in').isnumeric() and 59 <= int(hgt.rstrip('in')) <= 76
               )

    def is_hcl_valid(hcl: str) -> bool:
        return hcl_pattern.match(hcl) is not None

    def is_ecl_valid(ecl: str) -> bool:
        return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_pid_valid(pid: str) -> bool:
        return pid_pattern.match(pid) is not None

    byr_valid = False
    iyr_valid = False
    eyr_valid = False
    hgt_valid = False
    hcl_valid = False
    ecl_valid = False
    pid_valid = False

    parts = reduce(list.__add__, map(lambda x: x.split('\n'), passport.split(' ')))
    for part in parts:
        if part != '':
            label, value = part.split(':')
            if label == 'byr':
                byr_valid = is_byr_valid(value)
            elif label == 'iyr':
                iyr_valid = is_iyr_valid(value)
            elif label == 'eyr':
                eyr_valid = is_eyr_valid(value)
            elif label == 'hgt':
                hgt_valid = is_hgt_valid(value)
            elif label == 'hcl':
                hcl_valid = is_hcl_valid(value)
            elif label == 'ecl':
                ecl_valid = is_ecl_valid(value)
            elif label == 'pid':
                pid_valid = is_pid_valid(value)

    return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid


if __name__ == '__main__':
    sample_input = get_sample_input()
    sample_passports = find_passports(sample_input)
    sample_count = len(
        list(sample_passport for sample_passport in sample_passports if is_passport_valid(sample_passport))
    )
    print(f'Sample Result: {sample_count}')

    real_input = get_real_input()
    real_passports = find_passports(real_input)
    real_count = len(list(real_passport for real_passport in real_passports if is_passport_valid(real_passport)))
    print(f'Part One Result: {real_count}')

    sample_strict_input = get_sample_strict_input()
    sample_strict_passports = find_passports(sample_strict_input)
    sample_strict_count = len(list(
        sample_passport for sample_passport in sample_strict_passports if
        is_passport_valid_with_strict_checks(sample_passport))
    )
    print(f'Sample Strict Result: {sample_strict_count}')

    real_strict_passports = find_passports(real_input)
    real_strict_count = len(
        list(real_passport for real_passport in real_passports if is_passport_valid_with_strict_checks(real_passport))
    )
    print(f'Part Two Result: {real_strict_count}')
