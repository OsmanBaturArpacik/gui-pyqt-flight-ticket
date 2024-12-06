
def printOgrenci(ogrenci):
    print(f"ogrencinin adi: {ogrenci["ad"]}\n"
          f"yasi: {ogrenci["yas"]}\n"
          f"notlar: {ogrenci["notlar"]}\n"
          f"dersler: {ogrenci["dersler"]}\n"
          f"gezdigi yerler: {ogrenci["gezdigi_yerler"]}")

def printType(ogrenci):
    print(f"ogrencinin adi: {type(ogrenci["ad"])}\n"
          f"yasi: {type(ogrenci["yas"])}\n"
          f"notlar: {type(ogrenci["notlar"])}\n"
          f"dersler: {type(ogrenci["dersler"])}\n"
          f"gezdigi yerler: {type(ogrenci["gezdigi_yerler"])}")

if __name__ == '__main__':
    # TEK OGRENCİ

    ogrenci = {
        "ad": "osman",
        "yas": 20,
        "notlar": [70,80,60],
        "dersler": {"matematik", "Fizik", "Biyoloji"},
        "gezdigi_yerler": ("İstanbul", "Ankara", "Kütahya"),
        }

    print("Ogrenci-1:\n")
    printOgrenci(ogrenci)

    # BİRDEN FAZLA OGRENCİ

    ogrenciler = {
        "ogrenci1": {
                "ad": "osman",
                "yas": 20,
                "notlar": [70, 80, 60],
                "dersler": {"matematik", "Fizik", "Biyoloji"},
                "gezdigi_yerler": ("İstanbul", "Ankara", "Kütahya")
        },
        "ogrenci2": {
                "ad": "batur",
                "yas": 22,
                "notlar": [30, 20, 50],
                "dersler": {"resim", "kimya", "beden"},
                "gezdigi_yerler": ("Edirne", "Adana", "Kütahya")
        }
    }
    print()
    print("Ogrenci-1:\n")
    printOgrenci(ogrenciler["ogrenci1"])
    print()
    print("Ogrenci-2:\n")
    printOgrenci(ogrenciler["ogrenci2"])







    printType(ogrenci)




    ogrenciler = {
        [
            {
                "ad": "osman",
                "yas": 20,
                "notlar": [70, 80, 60],
                "dersler": {"matematik", "Fizik", "Biyoloji"},
                "gezdigi_yerler": ("İstanbul", "Ankara", "Kütahya")
            },
            {
                "ad": "batur",
                "yas": 22,
                "notlar": [30, 20, 50],
                "dersler": {"resim", "kimya", "beden"},
                "gezdigi_yerler": ("Edirne", "Adana", "Kütahya")
            }
        ]
    }
