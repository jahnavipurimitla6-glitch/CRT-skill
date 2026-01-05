priceItem=input().strip()
prime_digit={'2','3','5','7'}
discount=sum(int(digit) for digit in priceItem if digit in prime_digit)
print(discoumnt)
