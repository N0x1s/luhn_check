class Luhn:
    @staticmethod
    def luhn_check(n):
        r = [int(_) for _ in str(n)[::-1]]
        checksum = (sum(r[0::2]) + sum(sum(divmod(d*2, 10))
                                       for d in r[1::2]))
        return checksum % 10 == 0 and bool(checksum)
