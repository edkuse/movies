
class Movie(object):
	"""A movie object.

	Creates and stores movie information including title, storyline, 
	URL of the poster image, and URL to trailer.
	"""
	def __init__(self, title, storyline, image_url, trailer_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = image_url
		self.trailer_youtube_url = trailer_url
