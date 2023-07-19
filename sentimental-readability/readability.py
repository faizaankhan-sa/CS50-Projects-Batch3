from cs50 import get_string

txt = get_string("Text: ")

sen = 0
wor = 1
let = 0

for x in txt:
    if x.isalpha():
        let += 1
    elif x == " ":
        wor += 1
    elif x == "!" or x == "?" or x == ".":
        sen += 1

clindex = 0.0588 * (let/wor*100) - 0.296 * (sen/wor*100) - 15.8
if clindex < 1:
    print("Before grade 1")
elif clindex >= 16:
    print("Grade 16+")
else:
    print("Grade ", round(clindex))
