import fraction as fr
import sys

if __name__ == "__main__":
    try:
        _, num, denom = sys.argv
        fract_1 = fr.Fraction(int(num), int(denom))
        fract_2 = fr.Fraction(-1, 2)
        print(fract_1)
        print(fract_2)
        print(f"{fract_1} < {fract_2} => {fract_1 <= fract_2}")
        print(f"{fract_1} + {fract_2} = {fract_1 + fract_2}")
        print(f"{fract_1} - {fract_2} = {fract_1 - fract_2}")
        print(f"{fract_1} * {fract_2} = {fract_1 * fract_2}")
        print(f"{fract_1} : {fract_2} = {fract_1 / fract_2}")
        print(f"{fract_1} < 2 => {2 > fract_1}")
        print(f"{fract_1} + 2 = {2 + fract_1}")
        print(f"{fract_1} - 2 = {fract_1 - 2}")
        print(f"{fract_1} * 2 = {fract_1 * 2}")
        print(f"{fract_1} : 2 = {fract_1 / 2}")
    except (TypeError, ZeroDivisionError) as error:
        print(error)



