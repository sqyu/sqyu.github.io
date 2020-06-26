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

country_sorted_by_en = sorted(country_flag.items(), key=lambda item: item[1][1])
country_sorted_by_en = [code for code, _ in country_sorted_by_en]
country_sorted_by_en_idx_dict = {code: index for index, code in enumerate(country_sorted_by_en)}


open("travel_list.jemdoc", "w").write(
"""# jemdoc: menu{MENU}{travel_list.html}, lang-en
= My travel history (page under development)

== Countries and regions visited
""" + 
"\n".join([
	"- " + flag + " [" + country + ".html " + english + " (" + native + ")]"
	for country, (flag, english, native) in country_flag.items()
	]) + "\n")


country_sub_template = """# jemdoc: menu{MENU}{COUNTRY_CODE.html}, lang-en
= Travel to {COUNTRY}

[travel_list.html Back to list]

{PREV_NEXT_COUNTRIES}

== Description
{DESCRIPTION}

== Photos
{PHOTOS}
"""

def prev_next_countries(prev_visit_idx, next_visit_idx, prev_alpha_idx, next_alpha_idx):
	if prev_visit_idx == -1:
		prev_visit = None
	else:
		prev_visit = "[" + list(country_flag.items())[prev_visit_idx][0] + ".html <-Previous by order of first visit<-]"
	if prev_alpha_idx == -1:
		prev_alpha = None
	else:
		prev_alpha = "[" + country_sorted_by_en[prev_alpha_idx] + ".html <-Previous by alphabetical order<-]"
	if next_visit_idx == len(country_flag):
		next_visit = None
	else:
		next_visit = "[" + list(country_flag.items())[next_visit_idx][0] + ".html ->Next by order of first visit->]"
	if next_alpha_idx == len(country_flag):
		next_alpha = None
	else:
		next_alpha = "[" + country_sorted_by_en[next_alpha_idx] + ".html ->Next by alphabetical order->]"
	if prev_alpha is None:
		output = next_alpha + "\n\n"
	elif next_alpha is None:
		output = prev_alpha + "\n\n"
	else:
		output = prev_alpha + "{{&emsp;&emsp;&emsp;}}" + next_alpha + "\n\n"
	if prev_visit is None:
		output += next_visit
	elif next_visit is None:
		output += prev_visit
	else:
		output += prev_visit + "{{&emsp;&emsp;&emsp;}}" + next_visit
	return output




for index, (country, (flag, english, native)) in enumerate(country_flag.items()):
	if country + ".txt" not in os.listdir("."):
		open(country + ".txt", "w").write("DESCRIPTION:\n\nPHOTOS:\n")
	desc, photos = "".join(open(country + ".txt").readlines()).split("\nPHOTOS:\n")
	desc = re.sub(r"^DESCRIPTION:\n", "", desc).strip()
	photos = photos.strip()
	jemdoc_write = country_sub_template.replace("COUNTRY_CODE", country)
	jemdoc_write = jemdoc_write.replace("{COUNTRY}", flag + " " + english + " (" + native + ")")
	jemdoc_write = jemdoc_write.replace("{PREV_NEXT_COUNTRIES}", 
		prev_next_countries(index-1, index+1, country_sorted_by_en_idx_dict[country]-1, country_sorted_by_en_idx_dict[country]+1))
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




