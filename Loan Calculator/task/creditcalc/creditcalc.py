import math
import argparse


def annuity(p, n, i):
    # Calculate the annuity payment
    i = i / (12 * 100)
    a = (p * i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    print('Your annuity payment = {}!'.format(math.ceil(a) * n - p))
    print('Overpayment = {}'.format(math.ceil(a)))


def credit_principal(a, n, i):
    # Calculate the credit principal
    i = i / (12 * 100)
    p = a * ((math.pow((1 + i), n) - 1) / (i * math.pow((1 + i), n)))
    print('Your credit principal = {}!'.format(math.ceil(p)))
    print('Overpayment = {}'.format(math.ceil(a * n) - p))


def years(p, a, i):
    # Calculate the number of years
    i = i / (12 * 100)
    n = math.log(a / (a - i * p), 1 + i)
    print('It will take {} years to repay this loan!'.format(int(math.ceil(n) / 12)))
    print('Overpayment = {}'.format(a * int(math.ceil(n)) - p))


def diff(p, n, i):
    # Calculate the diff payments
    i = i / (12 * 100)
    sum_payments = 0
    for m in range(1, n + 1):
        d = p / n + i * (p - (p * (m - 1) / n))
        sum_payments += math.ceil(d)
        print('Month {}: payment is {}'.format(m, math.ceil(d)))
    print()
    print('Overpayment = {}'.format(math.ceil(sum_payments)-p))


parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=int, default=0)
parser.add_argument('--payment', type=int, default=0)
parser.add_argument('--periods', type=int, default=0)
parser.add_argument('--interest', type=float, default=0)
parser.add_argument('--type', type=str, default='annuity')
args = parser.parse_args()

payment_menu = args.type
if payment_menu == 'annuity':
    if args.payment != 0 and args.periods != 0 and args.interest != 0:
        credit_principal(args.payment, args.periods, args.interest)
    elif args.principal != 0 and args.periods != 0 and args.interest != 0:
        annuity(args.principal, args.periods, args.interest)
    elif args.principal != 0 and args.payment != 0 and args.interest != 0:
        years(args.principal, args.payment, args.interest)
    else:
        print('Incorrect parameters')
elif payment_menu == 'diff':
    if args.principal and args.periods and args.interest:
        diff(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')

# if payment_menu == 'n':
#     p = int(args.principal)
#     a = float(args.payment)
#     i = float(args.interest) / 100 / 12
#     n = math.ceil(math.log(a / (a - i * p), 1 + i))
#     print('It will take {} years and {} months to repay this loan!'.format(int(n // 12),
#                                                                            int(n % 12)))
# elif payment_menu == 'a':
#     p = int(args.principal)
#     n = int(args.periods)
#     i = float(args.interest) / 100 / 12
#     a = (p * i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
#     print('Your monthly payment = {}!'.format(math.ceil(a)))
# elif payment_menu == 'p':
#     a = float(args.payment)
#     n = int(args.periods)
#     i = float(args.interest) / 100 / 12
#     p = a / ((i * math.pow((1 + i), n))
#              / (math.pow((1 + i), n) - 1))
#     print('Your loan principal = {}!'.format(math.ceil(p)))
# else:
#     print('You have entered an invalid option')
