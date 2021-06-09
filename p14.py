def length_of_collatz_sequence(n, count=1):
    if n == 1:
        return count
    elif n % 2 == 0:
        return length_of_collatz_sequence((n/2), count+1)
    else:
        return length_of_collatz_sequence((3*n + 1), count+1)

def main():
    max_i = 0
    max_s = 0
    for i in range(1000_000-1, 22, -1):
        s = length_of_collatz_sequence(i)
        if s > max_s:
            max_s = s
            max_i = i
    print(max_i)


if __name__ == "__main__":
    # print(length_of_collatz_sequence(13))
    main()
