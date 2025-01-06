import random
from datetime import datetime, timedelta
from ui.controller.DbManager import DBManager
from itertools import permutations

# Olası şehirler
cities = ["İstanbul (Avrupa)", "İstanbul (Anadolu)", "Ankara", "İzmir", "Kütahya"]
airlines = ["Türk Hava Yolları", "Pegasus Hava Yolları", "Onur Air"]
available_seats = 36
price_multiples = [i for i in range(200, 1000, 50)]  # 200'den büyük 50'nin katları
departure_hours = ["10:30:00", "12:00:00", "13:30:00", "15:00:00", "16:30:00", "18:00:00"]


def generate_flight_data(from_city, to_city, base_date):
    """
    Rastgele uçuş verisi oluşturur.
    :param from_city: Kalkış şehri
    :param to_city: Varış şehri
    :param base_date: Gün/ay/yıl formatında bir tarih string'i
    :return: Rastgele uçuş verilerini içeren bir sözlük
    """
    # Tarihi datetime nesnesine çevir
    try:
        departure_base_date = datetime.strptime(base_date, "%d/%m/%Y")
    except ValueError:
        print("Hatalı tarih formatı! Lütfen 'gün/ay/yıl' formatında girin.")
        return None

    # Şirket seçimi, fiyat ve kalkış saati belirleme
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


def generate_all_flights(base_date):
    """
    Tüm şehir kombinasyonları için uçuş verilerini oluşturur.
    :param base_date: Gün/ay/yıl formatında bir tarih string'i
    :return: Tüm uçuş verilerini içeren liste
    """
    flight_data_list = []

    # Şehirlerin tüm kombinasyonlarını oluştur
    for from_city, to_city in permutations(cities, 2):  # Aynı şehirler arasında uçuş yapılmayacak
        # İstanbul (Avrupa) -> İstanbul (Anadolu) gibi uçuşları engellemek için kontrol
        if "İstanbul" in from_city and "İstanbul" in to_city:
            continue  # Bu durumda, İstanbul içi uçuşları atla

        flight = generate_flight_data(from_city, to_city, base_date)
        if flight:
            flight_data_list.append(flight)

    return flight_data_list


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
base_date_input = "4/1/2024"  # Başlangıç tarihi
flight_data_list = generate_all_flights(base_date_input)

# MongoDB'ye veri ekle
if flight_data_list:
    insert_flights_to_mongo(flight_data_list)
