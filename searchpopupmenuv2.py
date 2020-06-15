import dialogv2
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App

class SearchPopupMenu(dialogv2.MDInputDialog):
	title = 'Search by Address'
	text_button_ok = 'Search'

	def __init__(self):
		super().__init__()
		self.size_hint = [.9, .3]
		self.events_callback = self.callback

	def callback(self, *args):
		address = self.text_field.text
		self.geocode_get_lat_lon(address)

	def geocode_get_lat_lon(self, address):
		#app_id = "wuHcs4aTiLprbdhSn793"
		#app_code = "9v2BkviRwi9Ot26kp2IysQ"
		api_key = "rUd90Pq0itCtqKZfNVbRuWcOpOW_vIDGvN2WnOLlzT8"
		address = parse.quote(address)
		#url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
		url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&gen=9&apiKey=%s"%(address, api_key)
		UrlRequest(url, on_success = self.success, on_failure = self.failure, on_error = self.error)

	def success(self, urlrequest, result):
		print("Success")
		latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
		longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
		app = App.get_running_app()
		mapview = app.root.ids.mapview
		mapview.center_on(latitude,longitude)
		#print(latitude, longitude)
		#print(result)

	def failure(self, urlrequest, result):
		print("Failure")
		print(result)

	def error(self, urlrequest, result):
		print("Error")
		print(result)

