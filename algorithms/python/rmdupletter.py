
import sys
import collections
import string

def rmNeiDupL(s):
	length = len(s)
	strlist = list(s)
	i = 0
	while i < length:
		if i+1 != length and s[i]==s[i+1]:
			del strlist[i]
			length -= 1
			
		i += 1
	s = ''.join(strlist)
	#print s
	return s


def removeDupLettersv2(s):
	s = rmNeiDupL(s)
	numsDic = collections.Counter(s)

	keys = numsDic.keys()
	keys.sort()

	okeys = []
	for i in s:
		if numsDic[i] == 1:
			okeys.append(i)

	result = ''
	length = len(s)

	for i in range(length):

		nowStr = s[i]
		if nowStr not in keys:
			continue

		pot = keys.index(nowStr)

		if len(okeys)>0 and nowStr == okeys[0]:
			result += nowStr
			del okeys[0]
			del keys[pot]
		elif numsDic[nowStr] == 1:
			result += nowStr
			del keys[pot]
		elif nowStr == keys[0]:
			result += nowStr
			del keys[0]
		elif len(okeys)>0 and nowStr<okeys[0]:
			j = i + 1
			while s[j] != okeys[0]:
				if s[j] < nowStr:
					numsDic[nowStr] -= 1
					break
				j += 1
			else:
				result += nowStr
				del keys[pot]
		else:
			numsDic[nowStr] -= 1
				

	return result



def removeDupLetters(s):
	length = len(s)
	strlist = list(s)
	for i in range(length):
		if i+1 != length and s[i]==s[i+1]:
			del strlist[i]
	s = ''.join(strlist)
		
	numsDic = collections.Counter(s)

	keys = numsDic.keys()
	keys.sort()

	okeys = []
	for i in s:
		if numsDic[i] == 1:
			okeys.append(i)
			del keys[keys.index(i)]

	result = ''
	length = len(s)
	for i in range(length):

		nowStr = s[i]
		if (nowStr not in keys) and (nowStr not in okeys):
			continue

		if nowStr in keys:
			pot = keys.index(nowStr)

		if len(okeys)>0 and nowStr == okeys[0]:
			result += nowStr
			del okeys[0]
		elif numsDic[nowStr] == 1:
			result += nowStr
			del keys[pot]
		elif nowStr == keys[0] and (len(okeys)>0 and nowStr < okeys[0] or len(okeys)==0):
			result += nowStr
			del keys[0]
		
		else:
			numsDic[nowStr] -= 1
				

	return result


def removeDuplicateLetters(s):

	strdic = {}
	for i in s:
		if i in strdic:
			strdic[i] += 1
		else:
			strdic[i] = 1
	keys = strdic.keys()
	keys.sort()
	result = ''
	
	#thesqtitxyetpxloeevdeqifkz
	#['d', 'e', 'f', 'h', 'i', 'k', 'l', 'o', 'p', 'q', 's', 't', 'v', 'x', 'y', 'z']

	for i in range(len(s)):
		length = len(keys)
		nowStr = s[i]
		if nowStr not in keys:
			continue
		pot = keys.index(nowStr)
		if strdic[nowStr]>1 and keys[0] != nowStr:		
			if pot != length -1:
				afStr = keys[pot+1]
				count = s[i:].count(afStr)

				temp = keys[:keys.index(nowStr)]
				for k in range(i+1, len(s)):
					if s[k] == afStr:
						count -= 1
					if count == 0:
						result += nowStr
						strdic[nowStr] = 0
						del keys[pot]
						break
					if s[k] != nowStr and s[k] in temp:
						strdic[nowStr] -= 1
						break
			else:
				strdic[nowStr] -= 1
						
			
		elif  strdic[nowStr] == 1:
			result += nowStr
			strdic[nowStr] = 0
			del keys[pot]
		elif keys[0] == nowStr:
			result += nowStr
			strdic[nowStr] = 0
			if len(keys) == 0:
				return result
			del keys[0]
	return result


if __name__ == '__main__':

	if len(sys.argv)  > 1:
		print removeDupLettersv2(sys.argv[1])
	else:
		numslist = []
		numslist.append('thesqtitxyetpxloeevdeqifkz')
		numslist.append('bcabc')
		numslist.append('cbacdcbc')
		numslist.append('ccacbaba')
		numslist.append('bccab')
		numslist.append("cbbbcaa")
		numslist.append("ccacbaba")
		numslist.append('cbcab')

		for i in numslist:
			print i, removeDupLettersv2(i)



#print removeDuplicateLetters('mhdmsfxmcrslmaruresdouolyectxamdpsyadwxltpepthuwmuvacpvbtkvmdbqcmgavrrekczzltkkgutugzmmjncldgnkegchtuxrpzizhleefdgmigzznislffgzgtkbdabgyxojtkbqfjbkyrscnhizvibuivpsghrhhyarkvyvmexqhdcykulfsqalqwlubzupydxhvugizyhrozdlbdnyuxrersbuilyvouljenqdrxngeydzdltnacxydjflhmrbbujtqjlkfpydheitdeodtyugqljimnjtezgrqpfjyutqpzqiqjpehazybiodbybmvrjjhetdfahqbkucfmaabnpqcsqgdkhiosbndodnpjhanggnhdogfqskxdcjpltdsatdqwtpotgcfhketubhiakfijsxfmjcxnmmoqmdwmfypvarlpxhxkecuyytqjhmxtceopslowsbkreezeggfpmrfrluwtebuuigytcwjywkfcdqbxjdfgcetcxbudzhosjztrzjpqwthtzifbizhqsczetbxmiqaoshnqbybhcpmlyivgtafvoenxdverstplcovvixevpnfdmofdvpiecdzoiysbgdtfxtorlzbjltvdhjumpxovscmrlenfocwpkjmjclqrcyoudfmgxavhnewngsjqlkujwyyqhtxhdmlnvlrrdqzerxxvofnhdotmopxbedqrjzhbdxqsropfmqojqtwlxnkyrlslxcstyppchdpwelytfpfpdarzktxalyrogonlownmxkgxpdvttcmpcrrupiyynibzcxbbhmfunlqcshgyytxnkjadcyckekvcrehlmchgmqbofsodrznqwdbagmdwpnhmheplylucaprzqoyvihitivzgpjqclhwfynhvnnksxvfbqpqdstcghliaxhfmsnhyezwllyrydwfcokzmjuiwgophogqsrumbedwmeiyzwspssgsvwummjvbpulaqlocwyxjhzdijaakwwnrjijwylqgbguachbckkfocbvxaijyxpcrxtsjxknchwlzdouazckvicjetspprzopkfhrtyfyoscixyudpsxcdmaibcmpdprzslnupbrormpglmjgfwutxwacixjdesrewechbbrpreiyvowzixzdiwpfxqnbqobpjuawizuzljbkhgvvgbdoudyhmfzzccwqiyifyjzgcnuogaotnsxyukmhvlikcrqejuvtxwwvdajfamntywqyydevbglgsqfyvvjkxtkfsckelnsuzznmpryqhcacoqshcnskspbqapzljtzhwohqqrkdgcdidwetltjwafphryvnvxyvupmnxmngtecynhgtrweivdwjsfkfqetwxcijdxgebfborhsobkisvwsknxagarcjktkialbqpaostniygbvspdxbhruarkkjnettuvpfsidpjoxexqjlltstwgxffmrslwyipbanjutfqbahpdrtubmncjzpwlgzkhixxuwtzsexydwdeuggeddqsqsfztehjewenxvslbipiudbhhkflgjqygsthabxtocwtqbobvsrqzpeoaroeqgvwfojsxzhruqwwcssqgnwujiscnszlzoohfvglqrrewlvnlxhuubiwgdwrkzpolvwojvqohsyfhgrmhrzemsrvbwnwkywzqgkkxylanyhjtvxvhtrsscnpypmtnouprbtokjhvxgfddiigixwdbylvsofdrmelkrzujntmrjxwmluqmhinqpdihmlafqyhyxcjcsovrpjaovnclwkwkhrqnnotzmqralxfbwneqkwwshgvvurrmoyxbullwxivocehrdmpalzuthuwjqctcvihttnnktfhrgbwumjazfupbrztilnffbzheqeacgfcmmssusszmqiheinygltehwwsaxuvjgedutckpxuwtbovdjcdxxzvkcxvqjlthxreuhasfhcftfutbeelffzvhvcbtmvtvlimzchuyjbaukrictblxiuueuqcrmikeobsoxlhhkjlvamuhupfmuqguqlifjgwwyvqbftaafsgtcliiyniqjcqwzjhgynkzvwdjwquvpizixrhsufytzlqifuuzmnyunqzpjkawxrndzjedmgbgrazowphnyzhyouoywmvfxqsrhjygcwhvjkrlnyddklpblccgmbirdahrjwiyrhnfjpzlrravybzggklkoluiszjiznrpntndpvzqibtqzsaadpriizksjzevjcvxweurahisliczephpfjuuqgrdtalvliwzooqibplvaezhmqeakaasnamdditqrshmtxzvxdhjducjrgnrgjxfqyzwcgunzfyozoufithynydpbavlvovvfbvbkekzlibskkhjysyteyesvfzpztqbdqmefebulnhfufdiknruvjdfedaycumzditjeptpsgarhzynzxfttlujmltopejadhqyixoqumhxbdcaykhfngtdfmemaffrbroxpuezoyzkmqdyfvouywoqekpmllnkafeznzxhvhruzqomohrrloncoenurnxyzgzcronxhcupgsvogwuuxdaavvpcybkmatyabbtfszfvzldlzlekdcvvksugklzvsgqjdxcyvmnezsxrwfdgedhigfilkeiccsmhwqwhhspvbxpysksuwwkcjowhpecfqazdtqejqleezmuzlrfdsvpvncrxvtotiscpmsajnhfllbhfgdjgfjdihfuaymitdjejluccluzgbtcspagfcdcgwnhpzdyqaoqxpqytuxdhwgxwxziqecrkwqoofwanbkynizqambwzvmcjxvkeiqrjunmwwrwhelrocbtmadcceytohbjvxtovdtclilabmabqaolwhhgsraxorjohwxaldttbkswtaxlhpwxcncoxfotnmnkykahsijmuouvsjhtznerqbztftzppvptgfzhdteutcuchhhgkggwzqgdthzowcovxoemlhzaovgrcolakvioduybljadfawdprvuaewqqacbsvdrtvraqdqkrfvinclajunqlvkkpvxofhdqygbuukaplicqaiezdeolkzsnlwbpttvtrwsmiejzjjjfaeqkxgvhjagjnpuubnhgazhcsniznympivmspsiliqttprnyulpumkmvtcrccfqeqyhtjwfsbsitvhshgajibgvbkrphyxdjnhpewlvwnjokffvzkirqxhxjqglrvwjuihqjmncmefncpvrylippcrouprqzlwtctcphfuyilqbmjcemizbdcwqyskwcoexfbuyvtzviftgjlpkbivjrndtwvvocjplfbdtoobxeonzawymfctomlnsdikleqtozyhyftapkfpsqotmmitshrmldcdrupeadrkaroagwexxspekqdizgbzksakprgpderigvzvcgbfdjfyujeroubuuekivlnvoeplpgkwbmfuxweqbosqsqdfbthfqtvkplrvjphenmlbkcrephmtqfzlorcozieegnylznzjesnhpcmcgvzjqlikfukevbyydpxdkvcyxwysupnfnshvaqmhahevnexaxfyiatwrmodobzaemhfvcxbghdfhllpwpmcnoixqxrppbfnbraqitaxdgqtnsxtvqfduhclkrjzgbhbglicgdbmhirhgqvbnomybtembcryzuskxqudtbmvbeqyuutzgiqnntahihpoyfcahmucjlxofwjryjjfytgedaholssotycxhywdzyzdvlvbzxertxeipcklyjkrvcnnveqtudgkaewerdnrviabaamuyymumquprichjcctmervgmxrtuaxtxfvjpdcvwghnwkfbiqpivwvnleopvcncxxtatzbkfabmbgsosezazvxvevyjevuxhpyqncszmzlnlxbxfvrwkmmywuhqgceleiinnwrytshcigzelnrfpbadewyappzrjwzfqxiyjcbmzjvwzldbiicpwlnpvlgzfxtmvgxjdwjzifesaxozhnsubqtfaztagwbrjksnxdazxdpquwyklsogucuiixspqkpnipciomejhjgjoxgemkuijeawaqkwgmsmuvzbhkzbqoazxdglexgxbhveggxfzkxqsukvujamqsiwpdilqedzzgqcttkdabpmybkpyipuujpofqjpivzzautmvcfbyjzwyalxgxotsnazalicoxdzggxmafplrrrcecgfwkdkentjwjjiheutxfuxspdgvhcgyziobkwwndvhsvlfzlcjbicyxsdbhqigzewhixlxjqbknanywfyfduuvegiumtnpilzrerafyaylrpnjtsktbvavkdhxfzwirqawpzqbjopyfiukijyhtieevzldnxrkmtqedullaqorikoelfirmdkkxhfbkeiwpivooztijfmazvyumaqnfvcwwpmjnlfisvohttiqihwyknocbqloxokuwsrjhtoasiivununmefyrxaigcnagxareuciubdxatbmfieyboyrefthnhfyhufosfqdjeehgounlkgwpgluqthhnlypnxbexuqyhnaeppdfjgwpbibhjeeptwbzsvcebzwosynxkzfoaygrnnrgjdmfucnunkjnervmfwxskwibhlwdzzgppxhzdqsjnqrpxdlabbcdtxqpuptpmjtfovtmvgrxxremgbfzgcdcxuackddqgfkvzkwjxhtonbhujcrjpnqnswqswlkubxwyzpnculzjfvulqrnunvgotzkuyisjktxiwreftbalczvluoimahmsuupjmqrurrtttrdtivwkyxbypxqhlgnrvsortiqzirykcnpcjzasjcoxlwrpjpajfzbndlrbdrgcyydxdhtsjltqdfgbijxpepysmsyhblomaufoafcjabrdhtompxdjgssioytkedqoomktrfaxiarjrbjmnyezcwlfxqkrkazammudqhndfnkemdvjnbahkbmmpltzupwnybqdbrkmujsmoyttnhwhydgioatmygrosgsjmnawkxwchtpgcrkfrwvligaoowrrburrlzglozydsqnepqdvveagdjetzfcgupymxxbmfheydayaevamouyqlebnngackvtcpsuopuoawrkhwcnnqnstcrvcspqerredtahrkdnfdzapmyqzgplrepjsxznjsesiduxyslnlhlssszwtonxfmovkikbfopiyjmnfnztesldstolqyplczbpgrexwnfwzfdausdsyicchmfpebljwbvlqbrwdoeflmfvlgbxukuztxngftwjzvjntolpzcmflevmsnmlqmrxtdtwkmwtelrleeklaamfduqsdmhmvypaxzszcjytyurujeqriythhkoyurhrvbyqmozdnissivkwmiprrvieamftbjoicbjpvcphnnkmmjnrzqxclwrvnxjcohjhzwexgcjjrfyaisvvjccokxfycbaqwqgnylitmfyvdambrtbghcvbhbbvpeglhpvyawvxzphyjswgebbrpxyrnaczjmfyukvtdhtevbrisuoquynkrsysixsuktswwxynnmnnsqpgrappzlcnmflaubfkxowvzrwkxcjrseziwqvcdbfmcykajdephktudjosklyqpaqtbbnsdrvvbhjzbkybhryffalyczubankkrjbgtfkfvahdukeyybcxsfaudvgcchsraoxbqxbiemrudhjgfelwemkyeralmbgvtgqhvgpskmpvwaxsxqkksmbwrgisuydnyfmlucdfbujuqqyypcfotidqheyusosjfwcigdbppgrqwwveslwylqpaxfgjhmwxzodxjzjlwqtqonzggcjheevverggvtgejrlhwhatyydofnhmanobpntflkmrtnbsfxskzayrbrnbobxduitrlracnnaoqxebhogbrfbvebvvryopqlaeammwjhaiamqjoutptupvhctgemqizzxcficnognbilaawyldlmyrizaewcckefcehjrcpgiwuglwctywoofoaohlhlcqrynvmrybyblxftobasfskesimnyaqvlwmugaaupyclnwfieaampmfzhlgfivgoahejpacouzjhofcgczzaqhmszpmqpznfcuvbuvzhogbpgpmbaeljdgqjiulwrfokckeydozdvlpoaykdnbfjtgehnzjomelzrobfvzfmpfwuypazfgeteearekcczvrleoyrqudbiserphcrzyielrqewnlmgqldkzsdtrzwqolnttodzrbkwtzmlcrjiqttyftnhujnodccqndjefblvjwjqlarxcheacydskzhwbpzwqwkputfzusjgssstboytyhlbhrlmxctvsizbocnwuhrsccroujafkauxkrzlvsatrjhjoulhkxlxtwstdqrpibjwupkppkqmrnykoppecttmjxnstathqglcdpxhponvkzfnmhwvkugmtxecvcfqoyqlaclrdgdutsbladuggcpgkqrdawcqckuzrqfynrtewvqloyhmorpvchzntyhmjzlbfezeallvyoovzuvnlufswwdkslnyuecqmvzkiwqjmfkhvjnmvgzikahzocejltveeropdnazdpsicaihbntrqkbemhmuzeoqcwfiodvvutwwywluykmcnojwhhcwdscvkfxgwissbrazrrqfpshbjotiedrgdppdwtdcvwjhddogdzarvrztxyyqtnojothpjenfoesovqidpaiumrrkajhatfesxrdfshmufudlrtznfxcddhpfkkiawktxmbzctvbwpxbgiyslnlwjhayjlffmmbbonfhoqoutmjmxmqpuzkdefizbceaolibmchcadyqsxqgacebfjsswaaoenybknjpzhfumxestvpwtgswnysetqxupklnmpfnpnjryzdixolcisazlcvemwlyfrlmmhhzdkdpyvtuqquslvnhafjfkdiozuhmhocuhwivodtxlxuydzeyzzqegarbwvqiwpuvybzxyaalknyzxprrxmevzofurvqcbohpvjxtoemqevcynhftvhwmtwwtjalirukkhvxmhclontxpuafpwknwmwxdbashjtsznrkazngrmzbwoznypkdhalpvgrlflkejkbybjnemwzobzyfkysymmeubqzbgerkswxyojlrtyuzuwgydcdnroyokyhbpqesvtzabjgeabwwnlojsxieodeenonaqliptriswkdzcgfwjljeujdpmxsraizvdlvuqsmfwunkoafcjkemmlzbztfzmtdtvidjdvnxvwvvengcfajvtbsltpmisbhjyoraldphjxgmbyridhvltnqtutovnetksxagcbcsovypspzipjiidqqjyhqxptsloriuflxshqkssluvwyecchuqapazctewywnsjcalgmzxrcrycapnshukvvrrkhxcksbhfmubhdtuordlpsvvfduwbvrzswecwxrauqyvxlzcwgsucidisaglajsokzkhmzeheqvbkkxrzcphhzzahtqpchudofpsftgcjleprkzqcxqjuhmimgoelhyxvqwsopvmuothuviqymknnevoryficlkkifvoveagwwzxxsbtpmuphlzhybzavpmkagwtcktqkeovskupsuxsywxwncokqdhueaaqnoyjsxsizrepudbqyindauqecyymgjnpswktjauozkowpkjjcseezhasjsjpnsenkentcqgzclrmsgnuygjwqegglgcsufmicgwmlkbuxfqsogzfjiksjpdgrbjzprmwqkjojtwzkyuxwhhvrwmissqxsrhvyilasetwfitstpntcyrmaadhmuevzbbakftcqqbqkmuzlkqwrsisagkmjqswgsvnffjbgkvywioaabndgvwwnynxxnoikobyxvjcjuajwirdimyldarbosknvebwhfjuugntzwyqetffjlfcnffbuesymybtsxgiwpjayuznxwcgioajtqeorvzswicpfqhsntnhhvjrqcoqlzvdxydpkkchetlbwoexfpyjmokfnxzfiahakdsculjdxuwzkbftuimpxhnfawwgcffodpljgzhwyrybzkziwqhxbbkentxopopqetuhgkhbwwoixyyftsnfwcyecjoxbqjjaevbwhzibccbcldttaulcwwfztzehtutgfihwsgafjwmtevpyfvggmndmcsbnewpovordalmxklvzuelivmjagqqpzmczhefrhdyobvomkjhlpvlfljuorvwyvliahlbiazxwvnpjxombyuiqjsvdvvmrtjykyjrxtyabsjgpcoiodpzbdnrvczdazesbtrtrxqjsuwbetvapcujysdtiaeojoouhzxfhegsmvumtjpxqnvsaxcbzjdjjmzpdqnxczqszbtgubyvtydwytntwvskssqnggertcikdkpisgvekzushltzzfedcmtsthfvyucseiceqrajr')
