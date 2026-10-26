qiymet = float(input("Məhsulun qiymətini daxil et: "))
say = int(input("Alınacaq məhsulların sayını daxil edin: "))
verilen_pul = float(input("Verdiyiniz pul məbləğini daxil edin: "))

umumi_qiymet = qiymet * say
qaliq = verilen_pul - umumi_qiymet

print(f"Ümumi qiymət: {umumi_qiymet} AZN")
print(f"Qalan pul: {qaliq} AZN")