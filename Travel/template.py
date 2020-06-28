from collections import OrderedDict
import os 
import re
#from subprocess import Popen
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

country_list = OrderedDict(
	{"cn": ("🇨🇳", "中国大陆", {"en": "China", "hk": "中國大陸", "ha": "中國大陸", "tw": "中國大陸", "cn": "中国大陆", "ja": "中国", "ko": "중국", "fr": "Chine"}),
	"hk": ("🇭🇰", "香港", {"en": "Hong Kong", "hk": "香港", "ha": "香港", "tw": "香港", "cn": "香港", "ja": "香港", "ko": "홍콩", "fr": "Hong Kong"}),
	"mo": ("🇲🇴", "澳門", {"en": "Macau", "hk": "澳門", "ha": "澳門", "tw": "澳門", "cn": "澳门", "ja": "マカオ", "ko": "마카오", "fr": "Macao"}),
	"jp": ("🇯🇵", "日本", {"en": "Japan", "hk": "日本", "ha": "日本", "tw": "日本", "cn": "日本", "ja": "日本", "ko": "일본", "fr": "Japon"}),
	"au": ("🇦🇺", "Australia", {"en": "Australia", "hk": "澳洲", "ha": "澳洲", "tw": "澳洲", "cn": "澳大利亚", "ja": "オーストラリア", "ko": "오스트레일리아", "fr": "Australie"}),
	"tw": ("🇹🇼", "臺灣 | 台灣", {"en": "Taiwan", "hk": "臺灣", "ha": "臺灣 | 台灣", "tw": "臺灣 | 台灣", "cn": "台湾", "ja": "台湾", "ko": "대만", "fr": "Taïwan"}),
	"us": ("🇺🇸", "United States", {"en": "United States", "hk": "美國", "ha": "美國", "tw": "美國", "cn": "美国", "ja": "アメリカ合衆国", "ko": "미국", "fr": "États-Unis"}),
	"qa": ("🇶🇦", "قطر", {"en": "Qatar", "hk": "卡塔爾", "ha": "卡塔爾", "tw": "卡達", "cn": "卡塔尔", "ja": "カタール", "ko": "카타르", "fr": "Qatar"}),
	"pl": ("🇵🇱", "Polska", {"en": "Poland", "hk": "波蘭", "ha": "波蘭", "tw": "波蘭", "cn": "波兰", "ja": "ポーランド", "ko": "폴란드", "fr": "Pologne"}),
	"de": ("🇩🇪", "Deutschland", {"en": "Germany", "hk": "德國", "ha": "德國", "tw": "德國", "cn": "德国", "ja": "ドイツ", "ko": "독일", "fr": "Allemagne"}),
	"cz": ("🇨🇿", "Česko", {"en": "Czech Republic", "hk": "捷克", "ha": "捷克", "tw": "捷克", "cn": "捷克", "ja": "チェコ", "ko": "체코", "fr": "Tchéquie"}),
	"at": ("🇦🇹", "Österreich", {"en": "Austria", "hk": "奧地利", "ha": "奧地利", "tw": "奧地利", "cn": "奧地利", "ja": "オーストリア", "ko": "오스트리아", "fr": "Autriche"}),
	"sk": ("🇸🇰", "Slovensko", {"en": "Slovakia", "hk": "斯洛伐克", "ha": "斯洛伐克", "tw": "斯洛伐克", "cn": "斯洛伐克", "ja": "スロバキア", "ko": "슬로바키아", "fr": "Slovaquie"}),
	"hu": ("🇭🇺", "Magyarország", {"en": "Hungary", "hk": "匈牙利", "ha": "匈牙利", "tw": "匈牙利", "cn": "匈牙利", "ja": "ハンガリー", "ko": "헝가리", "fr": "Hongrie"}),
	"ca": ("🇨🇦", "Canada", {"en": "Canada", "hk": "加拿大", "ha": "加拿大", "tw": "加拿大", "cn": "加拿大", "ja": "カナダ", "ko": "캐나다", "fr": "Canada"}),
	"gb": ("🇬🇧", "United Kingdom", {"en": "United Kingdom", "hk": "英國", "ha": "英國", "tw": "英國", "cn": "英国", "ja": "イギリス", "ko": "영국", "fr": "Royaume-Uni"}),
	"ie": ("🇮🇪", "Éire", {"en": "Ireland", "hk": "愛爾蘭", "ha": "愛爾蘭", "tw": "愛爾蘭", "cn": "爱尔兰", "ja": "アイルランド", "ko": "아일랜드", "fr": "Irlande"}),
	"kr": ("🇰🇷", "대한민국", {"en": "South Korea", "hk": "韓國", "ha": "韓國", "tw": "韓國", "cn": "韩国", "ja": "韓国", "ko": "대한민국", "fr": "Corée du Sud"}),
	"fr": ("🇫🇷", "France", {"en": "France", "hk": "法國", "ha": "法國", "tw": "法國", "cn": "法国", "ja": "フランス", "ko": "프랑스", "fr": "France"}),
	"mc": ("🇲🇨", "Monaco", {"en": "Monaco", "hk": "摩納哥", "ha": "摩納哥", "tw": "摩納哥", "cn": "摩纳哥", "ja": "モナコ", "ko": "모나코", "fr": "Monaco"}),
	"it": ("🇮🇹", "Italia", {"en": "Italy", "hk": "意大利", "ha": "意大利", "tw": "義大利", "cn": "意大利", "ja": "イタリア", "ko": "이탈리아", "fr": "Italie"}),
	"ch": ("🇨🇭", "Schweiz | Suisse | Svizzera | Svizra", {"en": "Switzerland", "hk": "瑞士", "ha": "瑞士", "tw": "瑞士", "cn": "瑞士", "ja": "スイス", "ko": "스위스", "fr": "Suisse"}),
	"lu": ("🇱🇺", "Lëtzebuerg | Luxembourg | Luxemburg", {"en": "Luxembourg", "hk": "盧森堡", "ha": "盧森堡", "tw": "盧森堡", "cn": "卢森堡", "ja": "ルクセンブルク", "ko": "룩셈부르크", "fr": "Luxembourg"}),
	"be": ("🇧🇪", "België | Belgique | Belgien", {"en": "Belgium", "hk": "比利時", "ha": "比利時", "tw": "比利時", "cn": "比利时", "ja": "ベルギー", "ko": "벨기에", "fr": "Belgique"}),
	"nl": ("🇳🇱", "Nederland", {"en": "Netherlands", "hk": "荷蘭", "ha": "荷蘭", "tw": "荷蘭", "cn": "荷兰", "ja": "オランダ", "ko": "네덜란드", "fr": "Pays-Bas"}),
	"es": ("🇪🇸", "España", {"en": "Spain", "hk": "西班牙", "ha": "西班牙", "tw": "西班牙", "cn": "西班牙", "ja": "スペイン", "ko": "스페인", "fr": "Espagne"}),
	"mx": ("🇲🇽", "México", {"en": "Mexico", "hk": "墨西哥", "ha": "墨西哥", "tw": "墨西哥", "cn": "墨西哥", "ja": "メキシコ", "ko": "멕시코", "fr": "Mexique"}),
	"dk": ("🇩🇰", "Danmark", {"en": "Denmark", "hk": "丹麥", "ha": "丹麥", "tw": "丹麥", "cn": "丹麦", "ja": "デンマーク", "ko": "덴마크", "fr": "Danemark"}),
	"se": ("🇸🇪", "Sverige", {"en": "Sweden", "hk": "瑞典", "ha": "瑞典", "tw": "瑞典", "cn": "瑞典", "ja": "スウェーデン", "ko": "스웨덴", "fr": "Suède"}),
	"fl": ("🇫🇮", "Suomi | Finland", {"en": "Finland", "hk": "芬蘭", "ha": "芬蘭", "tw": "芬蘭", "cn": "芬兰", "ja": "フィンランド", "ko": "핀란드", "fr": "Finlande"}),
	"ee": ("🇪🇪", "Eesti", {"en": "Estonia", "hk": "愛沙尼亞", "ha": "愛沙尼亞", "tw": "愛沙尼亞", "cn": "爱沙尼亚", "ja": "エストニア", "ko": "에스토니아", "fr": "Estonie"}),
	"lv": ("🇱🇻", "Latvija", {"en": "Latvia", "hk": "拉脫維亞", "ha": "拉脫維亞", "tw": "拉脫維亞", "cn": "拉脱维亚", "ja": "ラトビア", "ko": "라트비아", "fr": "Lettonie"}),
	"lt": ("🇱🇹", "Lietuva", {"en": "Lithuania", "hk": "立陶宛", "ha": "立陶宛", "tw": "立陶宛", "cn": "立陶宛", "ja": "リトアニア", "ko": "리투아니아", "fr": "Lituanie"}),
	"by": ("🇧🇾", "Беларусь", {"en": "Belarus", "hk": "白俄羅斯", "ha": "白俄羅斯", "tw": "白俄羅斯", "cn": "白俄罗斯", "ja": "ベラルーシ", "ko": "벨라루스", "fr": "Biélorussie"}),
	"ua": ("🇺🇦", "Україна", {"en": "Ukraine", "hk": "烏克蘭", "ha": "烏克蘭", "tw": "烏克蘭", "cn": "乌克兰", "ja": "ウクライナ", "ko": "우크라이나", "fr": "Ukraine"}),
	"pt": ("🇵🇹", "Portugal", {"en": "Portugal", "hk": "葡萄牙", "ha": "葡萄牙", "tw": "葡萄牙", "cn": "葡萄牙", "ja": "ポルトガル", "ko": "포르투갈", "fr": "Portugal"}),
	"ad": ("🇦🇩", "Andorra", {"en": "Andorra", "hk": "安道爾", "ha": "安道爾", "tw": "安道爾", "cn": "安道尔", "ja": "アンドラ", "ko": "안도라", "fr": "Andorre"}),
	"fo": ("🇫🇴", "Føroyar | Færøerne", {"en": "Faroe Islands", "hk": "法羅群島", "ha": "法羅群島", "tw": "法羅群島", "cn": "法罗群岛", "ja": "フェロー諸島", "ko": "페로 제도", "fr": "Îles Féroé"}),
	"is": ("🇮🇸", "Ísland", {"en": "Iceland", "hk": "冰島", "ha": "冰島", "tw": "冰島", "cn": "冰岛", "ja": "アイスランド", "ko": "아이슬란드", "fr": "Islande"}),
	"no": ("🇳🇴", "Norge | Noreg | Norga | Vuodna | Nöörje", {"en": "Norway", "hk": "挪威", "ha": "挪威", "tw": "挪威", "cn": "挪威", "ja": "ノルウェー", "ko": "노르웨이", "fr": "Norvège"}),
	"sg": ("🇸🇬", "Singapore | 新加坡 | Singapura | சிங்கப்பூர்", {"en": "Singapore", "hk": "新加坡", "ha": "新加坡", "tw": "新加坡", "cn": "新加坡", "ja": "シンガポール", "ko": "싱가포르", "fr": "Singapour"}),
	"id": ("🇮🇩", "Indonesia", {"en": "Indonesia", "hk": "印尼", "ha": "印尼", "tw": "印尼", "cn": "印尼", "ja": "インドネシア", "ko": "인도네시아", "fr": "Indonésie"}),
	"my": ("🇲🇾", "Malaysia", {"en": "Malaysia", "hk": "馬來西亞", "ha": "馬來西亞", "tw": "馬來西亞", "cn": "马来西亚", "ja": "マレーシア", "ko": "말레이시아", "fr": "Malaisie"}),
	"rs": ("🇷🇸", "Србија | Srbija", {"en": "Serbia", "hk": "塞爾維亞", "ha": "塞爾維亞", "tw": "塞爾維亞", "cn": "塞尔维亚", "ja": "セルビア", "ko": "세르비아", "fr": "Serbie"}),
	"ba": ("🇧🇦", "Bosna i Hercegovina | Босна и Херцеговина", {"en": "Bosnia and Herzegovina", "hk": "波斯尼亞和黑塞哥維那", "ha": "波斯尼亞和黑塞哥維那", "tw": "波士尼亞與赫塞哥維納", "cn": "波斯尼亚和黑塞哥维那", "ja": "ボスニア・ヘルツェゴビナ", "ko": "보스니아 헤르체고비나", "fr": "Bosnie-Herzégovine"}),
	"me": ("🇲🇪", "Црна Гора | Crna Gora", {"en": "Montenegro", "hk": "黑山", "ha": "黑山", "tw": "蒙特內哥羅", "cn": "黑山", "ja": "モンテネグロ", "ko": "몬테네그로", "fr": "Monténégro"}),
	"al": ("🇦🇱", "Shqipëria", {"en": "Albania", "hk": "阿爾巴尼亞", "ha": "阿爾巴尼亞", "tw": "阿爾巴尼亞", "cn": "阿尔巴尼亚", "ja": "アルバニア", "ko": "알바니아", "fr": "Albanie"})
	})

html_lang = {"en": "en", "cn": "zh-Hans", "hk": "zh-Hant", "ha": "zh-Hant", "tw": "zh-Hant", "ja": "ja", "ko": "ko", "fr": "fr"}
prompt_text = {"en": ("My travel history (page under development)", "Countries and regions visited"), 
	"cn": ("我的旅行记录 (未完成页面)", "我去过的地方"), 
	"hk": ("我的旅游記錄 (未完成頁面)", "我去過嘅地方"), 
	"ha": ("吾旅游記錄 (未完成頁面)", "涯去過个地方"), 
	"tw": ("我ㄟ旅游記錄 (未完成頁面)", "我有去過ㄟ所在"),
	"ja": ("私の旅行履歴 (未完成のページ)", "訪れたことのある場所"),
	"ko": ("저의 여행력 (미완성의 페이지)", "간 적이 있는 곳"), 
	"fr": ("Mes voyages (page incomplète)", "Les endroits que j'ai visités")}


for lang in ["en", "cn", "hk", "ha", "tw", "ja", "ko", "fr"]:
	open("travel_list_LANG.jemdoc".replace("LANG", lang), "w").write(
		"# jemdoc: menu{MENU_LANG}{travel_list_LANG.html}, lang-HTMLLANG\n" \
		"= {PROMPT1}\n" \
		"== {PROMPT2}\n".replace("{PROMPT1}", prompt_text[lang][0]).replace("{PROMPT2}", prompt_text[lang][1]).replace("HTMLLANG", html_lang[lang]).replace("LANG", lang) + 
		"\n".join([
			"- " + flag + " [" + country + ".html " + other_lang[lang] + ("]" if other_lang[lang] == native else " (" + native + ")]")
			for country, (flag, native, other_lang) in country_list.items()
			]) + "\n")


# Sub pages only available in English for now
country_sorted_by_en = sorted(country_list.items(), key=lambda item: item[1][2]["en"])
country_sorted_by_en = [code for code, _ in country_sorted_by_en]
country_sorted_by_en_idx_dict = {code: index for index, code in enumerate(country_sorted_by_en)}
country_sub_template = """# jemdoc: menu{MENU_en}{COUNTRY_CODE.html}, lang-en
= Travel to {COUNTRY}

[travel_list_en.html Back to list]

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
		prev_visit = "[" + list(country_list.items())[prev_visit_idx][0] + ".html ⬅Previous by order of first visit⬅]"
	if prev_alpha_idx == -1:
		prev_alpha = None
	else:
		prev_alpha = "[" + country_sorted_by_en[prev_alpha_idx] + ".html ⬅Previous by alphabetical order⬅]"
	if next_visit_idx == len(country_list):
		next_visit = None
	else:
		next_visit = "[" + list(country_list.items())[next_visit_idx][0] + ".html ➡️Next by order of first visit➡️]"
	if next_alpha_idx == len(country_list):
		next_alpha = None
	else:
		next_alpha = "[" + country_sorted_by_en[next_alpha_idx] + ".html ➡️Next by alphabetical order➡️]"
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




for index, (country, (flag, native, other_lang)) in enumerate(country_list.items()):
	if country + ".txt" not in os.listdir("."):
		open(country + ".txt", "w").write("DESCRIPTION:\n\nPHOTOS:\n")
	desc, photos = "".join(open(country + ".txt").readlines()).split("\nPHOTOS:\n")
	desc = re.sub(r"^DESCRIPTION:\n", "", desc).strip()
	photos = photos.strip()
	jemdoc_write = country_sub_template.replace("COUNTRY_CODE", country)
	jemdoc_write = jemdoc_write.replace("{COUNTRY}", flag + " " + other_lang["en"] + " (" + native + ")")
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




