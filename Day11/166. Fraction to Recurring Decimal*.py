class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            sign = "-"
            if numerator < 0:
                numerator = -numerator
            else:
                denominator = -denominator
        else:
            sign = ""
            
        q, r = divmod(numerator, denominator)
        res = str(q)
        dic = {}
        digits = []
        r *= 10
        i = 0
        while True:
            q, r = divmod(r, denominator)
            if r == 0:
                if q != 0:
                    digits.append(q)
                    return sign+res +"."+"".join(map(str,digits))
                else:
                    if len(digits) > 0:
                        return sign+res+ "." + "".join(map(str,digits))
                    else:
                        return sign+res
            elif not (q,r) in dic:
                digits.append(q)
                dic[(q,r)] = i
                r *= 10
                i += 1
            else:
                index = dic[(q,r)]
                non_repeat = "".join(map(str,digits[:index]))
                repeat = "("+"".join(map(str,digits[index:]))+")"
                return sign+res+"."+non_repeat+repeat