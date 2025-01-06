import random
from datetime import datetime, timedelta
from ui.controller.DbManager import DBManager


# Olası değerler
cities = ["İstanbul (Avrupa)", "İstanbul (Anadolu)", "Ankara", "İzmir", "Kütahya"]
airlines = ["Türk Hava Yolları", "Pegasus Hava Yolları", "Onur Air"]
available_seats = 36
price_multiples = [i for i in range(200, 1000, 50)]  # 200'den büyük 50'nin katları
departure_hours = ["10:30:00", "12:00:00", "13:30:00", "15:00:00", "16:30:00", "18:00:00"]

def generate_flight_data(base_date):
    """
    Rastgele uçuş verisi oluşturur.
    :param base_date: Gün/ay/yıl formatında bir tarih string'i
    :return: Rastgele uçuş verilerini içeren bir sözlük
    """
    # Tarihi datetime nesnesine çevir
    try:
        departure_base_date = datetime.strptime(base_date, "%d/%m/%Y")
    except ValueError:
        print("Hatalı tarih formatı! Lütfen 'gün/ay/yıl' formatında girin.")
        return None

    # Rastgele değerler seç
    # from_city, to_city = random.sample(cities, 2)  # Şehirler farklı olacak
    # Şehirleri seç
    while True:
        from_city, to_city = random.sample(cities, 2)
        if "İstanbul" in from_city and "İstanbul" in to_city:  # Aynı şehir kontrolü (İstanbul'un iki yakası)
            continue
        break  # Geçerli şehirler seçildi, döngüden çık
    airline = random.choice(airlines)
    price = random.choice(price_multiples)
    departure_hour = random.choice(departure_hours)

    # Kalkış zamanı belirle
    departure_datetime = departure_base_date + timedelta(hours=int(departure_hour.split(":")[0]),
                                                         minutes=int(departure_hour.split(":")[1]))

    # Varış zamanını rastgele ekle: 1 ila 4 saat arası ekleme yap
    arrival_datetime = departure_datetime + timedelta(hours=random.randint(1, 4), minutes=random.choice([0, 30]))
    arrival_date = arrival_datetime.strftime("%d/%m/%Y %H:%M:%S")

    # Uçuş sözlüğünü oluştur
    flight_data = {
        "from": from_city,
        "to": to_city,
        "airline": airline,
        "available_seats": available_seats,
        "price": price,
        "arrival_date": arrival_date,
        "departure_date": departure_datetime.strftime("%d/%m/%Y %H:%M:%S")
    }

    return flight_data

# MongoDB'ye veri ekleme kısmı
def insert_flights_to_mongo(flight_list):
    """
    Uçuş verilerini MongoDB'ye ekler.
    :param flight_list: Eklenecek uçuş verilerinin listesi
    """
    try:
        db = DBManager
        db.connect()
        collection = db._flight_collection

        # Veri ekleme
        result = collection.insert_many(flight_list)
        print(f"{len(result.inserted_ids)} adet uçuş MongoDB'ye eklendi.")
    except Exception as e:
        print(f"MongoDB'ye eklenirken hata oluştu: {e}")

# Kullanım
base_date_input = "15/12/2024"  # Başlangıç tarihi
flight_data_list = []

for _ in range(5):  # 5 uçuş verisi oluştur
    flight = generate_flight_data(base_date_input)
    if flight:
        flight_data_list.append(flight)

# MongoDB'ye veri ekle
if flight_data_list:
    insert_flights_to_mongo(flight_data_list)
