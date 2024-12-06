import pymongo as mango
from prettytable import PrettyTable
from datetime import date

global myClient
global db
global tasks

def connectMongo():
	global myClient
	global db
	global tasks
	myClient = mango.MongoClient("mongodb://localhost:27017")
	print(myClient.list_database_names())
	dblist = myClient.list_database_names()
	if "task_management" in dblist:
		print("exist")

	db = myClient["task_management"]
	tasks = db["tasks"]
	# tasks.insert_one({"title": "title", "description": "description", "due_date": "due_date", "created_at": "created_at", "status": "status"})
	print(db.list_collection_names())

def add_task(title, description, due_date):
	today = date.today()
	today_str = f"{today.year}-{today.month}-{today.day}"
	task = {
		"title": title,
		"description": description,
		"due_date": due_date,
		"created_at": today_str,
		"status": "Pending"
	}
	id = tasks.insert_one(task)
	print(id)

def list_tasks():
	table = PrettyTable()
	table.field_names = ["ID", "Başlık", "Açıklama", "Son Tarih", "Oluşturulma tarihi", "Durum"]


	for task in tasks.find():
		table.add_row([task.get("_id", "N/A"), task.get("title", "N/A"), task.get("description", "N/A"), task.get("due_date", "N/A"), task.get("created_at", "N/A"), task.get("status", "N/A")])

	print(table)

def printOneTable(task):
	table = PrettyTable()
	table.field_names = ["ID", "Başlık", "Açıklama", "Son Tarih", "Oluşturulma tarihi", "Durum"]

	table.add_row([task.get("_id", "N/A"), task.get("title", "N/A"), task.get("description", "N/A"), task.get("due_date", "N/A"), task.get("created_at", "N/A"), task.get("status", "N/A")])

	print(table)

def update_task(title, status):
	task = {"title": title}
	update_task = {"$set": {"status": status}}
	tasks.update_one(task, update_task)
	printTask = tasks.find_one(task)
	printOneTable(printTask)

def delete_task(title):
	delete_task = {"title": title}
	task = tasks.find_one(delete_task)

	printOneTable(task)
	tasks.delete_one(delete_task)

def sortedByDate():
	table = PrettyTable()
	table.field_names = ["ID", "Başlık", "Açıklama", "Son Tarih", "Oluşturulma tarihi", "Durum"]
	for task in tasks.find().sort("due_date",-1):
		table.add_row([task.get("_id", "N/A"), task.get("title", "N/A"), task.get("description", "N/A"), task.get("due_date", "N/A"), task.get("created_at", "N/A"), task.get("status", "N/A")])
	print(table)

if __name__ == '__main__':

	connectMongo()
	print("--- Görev Yönetim Sistemi ---")
	str = ("1. Görev Ekle\n"
		   "2. Görevleri Listele\n"
		   "3. Görev Güncelle\n"
		   "4. Görev sil\n"
		   "5. Görevleri Tarihe Göre Sırala\n"
		   "6. Çıkış")

	param = -1
	while param != 6:
		print(str)
		param = int(input("Seçiminizi yapın: "))
		match param:
			case 1:
				title = input("Görev Başlığı: ")
				desc = input("Açıklama: ")
				due_date = input("Son Tarih (YYYY-MM-DD): ")
				add_task(title, desc, due_date)
			case 2:
				list_tasks()
			case 3:
				title = input("Durumunu Güncelemek İstediğin Görevin Başlığı: ")
				# desc = input("Açıklama: ")
				# due_date = input("Son Tarih (YYYY-MM-DD): ")
				status = input("Durum: ")
				update_task(title, status)
			case 4:
				title = input("Silmek İstediğin Görevin Başlığı: ")
				delete_task(title)
			case 5:
				sortedByDate()
			case 6:
				exit(1)
			case _:
				exit(1)

