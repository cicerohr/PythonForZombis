# EP1 - Google Developer Day 2011 (adaptado)


def googlon(texto, letras, tipo):
    """Busca no texto Googlon a quantidade ou de preposições ou de verbos ou de verbos na 1ª pessoa

    :param texto: texto precisa já estar "splitado"
    :param letras: caracteres a buscar no texto
    :param tipo: 'preposicoes';  'verbos'; 'verbos1'
    :return: quantidade encontrada
    """
    lista = list()
    total = 0
    for i in range(len(texto)):
        if tipo == 'preposicoes':
            if texto[i][0] in letras and texto[i][-1] not in letras:
                lista.append(texto[i])
        elif (tipo == 'verbos' or tipo == 'verbos1') and len(texto[i]) == 7 and texto[i][-1] not in letras:
            if tipo == 'verbos1' and texto[i][0] not in letras:
                lista.append(texto[i])
            elif tipo == 'verbos':
                lista.append(texto[i])
        total = len(lista)
    return total


def googlon_2(texto, tipo):
    """Busca no texto Googlon a quantidade ou de preposições ou de verbos ou de verbos na 1ª pessoa

    :param texto: texto Googlon já "splitado"
    :param tipo: 'preposicoes';  'verbos'; 'verbos1'
    :return: quantidade encontrada
    """
    if tipo == 'preposicoes':
        return len(list(filter(lambda self: self[0] in zumbi and self[-1] not in zumbi, texto)))
    if tipo == 'verbos':
        return len(list(filter(lambda self: len(self) == 7 and self[-1] not in zumbi, texto)))
    if tipo == 'verbos1':
        return len(list(filter(lambda self: self[0] not in zumbi and len(self) == 7 and self[-1] not in zumbi, texto)))


def ordem(self):
    # lista = 'zmbtshjpnwlrcxkqvdgf'
    lista = list('zmbtshjpnwlrcxkqvdgf')
    # lista = ['z', 'm', 'b', 't', 's', 'h', 'j', 'p', 'n', 'w', 'l', 'r', 'c', 'x', 'k','q','v','d','g','f']
    return self in lista


txtA = '''cncdbm pjcjzct vdbbxdtw rfqsr mkt gvhkcsvw qcxr kmk pnhc zwwdsd pgjjhr
lxzscps lmbjjx lgh mdcqlbwx ppzpvfbv vdszkb njv nvmfhshh ztvkmv dfbnht xfpj nlbcwrvv
dcrzslrf wzb krdb zndtfmf fwwm vmqzmg cpcnpnww nkjk ncrmzr jfmcl hxr vcj wcptgbc
gvbfxtbv wcjlrs psjc lrljqdct ltjwn vmhp wnlmw rkvg rtm djsv rwjls ngc zcjjttpt kbg
tdjzcwj pmgtzlng zvtnbs svztn pctgq qnghqcch mclvp qdht cbk lvqckrl qmwknt cqw jfxzx
tkljpkfc mjhskxjh lfjvrhr whshcrk kvtgzpl gxglr mpqxtbzb zbrpktxj knhmmtks mhj xdlsm
wcc sbrkdjmh gpn vwddsdl mqfsrwt khhmfng qkkjgg qdr qlpt njq xlc jfhhv kgzsb lqncvrh
jgw xhjk krprtxf dtrsfb rwtzbhs qbvvz nqbh pdfqlsv hhrrx pvf mdvcfqkt bsb gcnkszfk
rkzlhbnx njfqrzxj gtvrwp cmgp qddg gqjjcbjw khlbtg cdswmbgb lmbfvsv nfhvn jbnplx gkh
dmp hmnf bzrznlh vqdmjdsb ktbcx fgvsxzp gmv xftg lxtf dcxsrkl tzwvbkfq tpvdrlf khzzw
srtfttv lmknq jvkwr bplzzpjw rgtrj gcmdfzdx ksptr jzdfqq xmtzz pkqxrsw gvwg fqppvgk hsc
hdj gthkq trxl gkhp rbr skxpc lbkw bbdqpvn llshm bhrfvh gjw zgnlpgwl pdhqn ttjtx vfb
djftp kkrr ptmnzqkg tmjlqw pcvpwjb ggd jntktdz vth wtsp mlfmddsn phn hrdqrds phbq
vkffrqvt zxljnd lqg blnw brxk skwkh vqbq dlbnhz xpbddsjw gscvghmj pxcpvkmm jsfpllns
kpmmgxb pljpvcn wknwbcq wthwv bdjxr wdc lqmtsnrn wbcjprr htldnxcn qwl fvjdqd cwmb bfjmw
chv blx xblfrb gjbbg njqw mkmnwtzv dgsxl tgtclv xxcfpp brzxg lbrnrsf pfcpt wmvjxdsw
jmstqwx zjcrkzm ndtbsqsh jqbcddqh ggvf kcr mfhllb lbbkssx gsrxcb rwtxljp cwkc xwxjhbc
pfcgz zbdbsq wzfsf gqhdfchv cgp kwvnrfm ptmzl bkjcm dpl rskfms mqdgvskt hbtjpvm swff
vjq dwlrgxtm kqzrlxz vmpdxkv bwfgzmjn zzrr mlsm kknhkq jhtxc gjvnj mcld vftnnd pgbkhc
kzzsbq xqbs hlkxtc xgj vttn zmnc kwhcrd bfjbs lxkmnzx pbmp lnt ztm fkzql bjgllxv
bghqpnl hphvdvl lwlqdh xldsnqds tsmrhhtm gnksf lzhr rqm jvcmkbxv nsx cxpplqbq jzrr tnt
wpfl lnkfqjt tplwbr hzrv mxqhpg xxzdlwzx cgrtr jbvqmb cmsqdjx qcrx ljxh jbnw lgf tzd
cltdd jtmdmt djbgqqk tgsffh hbff jjqn wtlsx qlmhxrrf sklfrc dwsk rgpgqz zhzvm brprszrc
hqlgx tdbsgf fkmrtn frskk qjvg jlhpgh rxrmqp nmc dxpx lljs kszjq hlxx nbkvsrf dggshkxz
nlvgr zldk tvphkg hlnls wlsxsvf mmksm lzgfnkmg tbw nrpzqfr gfc sxcdqtlt rmmhtmbp jkk
fdh jcw nwjjkrdq kztrcqxt lphf frs dcsbhwp tgnq lmq tpppxf vmd tnbqgv xxtlt ljdz hdslhv
dkzxctcn qsfctn tdsbdhv dxmkk ghfntj dckqls knlwvk mrddntg fwqwfxs tzqcvz sbnfjs kcxl
dsgnhsf kgj mfm vjmmf wptc rtb dtblv frp wwmngbk dxss txz fzlxll lbqjrp hhcxnnhn 
skhcwxw lllkssb dgwd lzq czhhtclr bpngkf krh bzccxd rqkr mdz phk dfctpgr gkt bdnfbh wlj
lfhkmb crbhzfs qzz jbmlsfkx htkmdbx mxjccgv fpj ttl jbw pmnt khqr jhztz dvmj kwchwcv
xggzgkln dxz fdsfsc cgpn pphslgf jxsd fsp spzzbc trvpx wjg nmdzgmnr qslm znngdwb zqwb
dcgxxcqm kcdwcpdm ngqzs sbst ltqxkt tjgmjzh nmmqnzfn ngsbphqb gsqfgjn jtwhxdx pqc jsfkd
ccx dfj wrgf kslnx zgqxqpvm rflzw jgl rsd fshm zlmtqs qfbrdg dknttlb xvqnd gtrpzhwb
ngwrbrfk skkfq bzfqkpjj rzp trzz fgmcd ptg wzg mdxlzvkg rfqdh lvwht vkvqhk pdnqm gwpcph
qbpsv vhxdj vxf tvpjwzb tjpdp frtvg xrqhp zjqcbxf fpbwbzb whnjkv dqfjwtv mjwrncd xvgkv
xrsrjv zdrfjwc lmbtkhch srwg lvq bvrjztfm vwmb rpxwnbrw cmvjrf cdxsgqgs mtrfm wrzct
pznlvfk cgcdvbpt cnpqtw sfwsnkkw qjlmkkmv wrsctd lwdbkws qhvszv jzzpb jlgz ftdqspbf
vvsvkq znktlpx vcvccs kswfwbzv hwfbd grplms dfvt pmmd nvb tgjpq hgsx qgsvbgws gzrq
kmbgdwm tgmwmsc lsmphpk pwpznr mhcskk bmzqtdx pgwd jplzc cbkgf zbmclc tzhqvbt wkq
hljqwkz vgclcmdx ggzb vsng tjw ckxtmqx wffrgzp wbht rsqb gqwxpncw mkszj mhlrmd pcl
jqjgd rdrphff ftzkqg dgrhmgn zgl plkxf hzdb mmj plphnnv jvvc tlthnhrh ngkgnln nfv rtxct
ppsp rcfxhhh mbzkdw smdlrm cstjtb rhhmzvp tqbs szbmqd gbn fjmt fcppm qdgqls gxltm
mdrgqdht vxpbxrdj twxcfxk qzj wtfh vglkdghk xtdzrz rjldhzld mbd fgrfb hffjd hcr
vghjwkvl pfkjshg rrflt zflwbn xffjdlfs bbzvs wdxmfr fvntg twjhgcc zwvwrnn gcnzl ftfpd
wfqxrnzf mbccsd szltzjm kpbslq wxxchz szzh tgq jxnng cmrgdh pdxjxpxr bslbmwm mdkc
nqjflf vsrp gbprtv mkfsfcwd zkf pqsq chbb bmt smtkrxjx nfkltv cvhxd zwwx bzqcnzwp wcpn
jmqkbclx'''.split()

txtB = '''pwbfdmtc jms gswg wvsscb ffq lbrhbn lcxc hcr thc mghts vkgfc nrvfgs dsrdq
tcmfz scqskgsl twgzh whts dqt twtksl lcrdlc dpzrl hwlqvc xcfstz rfkvbr bzmvqp qxrs
jlmwtcs nmjkkmpg kbcbg shdf qxpm qbm hlcnqnw jwhvvrtr kccw njxtbh hbtn lqmxbx krnn hcv
ptqtwp xgnfggb bjdd nfgkxsw kgzcf bgncx rbsfrrcf vjwsjpw jbtcbqm xhhg kfpqcpx bfxlg
qddzdv rvfqp hphjhns xhk npdd gsxm ffkbj gwdxkhr ddqmr jnzznp jzsgkb lcgsgjvh xvsbdw
klzsxz xpjkjxc gth dtrmkn qzcsksd vsdrhj vtlxg kdtxsj sgs chnz bdllcsdl trggnlpd gwbvj
stnhs vqbhj tdhps sgkk mxnswm ghm sqhfcnlk lpwqpn gcgg mjxh prmqclss zfn gplktxj
vkjnkkv fzzx vdslwsdk fxt pnbqqbk ksfgcvw hxfq xxd rvqzhmm ctvfgxzv nrzdkx nsxmr
bnvkmhcl srvc nczkp zbgsxg nmpx vrqq xfmnsjc zszmrfjv cbwjfldn fgn mzpp crjnct cmh cwh
cvdk cslq tvr gggck pfs thfdcpxt fcffvg bwxr bstbzwsx ghhq ldzzlkg zmfkxvms lfn
zzzfchrk lktdlrlx wzjcvj nbbkqjt lthk wnxsmnx dzftkjr fqfqcjtd dzsvqbnx zhprp cqlphsk
cjvrwg fkhr mxrg tdbxnwrg sdcptlln tjsh vbmd vlgfskcx xtkdp ttjcc qtlmgsh kbndtscg nfw
kctx rcltszw hbjr zld npqqm bpcqrhq szzw vbxj ghhmdq nhfptrsg vpkgwcd rkkxqk jhxpngr
qnkfd wvcsmb bgnvwqln gfbrqn rjjp dvfqjqsf rspxz cvrjxjq gtps fbg rdp pbzqnc nssd
rrpzcwp drfrgjx wvcpw fst frp lmz gbb brzbhlns qsjgzzzp jwvbhl pchqk vhpbdwd mwtlm
wbdxk rsfpxl kqt psr bcdktps mrgnflhr fvxsmsbx rqprpvj clnr hdqzjc bndwhjwp fbbkvdhr
mlgtjw ntk pxv nsnv jnwp vtksnpbb lpwl rslljk hsd rzfmdp xlbnkbw ptfhnlc jjc dpptqzc
jgrt jgxn bgg hslbhksz lhld jfdjq mmttm hwjbnqwv dcxggwhc dcnhhltm fttbf xjnjhgh
tchctgjn fvjkmj wkfxqzkx knbhrwgs xmszj smnrwmlv cdbdwsjf grtkzrwh rwmbvt zssswpc cdvr
klhtb bhkwfwxm bdjzlg nnw hnw fkm dzxpk fmvx kwfj vbf bgp frfbhk kvqwc skddwrtg
brgkfqnf xmwth wrmv rzmjrbfb pkj hckr sfbvz vtfbq fmzf tkhnb srd slkbcmj ppq kxgdbxhh
grwpg hxhjznc ttmgnwb lljfz ftkgv fsjmrvcx dljps mtgnc bkwfwfnj npfvr qlgpv hmqhxfpb
vvwtkrf nfchzb phmhxkck ngrngr lvd dgbwpk txlttnpb ppldgl wsmngb xtxsblgt xxtctgsj
pbvtkm pmcmrmvf phcxvpf wtbfv mvclz dvsl tmzxrrg gbjz dtlsp klmjxg fxh svtlgdl vvlhntpt
zgtkjdm lbjrnmt fbbhqvg dwqnsgj bjjcsvms tlpzlxj bcw rtvmzn kjtqpxhw zkvkdxz dcx zqmsnl
rvqw kgsh gbwdh wslrbz pfnpqh mgj kgmq hpzmp kpr jgz bksx lvsbxzv qgzf qcgpc pvf xlt
znjntxpj stgwsc vxgcfc cbvwhf tbxwpk nbjbkrz rgc wps rjlfpch bxqhw nckdtf bsncq
cnsmqxwn mzmlgpp vnxr qgjs vpkpbsn tgmw lbcxxgsf nnmr wbpdssgm nmddl zcbpcbpt twrkx
sdqxsnw lntr rzv hgjjksxf qpnnjwl hbcv fkwkbd ncv plr lmpfkk dpcj jzjbjgp bdttl
wrrdnmjz mxqxqdxc shztl gdzj rntpnh rjrlrfk rncp qlrhnww rdzhzx qnnxhm gtd lqklxr
gpgpqtrc hfhp hxl bnr fpvxzwmx pfrxglb xmchrvwx wbnxl vjxgbs vddhjkq wndwxs mqndvm
hvbncjw pbmlw hzjwqn nfgxqmb pfvnpwj xbwknvmr xtm cnxck qnmtrvx kmhj hdfrtd gqz srlml
ckx pwlhnpgf rkln tvq vjgrlfs vpvwnjtg wbswcvbh dzcjppjm slt zvxhgq xhcvvc rjd xhqdvhmp
nqlnsk hxmjpmnv sjwwc hbjvpw dpmdnz sxpb qznnxl nwnlmbx vdb hgkkwd znsxfqs kqwjtrcg
vhbnd rpgtkzz fmt nmzhrrqn qbqbvpsm kqwxr gvp xvrvsdf pxwt vkdns dpf jwnwz mxpwc xdvs
drrlpnr xvpztf pxzm jtg fvfgnzx qndpq dmzwnfgm jzknzgk clbpzcpd xhxsqp zbfck btzjd jwbt
gwtll kqj wlsdx sdvnw mqpvxk kjdkt frgwz mpqnqr lpj gvc hcdp zpvrdnc ckvmtbvf bddvc
mptrq xrzwj lzlbc pvgkrhd wlkdtjz pslzhzhc qmrr crkxcs jtxhfvr qzd fwrgdmjt cmg xvhcb
zmllbxs mxg plzxjqlk cwnf mqt hlsssh lvmptxcd zdbsvmll wshnn xzrz xsnhn jhg jtkqhh kcsb
bgsfnz mfxmqjn glzb qtwhllw nfkjfn xgw mvssxl hpb vjhlfgld cgfwq qdvjskx ntnhcl ckm
rqrsw dpff krrkl mcs xnk jpnx llw ljhqlbhs njdm gph nwmm bcclbzz wjfktwv mgthn kltqfx
hqntlps bdr dqtswd vqmkgkb pmznqzh mwgf nndtsx xfrmgqqj mvkfdhh qxp pvpcmx mhnhb slw
clvtxn nfpnlr tsssrk rnvdjpc ptkp hrwx zgblvhlj lqrdrz bhtlqhvv mlpkx jsl vlj kbmfjgs
ktzb wrnn ztbcph lxccgcxh bkrhjtsl cbmhp hwswwqg rnwqq srhnz fkvl kcnr qbxwpg hnss gjdn
rnxhwgd jgngwzc kfvg nwkjt rhjtsvv txk szkpmn nnzbqwgs pjjzqkvx bkw dfcbw rffn qph
kckksgp nzn tpqnm znzppsg tvcgnrb zgdsp tqlqrf vjqqxsp pwj pgft cvl cvr cnhgxsd lkd qlw
vwtbh mfxs gbgw'''.split()

zumbi = 'zmb'
print(' Versão 1 com "for" '.center(30, '-'))
print(f'A: {googlon(txtA, zumbi, "preposicoes")} preposições.')
print(f'B: {googlon(txtA, zumbi, "verbos")} verbos.')
print(f'C: {googlon(txtA, zumbi, "verbos1")} verbos na 1ª pessoa.')
print(' Versão 2 com "filter" '.center(30, '-'))
# print(help(googlon))
print(f'A: {googlon_2(txtA, "preposicoes")} preposições.')
print(f'B: {googlon_2(txtA, "verbos")} verbos.')
print(f'C: {googlon_2(txtA, "verbos1")} verbos na 1ª pessoa.')
print('-' * 30)
# help(googlon_2)

lexicografia = 'zmbtshjpnwlrcxkqvdgf'
lista_ordenada = []
for i in txtA:
    vocabulo = ''
    for c in i:
        vocabulo += chr(lexicografia.find(c) + 65)
    lista_ordenada.append(vocabulo)
print(sorted(list(set(lista_ordenada))))
lista_ordenada.sort()


lista_temp = []
for i in lista_ordenada:
    txt = ''
    for c in i:
        txt += lexicografia[ord(c) - 65]
    lista_temp.append(txt)
print(' '.join(lista_temp))
# print(sorted(txtA, key=ordem))
# print(ordem)
