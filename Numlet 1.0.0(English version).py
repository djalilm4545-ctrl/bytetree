while True:
    print('number to character')
    number = input('enter a number(between 1 and 9999):')
    lst1 = [1,2,3,4,5,6,7,8,9]
    english_numbers_one_digit = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
        ]

    english_numbers_two_digit = [
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"

    ]
    english_numbers_three_digit = [
        "one hundred", "two hundred", "three hundred", "four hundred",
        "five hundred", "six hundred", "seven hundred", "eight hundred",
        "nine hundred"

        ]
    s_numbers = ["one hundred" , "one thousand"]
    def one_digit(x):   
        x = int(x) - 1
        form1 = f'{english_numbers_one_digit[x]}'
        return form1
    def two_digit(y):
        for i , i2 in y , '':
                i = int(i) - 2
                i2 = int(i2) - 1
                break
        if y[1]=='0':
            form2_1 = f'{english_numbers_two_digit[i]}'
            return form2_1    
        else:    
            form2 = f'{english_numbers_two_digit[i]}-{english_numbers_one_digit[i2]}'
            return form2   
    def three_digit(z):
            if z[1]=='1':
                for i3 , i4  , i4_1 in z , '':
                    two = i4 + i4_1 
                    i3 = int(i3) - 1
                    break
                form3_1 = f'{english_numbers_three_digit[i3]} and {one_digit(two)}'
                return form3_1
            elif z[1]=='0':
                if z[2]=='0':
                    form3_2 = f'{english_numbers_three_digit[int(z[0])-1]}'
                    return form3_2
                else:
                    for i3 , i4  , i4_1 in z , '':
                        two = i4 + i4_1
                        i3 = int(i3) - 1
                        i4_1 = int(i4_1)-1
                        res = int(i4_1)
                        break
                    form3_2 = f'{english_numbers_three_digit[i3]} and {english_numbers_one_digit[res]}'
                    return form3_2
            elif number[2]=='1':
                for i3 , i4  , i4_1 in z , '':
                    two = i4 + i4_1 
                    i3 = int(i3) - 1
                    break
                form3_3 = f'{english_numbers_three_digit[i3]} and {two_digit(two)}'
                return form3_3
            elif z[0]=='0':
                pass
            else:
                for i3 , *i4 in z , '':
                    i3 = int(i3) - 1
                    break
                form3 = f'{english_numbers_three_digit[i3]} and {two_digit(i4)}'
                return form3        
    def four_digit(a):
        if len(number) == 4:
           for i5 , *i7 in a , '':
                i5 = int(i5)-1
                break
           if a[1]=='0':
                if a[1]=='0' and a[2]=='1':
                    form4_1 = f'{english_numbers_one_digit[int(a[0])-1]} thousand and {one_digit(a[-2:])}'
                    return form4_1
                elif a[1]=='0' and a[2]=='0':
                    res2 = int(a[-1])-1
                    form4_1 = f'{english_numbers_one_digit[i5]} thousand and {english_numbers_one_digit[res2]}'
                    return form4_1
                else:
                    form4_1 = f'{english_numbers_one_digit[int(a[0])-1]} thousand and {two_digit(a[-2:])}'
                    return form4_1                    
           else:
                form4 = f'{english_numbers_one_digit[i5]} thousand and {three_digit(i7)}'
                return form4
          
            


    
    if number[0]=='0':
        print('first digit is 0!')
    elif len(number)>4:
        print('please enter a number between 1 and 9999.')
    else:    
        if int(number)<20:    
            print(one_digit(number))
        elif 100>int(number)>=20: 
            print(two_digit(number))
        elif int(number)==100:
            print(s_numbers[0])
        elif 1000>int(number)>100:
            print(three_digit(number))
        elif int(number)==1000:
            print(s_numbers[1])
        elif int(number)>1000:
            print(four_digit(number))
