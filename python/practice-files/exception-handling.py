try:
    data={'A':1,'B':2}
    # print(data['C'])
    print(10/0)
except KeyError:
    print('Exception in the code')
except ZeroDivisionError:
    print('ZerodivisionError')
finally:
    print('FInally cleared')