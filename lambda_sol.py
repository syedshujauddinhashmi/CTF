def rev_in(e_str):
    parts = e_str.split('_')
    base36_d = [chr(int(part, 36) + 10) for part in parts]
    joined = ''.join(base36_d)
    return joined

def rev_ch(e_str):
    xor_rev = ''.join(chr(123 ^ ord(c)) for c in e_str)
    shift3 = ''.join(chr(ord(c) + 3) for c in xor_rev)
    shift12 = ''.join(chr(ord(c) - 12) for c in shift3)
    return shift12

e_str = "16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r"

result = rev_in(e_str)
flag = rev_ch(result)

print("flag:", flag)
