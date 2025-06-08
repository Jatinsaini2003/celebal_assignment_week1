def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        dec_str = str(i).rjust(width)
        oct_str = oct(i)[2:].rjust(width)
        hex_str = hex(i)[2:].upper().rjust(width)
        bin_str = bin(i)[2:].rjust(width)
        print(dec_str, oct_str, hex_str, bin_str)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)