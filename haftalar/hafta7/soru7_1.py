import pymongo as m

if __name__ == '__main__':
	myClient = m.MongoClient("mongodb://localhost:27017")
	print(myClient.list_database_names())
	dblist = myClient.list_database_names()
	if "admin" in dblist:
		print("exist")

	db = myClient["db_okul_yonetim"]
	ogrenciler = db["ogrenciler"]
	print(db.list_collection_names())

	ogrenci = {"ad": "Ahmet", "yas": 20, "bolum": "yazilim muhendisligi"}
	ogrenciler.insert_one(ogrenci)

	ogrenciler_listesi = [
		{"ad": "Osman", "yas": 19, "bolum": "bilgisayar muhendisligi"},
		{"ad": "Cengiz", "yas": 22, "bolum": "yazilim muhendisligi"},
		{"ad": "Batur", "yas": 25, "bolum": "elektrik muhendisligi"}
	]

	ogrenciler_listesi = [
		{"ad": "Ali", "yas": 20, "bolum": "bilgisayar muhendisligi"},
		{"ad": "Murat", "yas": 21, "bolum": "yazilim muhendisligi"},
		{"ad": "Emre", "yas": 23, "bolum": "elektrik muhendisligi"},
		{"ad": "Ayse", "yas": 22, "bolum": "matematik"},
		{"ad": "Fatma", "yas": 24, "bolum": "insaat muhendisligi"},
		{"ad": "Can", "yas": 20, "bolum": "mekanika muhendisligi"},
		{"ad": "Zeynep", "yas": 21, "bolum": "kimya muhendisligi"},
		{"ad": "Hakan", "yas": 26, "bolum": "tarih"},
		{"ad": "Eda", "yas": 23, "bolum": "elektrik muhendisligi"},
		{"ad": "Ahmet", "yas": 22, "bolum": "fizik"},
		{"ad": "Elif", "yas": 25, "bolum": "psikoloji"},
		{"ad": "Mehmet", "yas": 23, "bolum": "endustri muhendisligi"},
		{"ad": "Gizem", "yas": 24, "bolum": "beslenme ve diyetetik"},
		{"ad": "Berk", "yas": 22, "bolum": "ingilizce"},
		{"ad": "Kadir", "yas": 21, "bolum": "isletme"},
		{"ad": "Seda", "yas": 25, "bolum": "turizm"},
		{"ad": "Okan", "yas": 23, "bolum": "medya ve iletisim"},
		{"ad": "Merve", "yas": 20, "bolum": "kamu yonetimi"},
		{"ad": "Deniz", "yas": 24, "bolum": "ulusal guvenlik ve savunma"},
		{"ad": "Baran", "yas": 22, "bolum": "sosyoloji"}
	]

	ogrenciler.insert_many(ogrenciler_listesi)

	for ogrenci in ogrenciler.find():
		print(ogrenci)

	for ogrenci in ogrenciler.find({"yas": 22}):
		print(ogrenci)

	ogrenci = ogrenciler.find_one({"ad": "Cengiz"})

	ogrenciler.update_one({"ad": "Osman"}, {"$set": {"yas": 20, "bolum": "insaat muhendisligi"}})

	ogrenciler.update_many({"bolum": "yazilim muhendisligi"}, {"$set": {"yas": 47}})

	ogrenciler.delete_one({"ad": "Batur"})

	ogrenciler.delete_many({"yas": 20})
	# 1 ascending, -1 descending
	for ogrenci in ogrenciler.find().sort("yas",1):
		print(ogrenci)

	for ogrenci in ogrenciler.find().sort([("bolum",1), ("yas", -1)]):
		print(ogrenci)

	for ogrenci in ogrenciler.find().sort([("bolum", 1), ("yas", -1)]).limit(3):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"ad": {"$regex": "^A"}}):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"ad": {"$regex": "t$"}}):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"bolum": {"$regex": "yazilim"}}):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"ad": {"$regex": "ahmet", "$options":"i"}}):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"ad": {"$regex": "^a", "$options":"i"}}).sort("yas", -1).limit(2):
		print(ogrenci)
