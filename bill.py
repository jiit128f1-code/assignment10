
# bill.py - Electricity bill module (legacy code, do not change behaviour)

HOUSEHOLD_TYPE = "H"
COMMERCIAL_TYPE = "C"

HOUSEHOLD_RATES = (3, 5, 8)
COMMERCIAL_RATES = (6, 9, 12)

FIRST_SLAB_LIMIT = 100
SECOND_SLAB_LIMIT = 300

TAX_RATE = 0.18
SENIOR_DISCOUNT_RATE = 0.05
LATE_SURCHARGE_RATE = 0.02
def calc(name, address, units, connection_type, previous_due, senior_flag):
    print('Customer:', name)
    print('Address:', address)

    if connection_type == 'H':
        if units <= 100:
            amount = units * 3
        elif units <= 300:
            amount = 100 * 3 + (units - 100) * 5
        else:
            amount = 100 * 3 + 200 * 5 + (units - 300) * 8

    elif connection_type == 'C':
        if units <= 100:
            amount = units * 6
        elif units <= 300:
            amount = 100 * 6 + (units - 100) * 9
        else:
            amount = 100 * 6 + 200 * 9 + (units - 300) * 12

    else:
        print('bad type')
        return -1

    tax_amount = amount * 0.18

    if senior_flag == 1 and connection_type == 'H':
        amount = amount - amount * 0.05
    total_amount = amount + tax_amount + previous_due

    if previous_due > 0:
        total_amount = total_amount + previous_due * 0.02

    print('Total:', total_amount)
    return total_amount


def calc2(name, address, units, connection_type, previous_due, senior_flag):
    receipt = ''
    receipt = receipt + 'Customer: ' + name + '\n'
    receipt = receipt + 'Address: ' + address + '\n'

    if connection_type == 'H':
        if units <= 100:
            amount = units * 3
        elif units <= 300:
            amount = 100 * 3 + (units - 100) * 5
        else:
            amount = 100 * 3 + 200 * 5 + (units - 300) * 8

    elif connection_type == 'C':
        if units <= 100:
            amount = units * 6
        elif units <= 300:
            amount = 100 * 6 + (units - 100) * 9
        else:
            amount = 100 * 6 + 200 * 9 + (units - 300) * 12

    else:
        return 'bad type'

    tax_amount = amount * 0.18

    if senior_flag == 1 and connection_type == 'H':
        amount = amount - amount * 0.05

    total_amount = amount + tax_amount + previous_due

    if previous_due > 0:
        total_amount = total_amount + previous_due * 0.02

    receipt = receipt + 'Total: ' + str(total_amount)
    return receipt
