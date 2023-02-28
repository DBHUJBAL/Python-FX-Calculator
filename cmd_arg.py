import sys
n = len(sys.argv)
for i in range(1, n):
    try:
        con_code = sys.argv[1] + sys.argv[3]
        if con_code.casefold() == 'audusd':
            exchange_rate = 0.8371
        elif con_code.casefold() == 'cadusd':
            exchange_rate = 0.8711
        elif con_code.casefold() == 'usdcny':
            exchange_rate = 6.1715
        elif con_code.casefold() == 'eurusd':
            exchange_rate = 1.2315
        elif con_code.casefold() == 'gbpusd':
            exchange_rate = 1.5683
        elif con_code.casefold() == 'nzdusd':
            exchange_rate = 0.7750
        elif con_code.casefold() == 'usdjpy':
            exchange_rate = 119.95
        elif con_code.casefold() == 'eurczk':
            exchange_rate = 27.6028
        elif con_code.casefold() == 'eurdkk':
            exchange_rate = 7.4450
        elif con_code.casefold() == 'eurnok':
            exchange_rate = 8.6651

        converted_amt = float(sys.argv[2]) * exchange_rate
        print("\n From: {0}, {1} ".format(sys.argv[1].upper(), sys.argv[2]))
        print("\n To: ", sys.argv[3].upper())
        if sys.argv[3].casefold() == 'jpy':
            print("\n = {0} {1}".format(sys.argv[3].upper(), int(converted_amt)))
            break
        print("\n = {0} {1}".format(sys.argv[3].upper(), round(converted_amt, 2)))
        break
    except NameError:
        print("\n Unable to find rate for {0} / {1} ".format(sys.argv[1].upper(), sys.argv[3].upper()))
        break

