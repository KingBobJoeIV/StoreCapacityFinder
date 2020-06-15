from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenuv2 import LocationPopupMenu
from convertdatav2 import updateDB

class StoreMarker(MapMarkerPopup):
	store_data = []

	def on_release(self):
		#open location on popup menu
		updateDB()
		#print("here")
		menu = LocationPopupMenu(self.store_data)
		menu.size_hint = [.8,.9]
		menu.open()