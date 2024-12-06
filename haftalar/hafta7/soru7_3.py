import pymongo as mango

if __name__ == '__main__':
	myClient = mango.MongoClient("mongodb://localhost:27017")
	print(myClient.list_database_names())
	dblist = myClient.list_database_names()
	if "universite" in dblist:
		print("exist")

	db = myClient["universite"]
	ogrenciler = db["ogrenciler"] # _id, ad, yas, bolum, gno
	dersler = db["dersler"] # _id, ders_adi, kredi, ogretmen_ismi
	ogretmenler = db["ogretmenler"] # _id, ad, bolum, deneyim

	print(db.list_collection_names())

	ogrenciler.insert_many(
		[
			{"_id": 1,	"ad": "Ayse",	"yas": 23,	"bolum": "Yazilim Muhendisligi",	"gno": 3.41},
			{"_id": 2,	"ad": "Osman",	"yas": 56,	"bolum": "Yazilim Muhendisligi",	"gno": 3.54},
			{"_id": 3,	"ad": "Zeynep",	"yas": 32,	"bolum": "Elektrik Muhendisligi",	"gno": 3.98},
			{"_id": 4,	"ad": "Ahmet",	"yas": 18,	"bolum": "Bilgisayar Muhendisligi",	"gno": 2.44},
			{"_id": 5,	"ad": "Tezcan",	"yas": 19,	"bolum": "Yazilim Muhendisligi",	"gno": 2.23},
			{"_id": 6,	"ad": "Esra",	"yas": 20,	"bolum": "Bilgisayar Muhendisligi",	"gno": 1.35}
		]
	)

	dersler.insert_many(
		[
			{"_id": 1,	"ders_adi": "Fizik-1",				"kredi": 5,	"ogretmen_ismi": "Ahmet"},
			{"_id": 2,	"ders_adi": "Fizik-2",				"kredi": 6,	"ogretmen_ismi": "Serap"},
			{"_id": 3,	"ders_adi": "Mat-1",				"kredi": 5,	"ogretmen_ismi": "Selim"},
			{"_id": 4,	"ders_adi": "Algoritma Analizi",	"kredi": 4,	"ogretmen_ismi": "Derya"},
			{"_id": 5,	"ders_adi": "Yapay Zeka",			"kredi": 2,	"ogretmen_ismi": "Ece"},
			{"_id": 6,	"ders_adi": "Veri Madenciliği",		"kredi": 3,	"ogretmen_ismi": "Furkan"}
		]
	)

	ogretmenler.insert_many(
		[
			{"_id": 1,	"ad": "Ahmet",	"bolum": "Fizik",					"deneyim": 5},
			{"_id": 2,	"ad": "Serap",	"bolum": "Fizik",					"deneyim": 10},
			{"_id": 3,	"ad": "Selim",	"bolum": "Matematik",				"deneyim": 3},
			{"_id": 4,	"ad": "Derya",	"bolum": "Bilgisayar Mühendisliği", "deneyim": 5},
			{"_id": 5,	"ad": "Ece",	"bolum": "Bilgisayar Mühendisliği", "deneyim": 7},
			{"_id": 6,	"ad": "Furkan",	"bolum": "Bilgi Teknolojileri", 	"deneyim": 4}
		]
	)

	print(db.list_collection_names())

	for ogrenci in ogrenciler.find():
		print(ogrenci)

	for ders in dersler.find():
		print(ders)

	for ogretmen in ogretmenler.find():
		print(ogretmen)

# belirli bir ifadeyle baslayan isimlerin oldugu documanları listeleylim
	for ogrenci in ogrenciler.find({"ad": {"$regex": "^e", "$options": "i"}}):
		print(ogrenci)

# genel not ortalamasına gore azalan sirada listeleyelim  eknot: .limit(3)
	for ogrenci in ogrenciler.find().sort("gno",-1):
		print(ogrenci)

# dersin adinda algoritma gecenleri listeleyelim
	for ders in dersler.find({"ders_adi": {"$regex": "algoritma", "$options": "i"}}):
		print(ders)

# deneyim 5 yil olan ogretmenleri listeleyelim
	for ogretmen in ogretmenler.find({"deneyim": 5}):
		print(ogretmen)

# gnosu 3 ile 4 arasinda olan ogrencileri listeleyelim
	for ogrenci in ogrenciler.find({"gno": {"$gte": 3, "$lt": 4}}).sort("yas", 1):
		print(ogrenci)

# adi "Ahmet" olan ogrencileri gno'sunu 3.5 olarak guncelleyelim
	ogrenciler.update_one({"ad": "Ahmet"}, {"$set": {"gno": 3.5}})

	# kontrol
	for ogrenci in ogrenciler.find({"_id": 4}):
		print(ogrenci)

# bolumu "Bilgisayar" olan tum ogrencielrin yaşlarını bir artırarak güncelleyelim
	ogrenciler.update_many({"bolum": {"$regex": "Bilgisayar"}}, {"$inc": {"yas": 1}})

	# kontrol
	for ogrenci in ogrenciler.find({"bolum": {"$regex": "Bilgisayar"}}):
		print(ogrenci)

# dersler koleksiyonunda ders_adi "Yapay Zeka" olan dersin kredisini 5 yapalim ve zorunlu-ders: True olarakyeni bir alan ekleyelim
	dersler.update_one({"ders_adi": "Yapay Zeka"}, {"$set": {"kredi": 5, "zorunlu-ders": True}})

	# kontrol
	for ders in dersler.find({"_id": 5}):
		print(ders)

# gno degeri 2.5 dan dusuk tum ogrencileri sileelim

	# kontrol
	for ogrenci in ogrenciler.find({"gno": {"$gte": 0, "$lt": 2.5}}):
		print(ogrenci)

	ogrenciler.delete_many({"gno": {"$gte": 0, "$lt": 2.5}})

	# kontrol
	for ogrenci in ogrenciler.find():
		print(ogrenci)


	myClient.drop_database("universite")