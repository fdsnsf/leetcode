
import sys
import collections
import string

def rmNeiDupL(s):
	length = len(s)
	strlist = list(s)
	i = 0
	while i < length:
		if i+1 != length and strlist[i]==strlist[i+1]:
			del strlist[i]
			length -= 1
		else:
			i += 1
	s = ''.join(strlist)
	#print s
	return s

def addokeys(okeys, okeysdic, pot, nowStr):
	for i in range(len(okeys)):
		if okeysdic[okeys[i]] > pot:
			okeys.insert(i, nowStr)
			okeysdic[nowStr] = pot
			break
	else:
		okeys.append(nowStr)
		okeysdic[nowStr] = pot
	return okeys,okeysdic


def removeDupLettersv2(s):
	s = rmNeiDupL(s)
	numsDic = collections.Counter(s)

	keys = numsDic.keys()
	keys.sort()

	okeys = []
	length = len(s)
	okeysdic = {}
	for i in range(length):
		if numsDic[s[i]] == 1:
			okeys.append(s[i])
			okeysdic[s[i]] = i

	result = ''
	

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

		elif len(okeys)>0:
			j = i + 1
			tempDic = {}
			while s[j] != okeys[0]:
				if s[j] in tempDic:
					tempDic[s[j]] += 1
				else:
					tempDic[s[j]] = 1
				if s[j] in keys and s[j] < nowStr:
					numsDic[nowStr] -= 1
					if numsDic[nowStr] == 1:
						okeys,okeysdic = addokeys(okeys, okeysdic, i+1+s[i+1:].index(nowStr), nowStr)
					break				 
				if s[j] in keys and tempDic[s[j]] == numsDic[s[j]] and nowStr < s[j]:
					result += nowStr
					del keys[pot]
					break
				j += 1
			else:
				if nowStr>okeys[0]:
					numsDic[nowStr] -= 1
					if numsDic[nowStr] == 1:
						okeys,okeysdic = addokeys(okeys, okeysdic, i+1+s[i+1:].index(nowStr), nowStr)
				else:
					result += nowStr
					del keys[pot]
		else:
			numsDic[nowStr] -= 1
			if numsDic[nowStr] == 1:
				okeys,okeysdic = addokeys(okeys, okeysdic, i+1+s[i+1:].index(nowStr), nowStr)
				

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

#thesqtitxyetpxloeevdeqifkz	hesitxyplovdqfkz
#bcabc    	abc
#cbacdcbc 	acdb
#ccacbaba 	acb
#bccab 		bca
#cbbbcaa 	bca
#ccacbaba 	acb
#cbcab 		bca
#mitnlruhznjfyzmtmfnstsxwktxlboxutbic	ilrhjfyzmnstwkboxuc
#rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws		bfegkuyjorndiqszpcaw
#bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv	bhcsdikworfltuzjxaympev
#eywdgenmcnzhztolafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm	chzafipuegjlxdqnbsotwrym
#lllllllllllmmmmmmmmmmmnnnnnnnnnnnooooooooooopppppppppppqqqqqqqqqqqrrrrrrrrrrrssssssssssstttttttttttuuuuuuuuuuuvvvvvvvvvvvwwwwwwwwwaaaaaaaaaaabbbbbbbbbbbcccccccccccdddddddddddeeeeeeeeeeefffffffffffggggggggggghhhhhhhhhhhiiiiiiiiiiijjjjjjjjjjjkkkkkkkkkkklllllllll		lmnopqrstuvwabcdefghijk
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
		numslist.append('mitnlruhznjfyzmtmfnstsxwktxlboxutbic')
		numslist.append("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")
		numslist.append('bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv')
		numslist.append('eywdgenmcnzhztolafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm')
		numslist.append('lllllllllllmmmmmmmmmmmnnnnnnnnnnnooooooooooopppppppppppqqqqqqqqqqqrrrrrrrrrrrssssssssssstttttttttttuuuuuuuuuuuvvvvvvvvvvvwwwwwwwwwaaaaaaaaaaabbbbbbbbbbbcccccccccccdddddddddddeeeeeeeeeeefffffffffffggggggggggghhhhhhhhhhhiiiiiiiiiiijjjjjjjjjjjkkkkkkkkkkklllllllll')

		for i in numslist:
			print i, removeDupLettersv2(i)



#print removeDuplicateLetters('mhdmsfxmcrslmaruresdouolyectxamdpsyadwxltpepthuwmuvacpvbtkvmdbqcmgavrrekczzltkkgutugzmmjncldgnkegchtuxrpzizhleefdgmigzznislffgzgtkbdabgyxojtkbqfjbkyrscnhizvibuivpsghrhhyarkvyvmexqhdcykulfsqalqwlubzupydxhvugizyhrozdlbdnyuxrersbuilyvouljenqdrxngeydzdltnacxydjflhmrbbujtqjlkfpydheitdeodtyugqljimnjtezgrqpfjyutqpzqiqjpehazybiodbybmvrjjhetdfahqbkucfmaabnpqcsqgdkhiosbndodnpjhanggnhdogfqskxdcjpltdsatdqwtpotgcfhketubhiakfijsxfmjcxnmmoqmdwmfypvarlpxhxkecuyytqjhmxtceopslowsbkreezeggfpmrfrluwtebuuigytcwjywkfcdqbxjdfgcetcxbudzhosjztrzjpqwthtzifbizhqsczetbxmiqaoshnqbybhcpmlyivgtafvoenxdverstplcovvixevpnfdmofdvpiecdzoiysbgdtfxtorlzbjltvdhjumpxovscmrlenfocwpkjmjclqrcyoudfmgxavhnewngsjqlkujwyyqhtxhdmlnvlrrdqzerxxvofnhdotmopxbedqrjzhbdxqsropfmqojqtwlxnkyrlslxcstyppchdpwelytfpfpdarzktxalyrogonlownmxkgxpdvttcmpcrrupiyynibzcxbbhmfunlqcshgyytxnkjadcyckekvcrehlmchgmqbofsodrznqwdbagmdwpnhmheplylucaprzqoyvihitivzgpjqclhwfynhvnnksxvfbqpqdstcghliaxhfmsnhyezwllyrydwfcokzmjuiwgophogqsrumbedwmeiyzwspssgsvwummjvbpulaqlocwyxjhzdijaakwwnrjijwylqgbguachbckkfocbvxaijyxpcrxtsjxknchwlzdouazckvicjetspprzopkfhrtyfyoscixyudpsxcdmaibcmpdprzslnupbrormpglmjgfwutxwacixjdesrewechbbrpreiyvowzixzdiwpfxqnbqobpjuawizuzljbkhgvvgbdoudyhmfzzccwqiyifyjzgcnuogaotnsxyukmhvlikcrqejuvtxwwvdajfamntywqyydevbglgsqfyvvjkxtkfsckelnsuzznmpryqhcacoqshcnskspbqapzljtzhwohqqrkdgcdidwetltjwafphryvnvxyvupmnxmngtecynhgtrweivdwjsfkfqetwxcijdxgebfborhsobkisvwsknxagarcjktkialbqpaostniygbvspdxbhruarkkjnettuvpfsidpjoxexqjlltstwgxffmrslwyipbanjutfqbahpdrtubmncjzpwlgzkhixxuwtzsexydwdeuggeddqsqsfztehjewenxvslbipiudbhhkflgjqygsthabxtocwtqbobvsrqzpeoaroeqgvwfojsxzhruqwwcssqgnwujiscnszlzoohfvglqrrewlvnlxhuubiwgdwrkzpolvwojvqohsyfhgrmhrzemsrvbwnwkywzqgkkxylanyhjtvxvhtrsscnpypmtnouprbtokjhvxgfddiigixwdbylvsofdrmelkrzujntmrjxwmluqmhinqpdihmlafqyhyxcjcsovrpjaovnclwkwkhrqnnotzmqralxfbwneqkwwshgvvurrmoyxbullwxivocehrdmpalzuthuwjqctcvihttnnktfhrgbwumjazfupbrztilnffbzheqeacgfcmmssusszmqiheinygltehwwsaxuvjgedutckpxuwtbovdjcdxxzvkcxvqjlthxreuhasfhcftfutbeelffzvhvcbtmvtvlimzchuyjbaukrictblxiuueuqcrmikeobsoxlhhkjlvamuhupfmuqguqlifjgwwyvqbftaafsgtcliiyniqjcqwzjhgynkzvwdjwquvpizixrhsufytzlqifuuzmnyunqzpjkawxrndzjedmgbgrazowphnyzhyouoywmvfxqsrhjygcwhvjkrlnyddklpblccgmbirdahrjwiyrhnfjpzlrravybzggklkoluiszjiznrpntndpvzqibtqzsaadpriizksjzevjcvxweurahisliczephpfjuuqgrdtalvliwzooqibplvaezhmqeakaasnamdditqrshmtxzvxdhjducjrgnrgjxfqyzwcgunzfyozoufithynydpbavlvovvfbvbkekzlibskkhjysyteyesvfzpztqbdqmefebulnhfufdiknruvjdfedaycumzditjeptpsgarhzynzxfttlujmltopejadhqyixoqumhxbdcaykhfngtdfmemaffrbroxpuezoyzkmqdyfvouywoqekpmllnkafeznzxhvhruzqomohrrloncoenurnxyzgzcronxhcupgsvogwuuxdaavvpcybkmatyabbtfszfvzldlzlekdcvvksugklzvsgqjdxcyvmnezsxrwfdgedhigfilkeiccsmhwqwhhspvbxpysksuwwkcjowhpecfqazdtqejqleezmuzlrfdsvpvncrxvtotiscpmsajnhfllbhfgdjgfjdihfuaymitdjejluccluzgbtcspagfcdcgwnhpzdyqaoqxpqytuxdhwgxwxziqecrkwqoofwanbkynizqambwzvmcjxvkeiqrjunmwwrwhelrocbtmadcceytohbjvxtovdtclilabmabqaolwhhgsraxorjohwxaldttbkswtaxlhpwxcncoxfotnmnkykahsijmuouvsjhtznerqbztftzppvptgfzhdteutcuchhhgkggwzqgdthzowcovxoemlhzaovgrcolakvioduybljadfawdprvuaewqqacbsvdrtvraqdqkrfvinclajunqlvkkpvxofhdqygbuukaplicqaiezdeolkzsnlwbpttvtrwsmiejzjjjfaeqkxgvhjagjnpuubnhgazhcsniznympivmspsiliqttprnyulpumkmvtcrccfqeqyhtjwfsbsitvhshgajibgvbkrphyxdjnhpewlvwnjokffvzkirqxhxjqglrvwjuihqjmncmefncpvrylippcrouprqzlwtctcphfuyilqbmjcemizbdcwqyskwcoexfbuyvtzviftgjlpkbivjrndtwvvocjplfbdtoobxeonzawymfctomlnsdikleqtozyhyftapkfpsqotmmitshrmldcdrupeadrkaroagwexxspekqdizgbzksakprgpderigvzvcgbfdjfyujeroubuuekivlnvoeplpgkwbmfuxweqbosqsqdfbthfqtvkplrvjphenmlbkcrephmtqfzlorcozieegnylznzjesnhpcmcgvzjqlikfukevbyydpxdkvcyxwysupnfnshvaqmhahevnexaxfyiatwrmodobzaemhfvcxbghdfhllpwpmcnoixqxrppbfnbraqitaxdgqtnsxtvqfduhclkrjzgbhbglicgdbmhirhgqvbnomybtembcryzuskxqudtbmvbeqyuutzgiqnntahihpoyfcahmucjlxofwjryjjfytgedaholssotycxhywdzyzdvlvbzxertxeipcklyjkrvcnnveqtudgkaewerdnrviabaamuyymumquprichjcctmervgmxrtuaxtxfvjpdcvwghnwkfbiqpivwvnleopvcncxxtatzbkfabmbgsosezazvxvevyjevuxhpyqncszmzlnlxbxfvrwkmmywuhqgceleiinnwrytshcigzelnrfpbadewyappzrjwzfqxiyjcbmzjvwzldbiicpwlnpvlgzfxtmvgxjdwjzifesaxozhnsubqtfaztagwbrjksnxdazxdpquwyklsogucuiixspqkpnipciomejhjgjoxgemkuijeawaqkwgmsmuvzbhkzbqoazxdglexgxbhveggxfzkxqsukvujamqsiwpdilqedzzgqcttkdabpmybkpyipuujpofqjpivzzautmvcfbyjzwyalxgxotsnazalicoxdzggxmafplrrrcecgfwkdkentjwjjiheutxfuxspdgvhcgyziobkwwndvhsvlfzlcjbicyxsdbhqigzewhixlxjqbknanywfyfduuvegiumtnpilzrerafyaylrpnjtsktbvavkdhxfzwirqawpzqbjopyfiukijyhtieevzldnxrkmtqedullaqorikoelfirmdkkxhfbkeiwpivooztijfmazvyumaqnfvcwwpmjnlfisvohttiqihwyknocbqloxokuwsrjhtoasiivununmefyrxaigcnagxareuciubdxatbmfieyboyrefthnhfyhufosfqdjeehgounlkgwpgluqthhnlypnxbexuqyhnaeppdfjgwpbibhjeeptwbzsvcebzwosynxkzfoaygrnnrgjdmfucnunkjnervmfwxskwibhlwdzzgppxhzdqsjnqrpxdlabbcdtxqpuptpmjtfovtmvgrxxremgbfzgcdcxuackddqgfkvzkwjxhtonbhujcrjpnqnswqswlkubxwyzpnculzjfvulqrnunvgotzkuyisjktxiwreftbalczvluoimahmsuupjmqrurrtttrdtivwkyxbypxqhlgnrvsortiqzirykcnpcjzasjcoxlwrpjpajfzbndlrbdrgcyydxdhtsjltqdfgbijxpepysmsyhblomaufoafcjabrdhtompxdjgssioytkedqoomktrfaxiarjrbjmnyezcwlfxqkrkazammudqhndfnkemdvjnbahkbmmpltzupwnybqdbrkmujsmoyttnhwhydgioatmygrosgsjmnawkxwchtpgcrkfrwvligaoowrrburrlzglozydsqnepqdvveagdjetzfcgupymxxbmfheydayaevamouyqlebnngackvtcpsuopuoawrkhwcnnqnstcrvcspqerredtahrkdnfdzapmyqzgplrepjsxznjsesiduxyslnlhlssszwtonxfmovkikbfopiyjmnfnztesldstolqyplczbpgrexwnfwzfdausdsyicchmfpebljwbvlqbrwdoeflmfvlgbxukuztxngftwjzvjntolpzcmflevmsnmlqmrxtdtwkmwtelrleeklaamfduqsdmhmvypaxzszcjytyurujeqriythhkoyurhrvbyqmozdnissivkwmiprrvieamftbjoicbjpvcphnnkmmjnrzqxclwrvnxjcohjhzwexgcjjrfyaisvvjccokxfycbaqwqgnylitmfyvdambrtbghcvbhbbvpeglhpvyawvxzphyjswgebbrpxyrnaczjmfyukvtdhtevbrisuoquynkrsysixsuktswwxynnmnnsqpgrappzlcnmflaubfkxowvzrwkxcjrseziwqvcdbfmcykajdephktudjosklyqpaqtbbnsdrvvbhjzbkybhryffalyczubankkrjbgtfkfvahdukeyybcxsfaudvgcchsraoxbqxbiemrudhjgfelwemkyeralmbgvtgqhvgpskmpvwaxsxqkksmbwrgisuydnyfmlucdfbujuqqyypcfotidqheyusosjfwcigdbppgrqwwveslwylqpaxfgjhmwxzodxjzjlwqtqonzggcjheevverggvtgejrlhwhatyydofnhmanobpntflkmrtnbsfxskzayrbrnbobxduitrlracnnaoqxebhogbrfbvebvvryopqlaeammwjhaiamqjoutptupvhctgemqizzxcficnognbilaawyldlmyrizaewcckefcehjrcpgiwuglwctywoofoaohlhlcqrynvmrybyblxftobasfskesimnyaqvlwmugaaupyclnwfieaampmfzhlgfivgoahejpacouzjhofcgczzaqhmszpmqpznfcuvbuvzhogbpgpmbaeljdgqjiulwrfokckeydozdvlpoaykdnbfjtgehnzjomelzrobfvzfmpfwuypazfgeteearekcczvrleoyrqudbiserphcrzyielrqewnlmgqldkzsdtrzwqolnttodzrbkwtzmlcrjiqttyftnhujnodccqndjefblvjwjqlarxcheacydskzhwbpzwqwkputfzusjgssstboytyhlbhrlmxctvsizbocnwuhrsccroujafkauxkrzlvsatrjhjoulhkxlxtwstdqrpibjwupkppkqmrnykoppecttmjxnstathqglcdpxhponvkzfnmhwvkugmtxecvcfqoyqlaclrdgdutsbladuggcpgkqrdawcqckuzrqfynrtewvqloyhmorpvchzntyhmjzlbfezeallvyoovzuvnlufswwdkslnyuecqmvzkiwqjmfkhvjnmvgzikahzocejltveeropdnazdpsicaihbntrqkbemhmuzeoqcwfiodvvutwwywluykmcnojwhhcwdscvkfxgwissbrazrrqfpshbjotiedrgdppdwtdcvwjhddogdzarvrztxyyqtnojothpjenfoesovqidpaiumrrkajhatfesxrdfshmufudlrtznfxcddhpfkkiawktxmbzctvbwpxbgiyslnlwjhayjlffmmbbonfhoqoutmjmxmqpuzkdefizbceaolibmchcadyqsxqgacebfjsswaaoenybknjpzhfumxestvpwtgswnysetqxupklnmpfnpnjryzdixolcisazlcvemwlyfrlmmhhzdkdpyvtuqquslvnhafjfkdiozuhmhocuhwivodtxlxuydzeyzzqegarbwvqiwpuvybzxyaalknyzxprrxmevzofurvqcbohpvjxtoemqevcynhftvhwmtwwtjalirukkhvxmhclontxpuafpwknwmwxdbashjtsznrkazngrmzbwoznypkdhalpvgrlflkejkbybjnemwzobzyfkysymmeubqzbgerkswxyojlrtyuzuwgydcdnroyokyhbpqesvtzabjgeabwwnlojsxieodeenonaqliptriswkdzcgfwjljeujdpmxsraizvdlvuqsmfwunkoafcjkemmlzbztfzmtdtvidjdvnxvwvvengcfajvtbsltpmisbhjyoraldphjxgmbyridhvltnqtutovnetksxagcbcsovypspzipjiidqqjyhqxptsloriuflxshqkssluvwyecchuqapazctewywnsjcalgmzxrcrycapnshukvvrrkhxcksbhfmubhdtuordlpsvvfduwbvrzswecwxrauqyvxlzcwgsucidisaglajsokzkhmzeheqvbkkxrzcphhzzahtqpchudofpsftgcjleprkzqcxqjuhmimgoelhyxvqwsopvmuothuviqymknnevoryficlkkifvoveagwwzxxsbtpmuphlzhybzavpmkagwtcktqkeovskupsuxsywxwncokqdhueaaqnoyjsxsizrepudbqyindauqecyymgjnpswktjauozkowpkjjcseezhasjsjpnsenkentcqgzclrmsgnuygjwqegglgcsufmicgwmlkbuxfqsogzfjiksjpdgrbjzprmwqkjojtwzkyuxwhhvrwmissqxsrhvyilasetwfitstpntcyrmaadhmuevzbbakftcqqbqkmuzlkqwrsisagkmjqswgsvnffjbgkvywioaabndgvwwnynxxnoikobyxvjcjuajwirdimyldarbosknvebwhfjuugntzwyqetffjlfcnffbuesymybtsxgiwpjayuznxwcgioajtqeorvzswicpfqhsntnhhvjrqcoqlzvdxydpkkchetlbwoexfpyjmokfnxzfiahakdsculjdxuwzkbftuimpxhnfawwgcffodpljgzhwyrybzkziwqhxbbkentxopopqetuhgkhbwwoixyyftsnfwcyecjoxbqjjaevbwhzibccbcldttaulcwwfztzehtutgfihwsgafjwmtevpyfvggmndmcsbnewpovordalmxklvzuelivmjagqqpzmczhefrhdyobvomkjhlpvlfljuorvwyvliahlbiazxwvnpjxombyuiqjsvdvvmrtjykyjrxtyabsjgpcoiodpzbdnrvczdazesbtrtrxqjsuwbetvapcujysdtiaeojoouhzxfhegsmvumtjpxqnvsaxcbzjdjjmzpdqnxczqszbtgubyvtydwytntwvskssqnggertcikdkpisgvekzushltzzfedcmtsthfvyucseiceqrajr')
