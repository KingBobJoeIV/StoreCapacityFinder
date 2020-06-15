from kivymd.app import MDApp
from usermapviewv2 import UserMapView
import sqlite3
from searchpopupmenuv2 import SearchPopupMenu

class MainApp(MDApp):
	connection = None
	cursor = None
	search_menu = None

	def on_start(self):
		#init gps

		#connect to db
		self.connection = sqlite3.connect("store.db")
		self.cursor = self.connection.cursor()

		#start search menu
		self.search_menu = SearchPopupMenu()

MainApp().run()
