
#coding=utf-8

import sys
import collections
import string

def rmNeiDupL(s):
	"""
    相邻且相同的字符只保留一个
	"""
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
	"""
	okeys为只出现一次的字符，而且按出现的顺序排序，okeysdic为这些字母在原始字符串中的位置，出现新的只有一次的字母，插入okeys中
	"""
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
	"""
	    这个题是给出一个字符串，求出所出现的字符组成的子串，字串中的字符的顺序是在原始字符串中的相对位置，且子串是字典序最小的一个
    最开始也想着求出所有字串，然后按字典排序求出最小的，但是想着这样会求出很多无用的结果，就直接奔着一个for循环求出最终的结果，
    虽然也accept了，但这个过程很痛苦，换了两个方案才算出来了，而且肯定还有优化的空间。
        基本思路是维护了两个列表和一个两个字典，中间还有一个临时的字典
    维护一个list，list中存放原始字符串中只出现一次的字符，这些这些字符出现在最终结果中的位置也肯定是固定的，遇到这些字符是直接可以放到结果中的。
    还有一个list（keys）放入所有字符，并按字典排序，遇到这种字符也是直接放入结果中。一个字典numsDic存放keys中字符在原始字符串中出现的次数，
    若次数为1是直接可以放入结果中的。还有一个字典okeysdic。
        下来就是一般情况，以okeys划分按段来判断，如果当前字符为nowStr，对当前字符到okeys中第一个字符之间的字符进行判断是在最终结果中加入
    当前字符还是舍弃。1.若中间这段字符串中有小于当前字符串的直接舍弃当前字符串，2.若有大于当前字符串且得放在okeys[0]之前(即在okeys[0]
    之后没有该字符串了)将当前字符串放入结果中，若所有字符都不符合1，2,若当前字符大于okeys[0]舍弃该字符，否则加入结果中
	"""
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
