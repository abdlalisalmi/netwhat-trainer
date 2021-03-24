import time
import random

num_correct = 0

class EnQuestions():

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
			qprint("\nWhich of the following proposals is the valid host range for the subnet on which the IP address 158.167.18.156/15 resides?")
			cprint("""
\t1 - 158.166.0.1 - 158.167.255.253
\t2 - 158.165.255.253 - 158.167.255.254
\t3 - 158.166.0.1 - 158.167.255.254
\t4 - 158.166.0.2 - 158.168.0.2""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nIf the IP address 123.48.189.194/21 is assigned to an Ethernet port of a router, what host address could communicate with it?")
			cprint("""
\t1 - 101.219.223.235
\t2 - 75.153.38.143
\t3 - 5.200.165.154
\t4 - 13.28.168.153
\t5 - 172.1.223.196
\t6 - 43.241.96.42
\t7 - 123.48.189.109
\t8 - 253.99.227.186""")
			repons = input("Your Answer : ")
			if repons == '7':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following proposals is a private IP address?")
			cprint("""
\t1 - 57.195.242.245
\t2 - 172.27.217.52
\t3 - 249.204.256.26
\t4 - 249.204.156.26
\t5 - 4.137.228.63
\t6 - 176.37.230.43
\t7 - 218.106.207.158
""")
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the network address of a host with an IP address of 182.161.121.118/24?")
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
			repons = input("Your Answer : ")
			if repons == '8':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the maximum number of IP addresses that can be assigned to hosts on a local subnet using the 255.255.128.0 subnet mask?")
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
			repons = input("Your Answer : ")
			if repons == '7':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw6_10():
			qprint("\nYou want to implement a mechanism that automates IP configuration, including IP address, subnet mask, default gateway and DNS information. What protocol will you use to achieve this?")
			cprint("""
\t1 - SNMP
\t2 - DHCP
\t3 - SMTP
\t4 - ARP
""")
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nYou have an interface on a router with the IP address of 124.144.156.248/21. Including the router interface, how many hosts can have IP addresses on the local network connected to the router interface?")
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
			repons = input("Your Answer : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following proposals is the valid host range for the subnet on which the IP address 1.93.149.6/17 resides?")
			cprint("""
\t1 - 1.93.127.255- 1.93.255.250
\t2 - 1.93.128.1- 1.94.0.1
\t3 - 1.93.128.1- 1.93.255.251
\t4 - 1.93.128.1- 1.93.255.254
\t5 - 1.93.128.1- 1.94.0.3
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the network address of a host with an IP address of 107.212.146.212.212/25?")
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
			repons = input("Your Answer : ")
			if repons == '6':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following proposals is the valid host range for the subnet on which the IP address 233.249.146.36/21 resides?")
			cprint("""
\t1 - 233.249.143.255-233.249.151.250
\t2 - 233.249.144.4-233.249.152.0
\t3 - 233.249.144.1-233.249.151.254
\t4 - 233.249.144.6-233.249.152.1
\t5 - 233.249.144.0-233.249.151.249

""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw11_15():
			qprint("\nWhich of the following propositions is not true?")
			cprint("""
\t1 - TCP is a datagram oriented protocol
\t2 - TCP does not support broadcasting
\t3 - TCP provides extended error checking mechanisms. This is because it provides flow control and data acknowledgement
\t4 - Data sequencing is a TCP feature (this means that packets arrive in order in the recipient)
\t5 - TCP is reliable because it guarantees the delivery of data to the router of the destination
\t6 - TCP is comparatively slower than UDP
""")
			repons = input("Your Answer : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the network address of a host with an IP address of 166.175.144.121/23?")
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
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the maximum number of IP addresses that can be assigned to hosts on a local subnet using the 255.255.255.128 subnet mask?")
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
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the maximum number of IP addresses that can be assigned to hosts on a local subnet using the 255.224.0.0 subnet mask?")
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
			repons = input("Your Answer : ")
			if repons == '8':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following proposals is a private IP address?")
			cprint("""
\t1 - 10.182.204.132
\t2 - 116.124.85.24
\t3 - 52.178.248.246
\t4 - 186.183.40.79
""")
			repons = input("Your Answer : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw16_20():
			qprint("\nWhat DHCP protocol does it use at the transport layer level?")
			cprint("""
\t1 - ICMP
\t2 - TCP
\t3 - FTP
\t4 - UDP
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nYou have an interface on a router with the IP address of 240.19.3.205/12. Including the router interface, how many hosts can have IP addresses on the local network connected to the router interface?")
			cprint("""
\t1 - 1048576
\t2 - 2097154
\t3 - 1048574
\t4 - 524284
\t5 - 1048578
\t6 - 2097148
\t7 - 1048572
""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the broadcast address of a host with an IP address of 51,254,122,100/24?")
			cprint("""
\t1 - 51.254.122.0
\t2 - 51.254.122.1
\t3 - 51.254.122.254
\t4 - 51.254.122.255
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the CIDR notation of the 255.255.128.0 subnet mask?")
			cprint("""
\t1 - /8
\t2 - /16
\t3 - /9
\t4 - /17
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the CIDR notation of the 255.255.192.0 subnet mask?")
			cprint("""
\t1 - /5
\t2 - /31
\t3 - /18
\t4 - /14
""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw21_25():
			qprint("\nWhat are the different layers of the OSI model?")
			cprint("""
\t1 - Application -> Presentation -> Session -> Transport -> Network -> Data Link -> Physical
\t2 - Application -> Mediation -> Session -> Transport -> Network -> Data Link -> Physical
\t3 - Presentation -> Session -> Transport -> Network -> Data Link -> Application -> Real
\t4 - Relation -> Transport -> Session -> Data Link -> Mediation -> Presentation -> Application
""")
			repons = input("Your Answer : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the network address of a host with an IP address of 116.45.224.50/8?")
			cprint("""
\t1 - 116.0.1.0
\t2 - 116.0.0.0
\t3 - 116.255.255.0
\t4 - 116.255.255.255
""")
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the network address of a host with an IP address of 45.195.37.187/16?")
			cprint("""
\t1 - 45.194.37.187
\t2 - 45.0.0.0
\t3 - 45.194.0.0
\t4 - 45.195.0.0
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\n.......... translates Internet domain names and host names into IP addresses")
			cprint("""
\t1 - Network time protocol (NTP)
\t2 - Default routing protocol
\t3 - Domain name system (DNS)
\t4 - OSI model system
""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich IP address class has more host addresses available by default?")
			cprint("""
\t1 - C
\t2 - D
\t3 - E
\t4 - B
\t5 - A
""")
			repons = input("Your Answer : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)

#**************************************************************************
#**************************************************************************

		def qw26_33():
			qprint("\nWhich of the following propositions is not true?")
			cprint("""
\t1 - UDP is faster, simpler and more efficient than TCP
\t2 - UDP only has the basic error control mechanism
\t3 - UDP is a datagram oriented protocol
\t4 - UDP does not support broadcasting
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following propositions is not true?")
			cprint("""
\t1 - TCP is a connection-oriented protocol
\t2 - TCP does not support broadcasting
\t3 - TCP provides extended error checking mechanisms. This is because it provides flow control and data acknowledgement
\t4 - Data sequencing is a TCP feature (this means that packets arrive in order in the recipient)
\t5 - The delivery of data to the destination cannot be guaranteed in TCP
\t6 - TCP is reliable because it guarantees the delivery of data to the router of the destination
""")
			repons = input("Your Answer : ")
			if repons == '5':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\n28 - What is the subnet mask of /24?")
			cprint("""
\t1 - 255.255.255.255
\t2 - 255.255.255.0
\t3 - 255.0.0.0
\t4 - 255.255.128.0
\t5 - 255.192.0.0
\t6 - 255.224.0.0
""")
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the size of an IPV4 address?")
			cprint("""
\t1 - 128 bits
\t2 - 32 bits
\t3 - 64 miles
\t4 - 16 bits
\t5 - 8 bits
\t6 - 64 bytes
""")
			repons = input("Your Answer : ")
			if repons == '2':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat is the size of an IPV6 address?")
			cprint("""
\t1 - 128 bits
\t2 - 32 bits
\t3 - 64 miles
\t4 - 16 bits
\t5 - 8 bits
\t6 - 64 bytes
""")
			repons = input("Your Answer : ")
			if repons == '1':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhat type of address is supported by DHCP?")
			cprint("""
\t1 - IPV4
\t2 - IPV6
\t3 - IPV4 and IPV6
\t4 - None of them
""")
			repons = input("Your Answer : ")
			if repons == '3':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich protocol does Ping use?")
			cprint("""
\t1 - ARP
\t2 - BootP
\t3 - TCP
\t4 - ICMP
""")
			repons = input("Your Answer : ")
			if repons == '4':
				correct()
			else:
				incorrect()
			time.sleep(0.5)
			qprint("\nWhich of the following propositions is not true?")
			cprint("""
\t1 - UDP is faster, simpler and more efficient than TCP
\t2 - UDP provides extended error checking mechanisms. This is because it provides flow control and data acknowledgement
\t3 - UDP is a datagram oriented protocol
\t4 - UDP supports broadcasting
""")
			repons = input("Your Answer : ")
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
			line_nb = 48
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
		cowsay("You Have \033[1;32;40m"+str(num_correct)+"/33\033[0;37;40m Correct Answers\n" + "------------------------------------------------\n" + "You Took \033[1;32;40m{}\033[0;37;40m Minutes To Complete The Training".format(round(total_time, 2)))
