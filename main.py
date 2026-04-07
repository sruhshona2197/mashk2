# 1
def menu():
    print("\n--- TALABALAR TIZIMI ---")
    print("1. Talaba qo‘shish")
    print("2. Talabalarni ko‘rish")
    print("3. Talaba qidirish")
    print("4. Talabani o‘chirish")
    print("5. Chiqish")

def talaba_qoshish(baza):
    ism = input("Ism kiriting: ")
    yosh = int(input("Yosh kiriting: "))
    kurs = input("Kurs kiriting: ")

    talaba = {
        "ism": ism,
        "yosh": yosh,
        "kurs": kurs
    }

    baza.append(talaba)
    print("✅ Talaba qo‘shildi!")

def talaba_korish(baza):
    if not baza:
        print("❌ Hech qanday talaba yo‘q")
        return

    for i, t in enumerate(baza, 1):
        print(f"{i}. {t['ism']} | {t['yosh']} yosh | {t['kurs']}")

def talaba_qidirish(baza):
    ism = input("Qidirilayotgan ism: ").lower()
    topildi = False

    for t in baza:
        if t["ism"].lower() == ism:
            print(f"🔎 Topildi: {t['ism']} | {t['yosh']} | {t['kurs']}")
            topildi = True

    if not topildi:
        print("❌ Topilmadi")

def talaba_ochirish(baza):
    ism = input("O‘chiriladigan talaba ismi: ").lower()

    for t in baza:
        if t["ism"].lower() == ism:
            baza.remove(t)
            print("🗑 Talaba o‘chirildi")
            return

    print("❌ Bunday talaba yo‘q")

def main():
    baza = []

    while True:
        menu()
        tanlov = input("Tanlang (1-5): ")

        if tanlov == "1":
            talaba_qoshish(baza)
        elif tanlov == "2":
            talaba_korish(baza)
        elif tanlov == "3":
            talaba_qidirish(baza)
        elif tanlov == "4":
            talaba_ochirish(baza)
        elif tanlov == "5":
            print("Dastur tugadi 👋")
            break
        else:
            print("❗ Noto‘g‘ri tanlov")

if __name__ == "__main__":
    main()
