import tweepy, time, sys

CONSUMER_KEY = '6iRsWenJOXgyE0q6Vtxn80Z2X'
CONSUMER_SECRET = 'Meh7OOhko50o4V2xhqmQLyH3O7fMrn6oFPxefOqSMmPm7TNw1r'
ACCESS_KEY = '2593998445-T4brN6M4rJlmQaG0m2iwzj9El2M1xMe8FgEYqx4'
ACCESS_SECRET = 'LfCJXUYqbxop9qnt0RzniixKhDaSEtF8XaPKE34I4siYP'

#directorio de la imagen
f_imagen="andres.jpg"

#enlace a twitter para autentificar
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#envia a Twitter los tokens de nuestra App
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

auth.secure = True
#usar la API de Twitter, para poder publicar tweets
api = tweepy.API(auth)

tweet = "Buen momo del andres"

#tweetea
api.update_with_media(f_imagen,status=tweet)