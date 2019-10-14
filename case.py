"""
Case-study #2
Developers:
Silkachev (30%), Popov N (30%), Vinnikov R(55%)
"""
import Local as lc

name_month = [lc.JAN, lc.FAB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(lc.QUESTION, name_month[month]), end=' ')
    income = float(input())
    annual_income += income
print(annual_income)


def sub():
    if annual_income <= 9075:
        gr1 = annual_income * 0.1
        gr2 = 0
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    elif 9076 <= annual_income <= 36900:
        gr1 = 9075 * 0.1
        gr2 = (annual_income - 9075) * 0.15
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    elif 36901 <= annual_income <= 89350:
        gr1 = 9075 * 0.1
        gr2 = (36900 - 9075) * 0.15
        gr3 = (annual_income - 36900) * 0.25
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    elif 89351 <= annual_income <= 186350:
        gr1 = 9075 * 0.1
        gr2 = (36900 - 9075) * 0.15
        gr3 = (89350 - 36900) * 0.25
        gr4 = (annual_income - 89350) * 0.28
        gr5 = 0
        gr6 = 0
        gr7 = 0
    elif 186351 <= annual_income <= 405100:
        gr1 = 9075 * 0.1
        gr2 = (36900 - 9075) * 0.15
        gr3 = (89350 - 36900) * 0.25
        gr4 = (186350 - 89350) * 0.28
        gr5 = (annual_income - 186350) * 0.33
        gr6 = 0
        gr7 = 0
    elif 405101 <= annual_income <= 406750:
        gr1 = 9075 * 0.1
        gr2 = (36900 - 9075) * 0.15
        gr3 = (89350 - 36900) * 0.25
        gr4 = (186350 - 89350) * 0.28
        gr5 = (405100 - 186350) * 0.33
        gr6 = (annual_income - 405100) * 0.35
        gr7 = 0
    elif 406751 < annual_income:
        gr1 = 9075 * 0.1
        gr2 = (36900 - 9075) * 0.15
        gr3 = (89350 - 36900) * 0.25
        gr4 = (186350 - 89350) * 0.28
        gr5 = (405100 - 186350) * 0.33
        gr6 = (406750 - 405100) * 0.35
        gr7 = (annual_income - 406750) * 0.396
    print(gr1 + gr2 + gr3 + gr4 + gr5 + gr6 + gr7)
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
        gr1 = annual_income * 0.1
        gr2 = 0
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 12951 <= annual_income <= 49400:
        gr1 = 12950 * 0.1
        gr2 = (annual_income - 12950) * 0.15
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 49401 <= annual_income <= 127550:
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12950) * 0.15
        gr3 = (annual_income - 49400) * 0.25
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 127551 <= annual_income <= 206600:
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12950) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (annual_income - 127550) * 0.28
        gr5 = 0
        gr6 = 0
        gr7 = 0
    if 206601 <= annual_income <= 405100:
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12950) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (annual_income - 206600) * 0.33
        gr6 = 0
        gr7 = 0
    if 405101 <= annual_income <= 432200:
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12950) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (405100 - 206600) * 0.33
        gr6 = (annual_income - 405100) * 0.35
        gr7 = 0
    if 432201 <= annual_income:
        gr1 = 12950 * 0.1
        gr2 = (49400 - 12950) * 0.15
        gr3 = (127550 - 49400) * 0.25
        gr4 = (206600 - 127550) * 0.28
        gr5 = (405100 - 206600) * 0.33
        gr6 = (432200 - 405100) * 0.35
        gr7 = (annual_income - 432200) * 0.396
    print(gr1 + gr2 + gr3 + gr4 + gr5 + gr6 + gr7)
    pass


print(lc.STATUS)
st = input()

if st == lc.SUBJECT:
    sub()

if st == lc.COUPLE:
    couple()

if st == lc.SINGLE:
    single()