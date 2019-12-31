import time
import random

num_correct = 0

class FrQuestions():

	def __init__(self = 0):
		
		def correct():
			global num_correct
			num_correct += 1
			print("\033[1;32;40m[√]\033[0;37;40m")

		def incorrect():
			print("\033[0;37;41m[X]\033[0;37;40m")

		def qprint(qw):
			print("\033[1;34;40m"+qw+"\033[0;37;40m")

		def cprint(ch):
			print("\033[1;36;40m"+ch+"\033[0;37;40m")

		def qw1_5():
			qprint("\nParmi les propositions suivantes, laquelle est la plage d'hotes valide pour le sous-reseau sur lequel l'adresse IP 158.167.18.156/15 reside ?")
			cprint("""
\t1 - 158.166.0.1 - 158.167.255.253
\t2 - 158.165.255.253 - 158.167.255.254
\t3 - 158.166.0.1 - 158.167.255.254
\t4 - 158.166.0.2 - 158.168.0.2""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nSi l'adresse IP 123.48.189.194/21 est attribuee a un port Ethernet d'un routeur, quelle adresse d'hote pourrait communiquer avec lui?")
			cprint("""
\t1 - 101.219.223.235
\t2 - 75.153.38.143
\t3 - 5.200.165.154
\t4 - 13.28.168.153
\t5 - 172.1.223.196
\t6 - 43.241.96.42
\t7 - 123.48.189.109
\t8 - 253.99.227.186""")
			repons = input("Votre Réponse : ")
			if repons == '7':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nLaquelle des propositions suivantes est une adresse IP privee?")
			cprint("""
\t1 - 57.195.242.245
\t2 - 172.27.217.52
\t3 - 249.204.256.26
\t4 - 249.204.156.26
\t5 - 4.137.228.63
\t6 - 176.37.230.43
\t7 - 218.106.207.158
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse reseau d'un hote avec une adresse IP de 182.161.121.118/24?")
			cprint("""
\t1 - 180.0.0.0
\t2 - 182.161.121.64
\t3 - 182.161.120.0
\t4 - 182.161.121.116
\t5 - 0.0.0.0
\t6 - 182.161.96.0
\t7 - 182.160.0.0
\t8 - 182.161.121.0

""")
			repons = input("Votre Réponse : ")
			if repons == '8':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuel est le nombre maximal d'adresses IP pouvant etre attribuees aux hotes d'un sous-reseau local utilisant le masque de sous-reseau 255.255.128.0 ?")
			cprint("""
\t1 - 65536
\t2 - 65532
\t3 - 16380
\t4 - 32768
\t5 - 32770
\t6 - 65530
\t7 - 32766
\t8 - 16382
\t9 - 32764


""")
			repons = input("Votre Réponse : ")
			if repons == '7':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw6_10():
			qprint("\nVous souhaitez implementer un mecanisme qui automatise la configuration IP, y compris l'adresse IP, le masque de sous-reseau, la passerelle par defaut et les informations DNS. Quel protocole utiliserez-vous pour y parvenir?")
			cprint("""
\t1 - SNMP
\t2 - DHCP
\t3 - SMTP
\t4 - ARP
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nVous avez une interface sur un routeur avec l'adresse IP de 124.144.156.248/21. L'interface du routeur comprise, combien d'hotes peuvent avoir des adresses IP sur le reseau local connectees a l'interface du routeur?")
			cprint("""
\t1 - 1020
\t2 - 2050
\t3 - 2044
\t4 - 4090
\t5 - 2046
\t6 - 2048
\t7 - 4092
\t8 - 2042
\t9 - 4094
""")
			repons = input("Votre Réponse : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nParmi les propositions suivantes, laquelle est la plage d'hote valide pour le sous-reseau sur lequel l'adresse IP 1.93.149.6/17 reside?")
			cprint("""
\t1 - 1.93.127.255- 1.93.255.250
\t2 - 1.93.128.1- 1.94.0.1
\t3 - 1.93.128.1- 1.93.255.251
\t4 - 1.93.128.1- 1.93.255.254
\t5 - 1.93.128.1- 1.94.0.3
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse reseau d'un hote avec une adresse IP de 107.212.146.212/25?")
			cprint("""
\t1 - 107.212.146.208
\t2 - 107.128.0.0
\t3 - 0.0.0.0
\t4 - 64.0.0.0
\t5 - 107.212.128.0
\t6 - 107.212.146.128
\t7 - 107.212.0.0
\t8 - 107.208.0.0
\t9 - 107.212.146.192

""")
			repons = input("Votre Réponse : ")
			if repons == '6':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nParmi les propositions suivantes, laquelle est la plage d'hotes valide pour le sous-reseau sur lequel l'adresse IP 233.249.146.36/21 reside?")
			cprint("""
\t1 - 233.249.143.255-233.249.151.250
\t2 - 233.249.144.4-233.249.152.0
\t3 - 233.249.144.1-233.249.151.254
\t4 - 233.249.144.6-233.249.152.1
\t5 - 233.249.144.0-233.249.151.249

""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw11_15():
			qprint("\nLaquelle des propositions suivantes n'est pas vraie ?")
			cprint("""
\t1 - TCP est un protocole oriente datagramme
\t2 - TCP ne prend pas en charge la diffusion
\t3 - TCP fournit des mecanismes de verification d'erreur etendus. C'est parce qu'il fournit le controle de flux et l'acquittement des donnees
\t4 - Le sequencage des donnees est une caracteristique de TCP (cela signifie que les paquets arrivent dans l'ordre dans le destinataire)
\t5 - TCP est fiable car il garantit la livraison des donnees au routeur de la destination
\t6 - TCp est comparativement plus lent que UDP
""")
			repons = input("Votre Réponse : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse reseaux d'un hote avec une adresse IP de 166.175.144.121/23?")
			cprint("""
\t1 - 166.128.0.0
\t2 - 166.175.144.0
\t3 - 166.175.144.96
\t4 - 128.0.0.0
\t5 - 166.174.0.0
\t6 - 166.0.0.0
\t7 - 166.0.0.0
\t8 - 166.175.144.120
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuel est le nombre maximal d'adresses IP pouvant etre attribuees aux hotes d'un sous-reseau local utilisant le masque de sous-reseau 255.255.255.128 ?")
			cprint("""
\t1 - 128
\t2 - 60
\t3 - 126
\t4 - 62
\t5 - 252
\t6 - 258
\t7 - 124
\t8 - 58
\t9 - 64
""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuel est le nombre maximal d'adresses IP pouvant etre attribuees aux hotes d'un sous-reseau local utilisant le masque de sous-reseau 255.224.0.0 ?")
			cprint("""
\t1 - 4194306
\t2 - 4194302
\t3 - 1048578
\t4 - 4194300
\t5 - 2097148
\t6 - 4194298
\t7 - 1048574
\t8 - 2097150
\t9 - 1048576
""")
			repons = input("Votre Réponse : ")
			if repons == '8':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nLaquelle des propositions suivantes est une adresse IP privee ?")
			cprint("""
\t1 - 10.182.204.132
\t2 - 116.124.85.24
\t3 - 52.178.248.246
\t4 - 186.183.40.79
""")
			repons = input("Votre Réponse : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw16_20():
			qprint("\nQuel protocole DHCP utilise-t-il au niveau de la couche transport ?")
			cprint("""
\t1 - ICMP
\t2 - TCP
\t3 - FTP
\t4 - UDP
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nVous avez une interface sur un routeur avec l'adresse IP  de 240.19.3.205/12. L'interface du routeur comprise, combien d'hotes peuvent avoir des adresses IP sur le reseau local conectees a l'interface du routeur ?")
			cprint("""
\t1 - 1048576
\t2 - 2097154
\t3 - 1048574
\t4 - 524284
\t5 - 1048578
\t6 - 2097148
\t7 - 1048572
""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse broadcast d'un hote avec une adresse IP de 51.254.122.100/24 ?")
			cprint("""
\t1 - 51.254.122.0
\t2 - 51.254.122.1
\t3 - 51.254.122.254
\t4 - 51.254.122.255
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est la notation CIDR du masque de sous reseau 255.255.128.0 ?")
			cprint("""
\t1 - /8
\t2 - /16
\t3 - /9
\t4 - /17
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est la notation CIDR du masque de sous reseau 255.255.192.0 ?")
			cprint("""
\t1 - /5
\t2 - /31
\t3 - /18
\t4 - /14
""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw21_25():
			qprint("\nQuelles sont les differentes couches du model OSI ?")
			cprint("""
\t1 - Application -> Presentation -> Session -> Transport -> Reseau -> Liaison -> Physique
\t2 - Application -> Mediation -> Session -> Transport -> Reseau -> Liaison -> Physique
\t3 - Presentation -> Session -> Transport -> Reseau -> Liaison -> Application -> Reel
\t4 - Relation -> Transport -> Session -> Liaison -> Mediation -> Presentation ->Application
""")
			repons = input("Votre Réponse : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse reseau d'un hote avec une adresse ip de 116.45.224.50/8 ?")
			cprint("""
\t1 - 116.0.1.0
\t2 - 116.0.0.0
\t3 - 116.255.255.0
\t4 - 116.255.255.255
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est l'adresse reseau d'un hote avec une adresse IP de 45.195.37.187/16?")
			cprint("""
\t1 - 45.194.37.187
\t2 - 45.0.0.0
\t3 - 45.194.0.0
\t4 - 45.195.0.0
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\n.......... traduit les noms de domaine Internet et d'hote en adresse IP")
			cprint("""
\t1 - Network time protocol (NTP)
\t2 - Default routing protocol
\t3 - Domain name system (DNS)
\t4 - OSI model system
""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle classe d'adresse IP a plus d'adresses d'hote disponibles par defaut ?")
			cprint("""
\t1 - C
\t2 - D
\t3 - E
\t4 - B
\t5 - A
""")
			repons = input("Votre Réponse : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw26_33():
			qprint("\nLaquelle des propositions suivantes n'est pas vraie ?")
			cprint("""
\t1 - UDP est plus rapide, plus simple et plus efficace que TCP
\t2 - UDP ne dispose que du mecanisme de controle d'erreur de base
\t3 - UDP est un protocole oriente datagramme
\t4 - UDP ne prend pas en charge la diffusion
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nLaquelle des propositions suivantes n'est pas vraie ?")
			cprint("""
\t1 - TCP est un protocole oriente connexion
\t2 - TCP ne prend pas en charge la diffusion
\t3 - TCP fournit des mecanismes de verification d'erreur etendus. C'est parce qu'il fournit le controle de flux et l'acquittement des donees
\t4 - Le sequencage des donnees est une caracteristique de TCP (cela signifie que les paquets arrivent dans l'ordre dans le destinataire)
\t5 - La livraison des donnees a la destination ne peut pas etre garantie en TCP
\t6 - TCP est fiable car il garantit la livraison des donnees au routeur de la destination
""")
			repons = input("Votre Réponse : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuel est le masque de sous reseau de /24 ?")
			cprint("""
\t1 - 255.255.255.255
\t2 - 255.255.255.0
\t3 - 255.0.0.0
\t4 - 255.255.128.0
\t5 - 255.192.0.0
\t6 - 255.224.0.0
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est la taille d'une adresse IPV4 ?")
			cprint("""
\t1 - 128 bits
\t2 - 32 bits
\t3 - 64 miles
\t4 - 16 bits
\t5 - 8 bits
\t6 - 64 bytes
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle est la taille d'une adresse IPV6 ?")
			cprint("""
\t1 - 128 bits
\t2 - 32 bits
\t3 - 64 miles
\t4 - 16 bits
\t5 - 8 bits
\t6 - 64 bytes
""")
			repons = input("Votre Réponse : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuelle type d'adresse est pris en charge par DHCP ?")
			cprint("""
\t1 - IPV4
\t2 - IPV6
\t3 - IPV4 et IPV6
\t4 - Aucun d'entre eux
""")
			repons = input("Votre Réponse : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nQuel protocole utilise Ping?")
			cprint("""
\t1 - ARP
\t2 - BootP
\t3 - TCP
\t4 - ICMP
""")
			repons = input("Votre Réponse : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nLaquelle des propositions suivantes n'est pas vraie ?")
			cprint("""
\t1 - UDP est plus rapide, plus simple et plus efficace que TCP
\t2 - UDP fournit des mecanismes de verification d'erreur etendus. C'est parce qu'il fournit le controle de flux et l'acquittement des donees
\t3 - UDP est un protocole oriente datagramme
\t4 - UDP prend en charge la diffusion
""")
			repons = input("Votre Réponse : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)


		numlst = list(range(1,6))
		random.shuffle(numlst)
		i = 0
		start_time = time.time()
		while i < len(numlst):
			if (numlst[i] == 1):
				qw1_5()
			elif (numlst[i] == 2):
				qw6_10()
			elif (numlst[i] == 3):
				qw11_15()
			elif (numlst[i] == 4):
				qw16_20()
			elif (numlst[i] == 5):
				qw21_25()
			i += 1
		end_time = time.time()

		def cowsay(string):
			line_nb = 58
			print("")
			print("-" * line_nb)
			print("{}".format(string))
			print("-" * line_nb)
			print('''\033[1;32;40m
     \\  ^__^
      \\ (♥♥)\\_______
        (__)\\       )\\
            ||----w |        
            ||     ||
				\033[0;37;40m''')

		global num_correct
		total_time = (end_time - start_time)/60
		cowsay("Vous Avez \033[1;32;40m"+str(num_correct)+"/33\033[0;37;40m Réponses Correctes\n" + "----------------------------------------------------------\n" + "Vous Avez Pris \033[1;32;40m{}\033[0;37;40m Minutes Pour Terminer La Préparation".format(round(total_time, 2)))