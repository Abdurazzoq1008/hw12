# =============================================================
# just son detector
# =============================================================
juft_son = int(input("Juft sonni kiriting: "))

if juft_son % 2 == 0 :
    print("Rahmat!")
else:
    print("Bu juft son emas.")

# ==============================================================
# kassir demo
# ==============================================================
while True:
    buyruq1 = input('Boshlash uchun enterni bosing.')
    while True:
            if buyruq1 == "":
               yosh = int(input('Yoshinggizni kiriting: '))
            if yosh > 60 or yosh < 4 :
                 print('Sizga bepul.')
            elif yosh <= 18:
               print("Sizga bitta chipta 10 000 so'm.")
            else:
              print("Sizga bitta chipta 20 000 so'm.")

            buyruq = "stop"
            davom = input("Yana davom etamizmi? To'xtatish uchun 'stop' deb yozing: ")
            if davom.lower() == buyruq :
              print("Dastur to'xtadi.")

              break

    break
# ============================================================================================
# comparitor
# ============================================================================================

son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))

if son1 > son2 :
    print(son1, ">", son2)
else:
    print(son1 ,"<", son2)

# =============================================================================================
# e shop seller.
# =============================================================================================
while True:
      products = input("Qidirayotgan mahsulotingizni yozing: ").strip().capitalize()
      shop_producs = ["Mayiz", "Xolva", "Tarvuz", "Qovun", "Guruch"]

      if products in shop_producs:
             print("Savatga qo'shildi:", products)
      else:
          print("Bizda bu turdagi mahsulot yo'q:", products)
          break
# ===============================================================================================
# calculator
# ===============================================================================================

son = int(input("Istalgan butun son kiriting: "))

for boluvchi in range(2, 100000):
    if son % boluvchi == 0:
        print(son, "soni", boluvchi, "ga qoldiqsiz bo'linadi")