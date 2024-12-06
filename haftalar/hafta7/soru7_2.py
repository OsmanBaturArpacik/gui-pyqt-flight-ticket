import pymongo as m

if __name__ == '__main__':
	myClient = m.MongoClient("mongodb://localhost:27017")
	print(myClient.list_database_names())
	dblist = myClient.list_database_names()
	if "universite" in dblist:
		print("exist")

	db = myClient["universite"]
	ogrenciler = db["ogrenciler"] # _id, ad, yas, bolum, gno
	dersler = db["dersler"] # _id, ders_adi, kredi, ogretmen_ismi
	ogretmenler = db["ogretmenler"] # _id, ad, bolum, deneyim

	print(db.list_collection_names())

	ogrenciler.insert_many([
		{"_id": 1, "ad": "cengiz", "yas": 28, "bolum": "yazilim muhendisligi", "gno": 3.4},
		{"_id": 2, "ad": "islam", "yas": 22, "bolum": "yazilim muhendisligi", "gno": 2.4},
		{"_id": 3, "ad": "osman", "yas": 19, "bolum": "bilgisayar muhendisligi", "gno": 1.6}])

	dersler.insert_many([
		{"_id": 1, "ders_adi": "Fizik-1", "kredi": 6, "ogretmen_ismi": "Muhammet"},
		{"_id": 2, "ders_adi": "Mat-1", "kredi": 1, "ogretmen_ismi": "Cengiz"},
		{"_id": 3, "ders_adi": "Fizik-2", "kredi": 3, "ogretmen_ismi": "Ali"}])

	ogretmenler.insert_many([
		{"_id": 1, "ad": "Muhammet", "bolum": "Elektrik Elektronik", "deneyim": 8},
		{"_id": 2, "ad": "Cengiz", "bolum": "Matematik", "deneyim": 10},
		{"_id": 3, "ad": "ALi", "bolum": "Elektrik Elektronik", "deneyim": 1}])

	print(db.list_collection_names())


	for ogrenci in ogrenciler.find():
		print(ogrenci)

	for ders in dersler.find():
		print(ders)

	for ogretmen in ogretmenler.find():
		print(ogretmen)

# belirli bir ifadeyle baslayan isimlerin oldugu documanları listeleylim
	for ogrenci in ogrenciler.find({"ad": "cengiz"}):
		print(ogrenci)

# genel not ortalamasına gore azalan sirada listele
	for ogrenci in ogrenciler.find().sort("gno",-1):
		print(ogrenci)

	dersler.insert_one({"_id": 4, "ders_adi": "algoritma analizi", "kredi": 2, "ogretmen_ismi": "Cengiz"})
# dersin adinda algoritma gecenleri listeleyelim
	for ders in dersler.find({"ders_adi": {"$regex": "algoritma"}}):
		print(ders)

	ogretmenler.insert_one({"_id": 4, "ad": "Selami", "bolum": "Elektrik Elektronik", "deneyim": 5})
# deneyim 5 yıl olan öğretmenleri listeleyelim
	for ogretmen in ogretmenler.find({"deneyim": 5}):
		print(ogretmen)

	ogrenciler.insert_one({"_id": 4, "ad": "taha", "yas": 22, "bolum": "elektrik muhendisligi", "gno": 3.85})
# gnosu 3 ile 4 arasında olan öğrnvcileri lsiteleyim
	for ogrenci in ogrenciler.find({"gno": {"$gte": 3, "$lt": 4}}):
		print(ogrenci)

	ogrenciler.insert_one({"_id": 5, "ad": "Ahmet", "yas": 22, "bolum": "elektrik muhendisligi", "gno": 2.5})
# adi ahmet olan ogrencieerin gno'sunu 3.5 olarak guncelleyelim
	ogrenciler.update_one({"ad": "Ahmet"}, {"$set": {"gno": 3.5}})
	for ogrenci in ogrenciler.find({"_id": 5}):
		print(ogrenci)

	for ogrenci in ogrenciler.find({"bolum": {"$regex": "bilgisayar"}}):
		print(ogrenci)
# bolumu bilgisayar olan tum ogrencielrin yaşlarını bir artırarak güncelleyelim
	ogrenciler.update_many({"bolum": {"$regex": "bilgisayar"}}, {"$inc": {"yas": 1}})

	dersler.insert_one({"_id": 5, "ders_adi": "yapay zeka", "kredi": 2, "ogretmen_ismi": "Ali"})
# deresler koleksiyonunda ders_adi yapay zeka olan dersin kredisini 5 yapalim ve zorunlu-ders: True olarakyeni bir alan ekleyelim
	dersler.update_one({"ders_adi": "yapay zeka"}, {"$set": {"kredi": 5, "zorunlu-ders": True}})
	for ders in dersler.find({"_id": 5}):
		print(ders)

	for ogrenci in ogrenciler.find({"gno": {"$gte": 0, "$lt": 2.5}}):
		print(ogrenci)

# gno degeri 2.5 dan dusuk tum ogrencileri sileelim
	ogrenciler.delete_many({"gno": {"$gte": 0, "$lt": 2.5}})
