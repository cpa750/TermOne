from math import ceil

SMALL_TIP_RATE = 0.15
LARGE_TIP_RATE = 0.2

def apply_tip(total):
    """
    Function that applies two tip rates to a total, then rounds that number.
    Returns the two new totals as a tuple.
    """
    small_tip = round(total*SMALL_TIP_RATE, 2)
    large_tip = round(total*LARGE_TIP_RATE, 2)

    return (small_tip, large_tip)

total = float(input("Enter the total bill amount: "))

tipped_total = apply_tip(total)
print("15% tipped total: ${}".format(tipped_total[0]))
print("20% tipped total: ${}".format(tipped_total[1]))

total = ceil(total)

tipped_total = apply_tip(total)
print("15% tipped total with initial amount rounded up: ${}".format(tipped_total[0]))
print("20% tipped total with initial amount rounded up: ${}".format(tipped_total[1]))
