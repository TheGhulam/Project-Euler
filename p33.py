from fractions import Fraction

# def cancel(n, d):
#     n_digits = [i for i in str(n)]
#     d_digits = [i for i in str(d)]
#     for n in n_digits:
#         for d in d_digits:
#             if n == d:
#                 n_digits.remove(n)
#                 d_digits.remove(n)
#     return (int("".join(n_digits)), int("".join(d_digits)))

def main():
    product = 1

    for i in range(10, 100):
        for j in range(i+1, 100):
            # Intersection of two sets
            common = list(set(str(i)) & set(str(j)))
            if len(common) != 0:
                if common[0] != '0':
                    num = list(str(i))
                    den = list(str(j))
                    # Remove common element from numerator and denominator
                    num.remove(common[0])
                    den.remove(common[0])
                    # Check if the value of num and den are not equal to 0
                    if num[0] != '0' and den[0] != '0':
                        # Check if they satisfy the equation condition
                        if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):
                            product *= Fraction(i,j)

    print(product.denominator)

if __name__ == "__main__":
    main()
