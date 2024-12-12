import pymongo

class DBManager:
    # Singleton design pattern ile veritabanı bağlantısını yönetiyoruz
    _client = None
    _db = None
    _user_collection = None

    @classmethod
    def connect(cls):
        if cls._client is None:
            # Bağlantıyı sadece ilk kez oluşturuyoruz
            cls._client = pymongo.MongoClient("mongodb://localhost:27017")
            cls._db = cls._client["ticket_app_db"]
            cls._user_collection = cls._db["user"]
            cls._ticket_collection = cls._db["ticket"]
            cls._flight_collection = cls._db["flight"]
            print("Veritabanına bağlanıldı.")
        return cls._user_collection

    @classmethod
    def close(cls):
        if cls._client:
            cls._client.close()
            print("Veritabanı bağlantısı kapatıldı.")
