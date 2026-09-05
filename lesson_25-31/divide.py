try:
    a=int(input('what is first num'))
    b=int(input('WHAT IS SEcond num'))

    print(a/b)
except ZeroDivisionError:
    print('zero division exception')
except ValueError as e:
    print('value error type integer ',e)
except:
    print('unknown exception')