
#Un bot que publica por nosotros en Twitter

##time para poder permitir esperar un tiempo entre cada publicación (Y no estar publicando como wns, sino esperando unos momentos...)
##sys para poder importar el archivo de texto que contendrá los tweets.
import tweepy, time, sys

#nombre del archivo pasado como argumento en la consola
#argfile = str(sys.argv[1])


#claves y los tokens

CONSUMER_KEY = '6iRsWenJOXgyE0q6Vtxn80Z2X'
CONSUMER_SECRET = 'Meh7OOhko50o4V2xhqmQLyH3O7fMrn6oFPxefOqSMmPm7TNw1r'
ACCESS_KEY = '2593998445-T4brN6M4rJlmQaG0m2iwzj9El2M1xMe8FgEYqx4'
ACCESS_SECRET = 'LfCJXUYqbxop9qnt0RzniixKhDaSEtF8XaPKE34I4siYP'


#enlace a twitter para autentificar
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

#envia a Twitter los tokens de nuestra App
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#usar la API de Twitter, para poder publicar tweets
api = tweepy.API(auth)

#leer el archivo que contiene nuestros tweets
#filename = open(argfile,'r')
filename = open('tweets.txt','r')
f = filename.readlines()
filename.close()


#tweetea por linea del txt

# for line in f:
#     print("[+] Tweeting something...")
#     api.update_status(status = line)
#     print("[+] Tweet: ", line)
#     time.sleep(20)


try:
	for line in f:
	    print("[+] Tweeting something...")
	    api.update_status(status = line)
	    print("[+] Tweet: ", line)
	    time.sleep(20)
except tweepy.TweepError as error:
    if error.api_code == 187:
        # Do something special
        print('duplicate message')
    else:
       raise error