from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from storemarkerv2 import StoreMarker
from convertdatav2 import updateDB

class UserMapView(MapView):
	getting_stores_timer = None
	store_names = []

	def start_getting_stores_in_fov(self):
		#gets stores in fov after 1 sec if no scrolling/zoom
		try:
			self.getting_stores_timer.cancel()
		except:
			pass

		self.getting_stores_timer = Clock.schedule_once(self.get_stores_in_fov, 1)

	def get_stores_in_fov(self, *args):
		min_lat, min_lon, max_lat, max_lon = self.get_bbox()
		print("min_lat: " + str(min_lat))
		print("max_lat: " + str(max_lat))
		print("min_lon: " + str(min_lon))
		print("max_lon: " + str(max_lon))
		app = App.get_running_app()
		sql_statement = "SELECT * FROM my_table WHERE (CAST(x AS INTEGER) > %s) AND (CAST(x AS INTEGER)  < %s) AND (CAST(y AS INTEGER) > %s) AND (CAST(y AS INTEGER) < %s)"%(min_lon, max_lon, min_lat, max_lat)
		app.cursor.execute(sql_statement)
		stores = app.cursor.fetchall()
		print(stores)
		#checks if the database is updated
		updateDB()
		for store in stores:
			name = store[0]
			if name in self.store_names:
				self.update_store(store)
			else:
				self.add_store(store)

	def add_store(self,store):
		#create marker
		lat, lon = store[3], store[2]
		marker = StoreMarker(lat = lat, lon = lon)
		marker.store_data = store
		#add marker to map
		self.add_widget(marker)

	def update_store(self,store):
		lat, lon = store[3], store[2]
		marker = StoreMarker(lat = lat, lon = lon)
		marker.store_data = store


		#keep track of marker name
		name = store[0]
		self.store_names.append(name)