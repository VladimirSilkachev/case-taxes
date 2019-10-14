"""
Case-study #2
Developers:
Silkachev (40%), Popov N (30%), Vinnikov R(50%)
"""
import local as lc

name_month = [lc.JAN, lc.FAB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(lc.QUESTION, name_month[month], end=''))
    income = float(input())
    annual_income += income
print(annual_income)


def sub():
    if annual_income <= 9075:
        taxes = 0.1
        s = 1
    elif 9076 <= annual_income <= 36900:
        s = 2
        taxes = 0.15
    elif 36901 <= annual_income <= 89350:
        s = 3
        taxes = 0.25
    elif 89351 <= annual_income <= 186350:
        s = 4
        taxes = 0.28
    elif 186351 <= annual_income <= 405100:
        s = 5
        taxes = 0.33
    elif 405101 <= annual_income <= 406750:
        s = 6
        taxes = 0.35
    elif 406751 < annual_income:
        s = 7
        taxes = 0.396
    pass


def couple():
    if annual_income <= 18150:
        taxes = 0.1
        s = 1
    elif 18151 <= annual_income <= 73800:
        taxes = 0.15
        s = 2
    elif 73801 <= annual_income <= 148850:
        taxes = 0.25
        s = 3
    elif 148851 <= annual_income <= 226850:
        taxes = 0.28
        s = 4
    elif 226851 <= annual_income <= 405100:
        taxes = 0.33
        s = 5
    elif 405101 <= annual_income <= 457600:
        taxes = 0.35
        s = 6
    elif 457601 <= annual_income:
        taxes = 0.396
        s = 7
    pass


def single():
    if annual_income <= 12950:
        taxes = 0.1
        s = 1
        gr1 = annual_income * 0.1
        gr2 = 0
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 12951 <= annual_income <= 49400:
        taxes = 0.15
        s = 2
        gr1 = 12950 * 0.1
        gr2 = (annual_income - gr1) * 0.15
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 49401 <= annual_income <= 127550:
        taxes = 0.25
        s = 3
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12951) * 0.15
        gr3 = (annual_income - 49400) * 0.25
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 127551 <= annual_income <= 206600:
        taxes = 0.28
        s = 4
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12951) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (annual_income - 127550) * 0.28
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 206601 <= annual_income <= 405100:
        taxes = 0.33
        s = 5
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12951) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (annual_income - 206600) * 0.33
        gr6 = 0
        gr7 = 0
    if 405101 <= annual_income <= 432200:
        taxes = 0.35
        s = 6
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12951) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (405100 - 206600) * 0.33
        gr6 = (annual_income - 405100) * 0.35
        gr7 = 0
    if 432201 <= annual_income:
        taxes = 0.396
        s = 7
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12951) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (405100 - 206600) * 0.33
        gr6 = (432200 - 405100) * 0.35
        gr7 = (annual_income - 432200) * 0.396
    for i in range(7, 1, -1):
        if s == i:
            t = (gr1 + gr2 + gr3 + gr4 + gr5 + gr6 + gr7)
    pass


print(lc.STATUS)
st = input()

if st == lc.SUBJECT:
    sub()

if st == lc.COUPLE:
    couple()

if st == lc.SINGLE:
    single()