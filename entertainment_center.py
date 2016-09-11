import media
import fresh_tomatoes


#
# List of favorite movies using the movie title, storyline, poster image 
# url, and youtube trailer url.  Information was copied from TMDB: 
# https://www.themoviedb.org/
#
my_movies = [
	media.Movie(
		"The Usual Suspects",
		"""
		A sole survivor tells of the twisty events leading up to a horrific 
		gun battle on a boat, which begin when five criminals meet at a 
		seemingly random police lineup.
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/jgJoRWltoS17nD5MAQ1yK2Ztefw.jpg",
		"https://youtu.be/oiXdPolca5w"
	),
	media.Movie(
		"Shawshank Redemption",
		"""
		Framed in the 1940s for the double murder of his wife and her lover, 
		upstanding banker Andy Dufresne begins a new life at the Shawshank 
		prison, where he puts his accounting skills to work for an amoral 
		warden. During his long stretch in prison, Dufresne comes to be admired 
		by the other inmates -- including an older prisoner named Red -- for 
		his integrity and unquenchable sense of hope.
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
		"https://youtu.be/WawU4ouldxU"
	),
	media.Movie(
		"Ace Ventura: Pet Detective",
		"""
		He's Ace Ventura: Pet Detective. Jim Carrey is on the case to find the 
		Miami Dolphins' missing mascot and quarterback Dan Marino. He goes 
		eyeball to eyeball with a man-eating shark, stakes out the Miami 
		Dolphins and woos and wows the ladies. Whether he's undercover, under 
		fire or underwater, he always gets his man... or beast!
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/nZirljb8XYbKTWsRQTplDGhx39Q.jpg",
		"https://youtu.be/cXcH0f2B2vA"
	),
	media.Movie(
		"Swingers",
		"""
		This is a story about Mike, a guy who left his girl in New York when he 
		came to LA to be a star. It's been six months since his girlfriend left 
		him and he's not doing so good. So, his pal and some other friends try 
		and get him back in the social scene and forget about his 6 year 
		relationship.
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/h1nLEgXCNK6sQgup22SYgNTrwJm.jpg",
		"https://youtu.be/sfHZvxg87h8"
	),
	media.Movie(
		"Inception",
		"""
		Cobb, a skilled thief who commits corporate espionage by infiltrating 
		the subconscious of his targets is offered a chance to regain his old 
		life as payment for a task considered to be impossible: "inception", 
		the implantation of another person's idea into a target's subconscious.
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg",
		"https://youtu.be/xitHF0IPJSQ"
	),
	media.Movie(
		"Memento",
		"""
		Suffering short-term memory loss after a head injury, Leonard Shelby 
		embarks on a grim quest to find the lowlife who murdered his wife in 
		this gritty, complex thriller that packs more knots than a hangman's 
		noose. To carry out his plan, Shelby snaps Polaroids of people and 
		places, jotting down contextual notes on the backs of photos to aid 
		in his search and jog his memory. He even tattoos his own body in a 
		desperate bid to remember.
		""",
		"https://image.tmdb.org/t/p/w600_and_h900_bestv2/fQMSaP88cf1nz4qwuNEEFtazuDM.jpg",
		"https://youtu.be/Rq9eM4ZXRgs"
	)
]

#
# Load and display movie website using fresh_tomatoes module
#
fresh_tomatoes.open_movies_page(my_movies)

