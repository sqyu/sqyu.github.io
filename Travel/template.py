from collections import OrderedDict
import os 
import re
#from subprocess import Popen
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

country_flag = OrderedDict(
	{"cn": ("🇨🇳", "China", "中国"),
	"hk": ("🇭🇰", "Hong Kong", "香港"), 
	"mo": ("🇲🇴", "Macau", "澳門"),
	"jp": ("🇯🇵", "Japan", "日本"), 
	"au": ("🇦🇺", "Australia", "Australia"),
	"tw": ("🇹🇼", "Taiwan", "臺灣 | 台灣"),
	"us": ("🇺🇸", "United States", "United States"), 
	"qa": ("🇶🇦", "Qatar", "قطر"), 
	"pl": ("🇵🇱", "Poland", "Polska"),
	"de": ("🇩🇪", "Germany", "Deutschland"),
	"cz": ("🇨🇿", "Czech Republic", "Česko"),
	"at": ("🇦🇹", "Austria", "Österreich"), 
	"sk": ("🇸🇰", "Slovakia", "Slovensko"), 
	"hu": ("🇭🇺", "Hungary", "Magyarország"),
	"ca": ("🇨🇦", "Canada", "Canada"),
	"gb": ("🇬🇧", "United Kingdom", "United Kingdom"), 
	"ie": ("🇮🇪", "Ireland", "Éire"),
	"kr": ("🇰🇷", "South Korea", "대한민국"),
	"fr": ("🇫🇷", "France", "France"), 
	"mc": ("🇲🇨", "Monaco", "Monaco"),
	"it": ("🇮🇹", "Italy", "Italia"),
	"ch": ("🇨🇭", "Switzerland", "Schweiz | Suisse | Svizzera | Svizra"),
	"lu": ("🇱🇺", "Luxembourg", "Lëtzebuerg | Luxembourg | Luxemburg"),
	"be": ("🇧🇪", "Belgium", "België | Belgique | Belgien"), 
	"nl": ("🇳🇱", "Netherlands", "Nederland"),
	"es": ("🇪🇸", "Spain", "España"),
	"mx": ("🇲🇽", "Mexico", "México"),
	"dk": ("🇩🇰", "Denmark", "Danmark"),
	"se": ("🇸🇪", "Sweden", "Sverige"), 
	"fl": ("🇫🇮", "Finland", "Suomi | Finland"),
	"ee": ("🇪🇪", "Estonia", "Eesti"),
	"lv": ("🇱🇻", "Latvia", "Latvija"),
	"lt": ("🇱🇹", "Lithuania", "Lietuva"),
	"by": ("🇧🇾", "Belarus", "Беларусь"),
	"ua": ("🇺🇦", "Ukraine", "Україна"), 
	"pt": ("🇵🇹", "Portugal", "Portugal"),
	"ad": ("🇦🇩", "Andorra", "Andorra"),
	"fo": ("🇫🇴", "Faroe Islands", "Føroyar | Færøerne"),
	"is": ("🇮🇸", "Iceland", "Ísland"), 
	"no": ("🇳🇴", "Norway", "Norge | Noreg | Norga | Vuodna | Nöörje"), 
	"sg": ("🇸🇬", "Singapore", "Singapore | 新加坡 | Singapura | சிங்கப்பூர்"),
	"id": ("🇮🇩", "Indonesia", "Indonesia"), 
	"my": ("🇲🇾", "Malaysia", "Malaysia"),
	"rs": ("🇷🇸", "Serbia", "Србија | Srbija"), 
	"ba": ("🇧🇦", "Bosnia and Herzegovina", "Bosna i Hercegovina | Босна и Херцеговина"), 
	"me": ("🇲🇪", "Montenegro", "Црна Гора | Crna Gora"),
	"al": ("🇦🇱", "Albania", "Shqipëria")
	})


open("travel_list.jemdoc", "w").write(
"""# jemdoc: menu{MENU}{travel_list.html}, lang-en
= My travel history (page under development)

== Countries and regions visited
""" + 
"\n".join([
	"- " + items[0] + " [" + country + ".html " + items[1] + " (" + items[2] + ")]"
	for country, items in country_flag.items()
	]) + "\n")


country_sub_template = """# jemdoc: menu{MENU}{COUNTRY_CODE.html}, lang-en
= Travel to {COUNTRY}
[travel_list.html Back to list]

== Description
{DESCRIPTION}

== Photos
{PHOTOS}
"""


for country, items in country_flag.items():
	if country + ".txt" not in os.listdir("."):
		open(country + ".txt", "w").write("DESCRIPTION:\n\nPHOTOS:\n")
	desc, photos = "".join(open(country + ".txt").readlines()).split("\nPHOTOS:\n")
	desc = re.sub(r"^DESCRIPTION:\n", "", desc).strip()
	photos = photos.strip()
	jemdoc_write = country_sub_template.replace("COUNTRY_CODE", country)
	jemdoc_write = jemdoc_write.replace("{COUNTRY}", items[0] + " " + items[1] + " (" + items[2] + ")")
	if desc:
		jemdoc_write = jemdoc_write.replace("{DESCRIPTION}", desc)
	else:
		jemdoc_write = jemdoc_write.replace("== Description\n{DESCRIPTION}\n\n", "")
	if photos:
		photo_jemdoc = []
		for line in photos.split("\n"):
			if len(line.split(" ", 3)) < 4:
				raise Exception("In " + country + ".txt: Each line under PHOTOS must have the form 'photo name (under Photos/) SPACE width in pixels SPACE height SPACE description'.")
			name, width, height, photo_desc = line.split(" ", 3)
			photo_jemdoc.append("~~~\n{}{img_left}{Photos/%s}{%s}{%s}{%s}{}\n%s\n~~~" % (name, photo_desc, width, height, photo_desc))
		jemdoc_write = jemdoc_write.replace("{PHOTOS}", "\n\n".join(photo_jemdoc))
	else:
		jemdoc_write = jemdoc_write.replace("== Photos\n{PHOTOS}", "")
	open(country + ".jemdoc", "w").write(jemdoc_write)




