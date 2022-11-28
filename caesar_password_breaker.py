print("CAESAR PASSWORD BREAKER")
print("Made for lazy people :)")

alpha = "abcdefghijklmnopqrstuvwxyz"  # alpha = alphabeth

text = input("Enter the password: ")
shift = int(input("Enter the shift value: "))
enc_text = ""       # enc = encrypted

for i in range(len(text)):
    enc_idx = (alpha.index(text[i]) - shift)
    if enc_idx < 0:
        enc_idx = 26 + enc_idx
    enc_text = enc_text + alpha[enc_idx]    # idx = index
print("text is : ",enc_text)