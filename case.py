"""
Case-study #2
Developers:
Silkachev (35%), Popov N (30%), Vinnikov R(50%)
"""
import Local as lc

name_month = [lc.JAN, lc.FAB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(lc.QUESTION, name_month[month]), end=' ')
    income = float(input())
    annual_income += income
print(annual_income)


def couple():                                   # вычисление суммы налога для пары
    if annual_income <= 18150:
        gr1 = annual_income * 0.1
        gr2 = 0
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
        
    elif 18151 <= annual_income <= 73800:
        gr1 = 18150 * 0.1
        gr2 = (annual_income - 18150) * 0.15
        gr3 = 0
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
        
    elif 73801 <= annual_income <= 148850:
        gr1 = 18150 * 0.1
        gr2 = (73800 - 18150) * 0.15
        gr3 = (annual_income - 73800) * 0.25
        gr4 = 0
        gr5 = 0
        gr6 = 0
        gr7 = 0
        
    elif 148851 <= annual_income <= 226850:
        gr1 = 18150 * 0.1
        gr2 = (73800 - 18150) * 0.15
        gr3 = (148850 - 73800) * 0.25
        gr4 = (annual_income - 148850) * 0.28
        gr5 = 0
        gr6 = 0
        gr7 = 0
        
    elif 226851 <= annual_income <= 405100:
        gr1 = 18150 * 0.1
        gr2 = (73800 - 18150) * 0.15
        gr3 = (148850 - 73801) * 0.25
        gr4 = (226850 - 148851) * 0.28
        gr5 = (annual_income - 226850) * 0.33
        gr6 = 0
        gr7 = 0
        
    elif 405101 <= annual_income <= 457600:
        gr1 = 18150 * 0.1
        gr2 = (73800 - 18150) * 0.15
        gr3 = (148850 - 73800) * 0.25
        gr4 = (226850 - 148850) * 0.28
        gr5 = (405100 - 226850) * 0.33
        gr6 = (annual_income - 405100) * 0.35
        gr7 = 0
        
    elif 457601 <= annual_income:
        gr1 = 18150 * 0.1
        gr2 = (73800 - 18150) * 0.15
        gr3 = (148850 - 73800) * 0.25
        gr4 = (226850 - 148850) * 0.28
        gr5 = (405100 - 226850) * 0.33
        gr6 = (457600 - 405100) * 0.35
        gr7 = (annual_income - 457600) * 0.396
        
    print(gr1 + gr2 + gr3 + gr4 + gr5 + gr6 + gr7)
    pass


def single():                                           # Вычисление суммы налога для родителя-одиночки
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