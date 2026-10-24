
HOUSEHOLD_TYPE = "H"
COMMERCIAL_TYPE = "C"

HOUSEHOLD_RATES = (3, 5, 8)
COMMERCIAL_RATES = (6, 9, 12)

FIRST_SLAB_LIMIT = 100
SECOND_SLAB_LIMIT = 300

TAX_RATE = 0.18
SENIOR_DISCOUNT_RATE = 0.05
LATE_SURCHARGE_RATE = 0.02


def calculate_slab_amount(units, rates):
    first_rate, second_rate, third_rate = rates

    if units <= FIRST_SLAB_LIMIT:
        return units * first_rate

    if units <= SECOND_SLAB_LIMIT:
        return (
            FIRST_SLAB_LIMIT * first_rate
            + (units - FIRST_SLAB_LIMIT) * second_rate
        )

    return (
        FIRST_SLAB_LIMIT * first_rate
        + (SECOND_SLAB_LIMIT - FIRST_SLAB_LIMIT) * second_rate
        + (units - SECOND_SLAB_LIMIT) * third_rate
    )


def calculate_tax(amount):
    return amount * TAX_RATE


def apply_senior_discount(amount, connection_type, senior_flag):
    if senior_flag == 1 and connection_type == HOUSEHOLD_TYPE:
        return amount - amount * SENIOR_DISCOUNT_RATE
    return amount


def calculate_late_surcharge(previous_due):
    if previous_due > 0:
        return previous_due * LATE_SURCHARGE_RATE
    return 0


def calculate_total(units, connection_type, previous_due, senior_flag):
    if connection_type == HOUSEHOLD_TYPE:
        rates = HOUSEHOLD_RATES
    elif connection_type == COMMERCIAL_TYPE:
        rates = COMMERCIAL_RATES
    else:
        return None

    amount = calculate_slab_amount(units, rates)
    tax_amount = calculate_tax(amount)
    amount = apply_senior_discount(
        amount, connection_type, senior_flag
    )

    return (
        amount
        + tax_amount
        + previous_due
        + calculate_late_surcharge(previous_due)
    )


def calc(name, address, units, connection_type, previous_due, senior_flag):
    print("Customer:", name)
    print("Address:", address)

    total_amount = calculate_total(
        units, connection_type, previous_due, senior_flag
    )

    if total_amount is None:
        print("bad type")
        return -1

    print("Total:", total_amount)
    return total_amount


def calc2(name, address, units, connection_type, previous_due, senior_flag):
    total_amount = calculate_total(
        units, connection_type, previous_due, senior_flag
    )

    if total_amount is None:
        return "bad type"

    return (
        f"Customer: {name}\n"
        f"Address: {address}\n"
        f"Total: {total_amount}"
    )
