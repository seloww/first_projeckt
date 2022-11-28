print("CAESAR PASSWORD MAKER")
print("Made for lazy people :)")

alpha = "abcdefghijklmnopqrstuvwxyz"  # alpha = alphabeth

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
enc_text = ""       # enc = encrypted

for i in range(len(text)):
    enc_idx = (alpha.index(text[i]) + shift)%29
    enc_text=enc_text+alpha[enc_idx]
print("password is : ",enc_text)