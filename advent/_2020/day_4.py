def read_passports(filename):
    with open(filename) as file:
        passports = []
        passport = {}
        for line in file.readlines():
            if line == '\n':
                passports.append(passport)
                passport = {}
            else:
                for pair in line[:-1].split(' '):
                    key, value = pair.split(':')
                    passport[key] = value
        if passport:
            passports.append(passport)
    return passports

batch = read_passports('input/2020/day_4')


def is_valid_1(_passport):
    for field in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
        if field not in _passport:
            return False
    return True


print('PART 1')
print(f'{len(batch)} passports')
print(f'{len([p for p in batch if is_valid_1(p)])} valid')


def is_valid_2(_passport):
    try:
        # for field in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
        byr = int(_passport['byr'])
        assert 1920 <= byr <= 2002, 'too young/old'
        iyr = int(_passport['iyr'])
        assert 2010 <= iyr <= 2020, 'old/fake passport'
        eyr = int(_passport['eyr'])
        assert 2020 <= eyr <= 2030, 'expired/invalid passport'
        hgt = _passport['hgt']
        unit = hgt[-2:]
        assert unit in ('in', 'cm'), 'invalid hgt unit'
        value = int(hgt[:-2])
        assert unit == 'in' or 150 <= value <= 193, 'invalid hgt (cm)'
        assert unit == 'cm' or 59 <= value <= 76, 'invalid hgt (in)'
        hcl = _passport['hcl']
        assert len(hcl) == 7, 'invalid hcl (len)'
        assert hcl[0] == '#', 'missing #'
        for chr in hcl[1:]:
            assert chr in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], 'invalid hex'
        ecl = _passport['ecl']
        assert ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 'invalid ecl'
        pid = _passport['pid']
        assert len(pid) <= 9, 'invalid pid len'
        int(pid)
    except (AssertionError, KeyError, TypeError, ValueError) as e:
        if is_valid_1(_passport):
            print(_passport, e)
        return False
    return True


print('PART 2')
print(f'{len(batch)} passports')
print(f'{len([p for p in batch if is_valid_2(p)])} valid')
