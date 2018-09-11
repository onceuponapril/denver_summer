menu=''
fl='7ELEVEN.F-37319592.txt'
with open(fl,'r') as file:
    for line in file:
        if 'DC40' in line:
            direct=line[35:39]
            mestyp=line[99:148].strip()
            credat=line[378:386]
            smdpor=line[148:157]
            sdnprt=line[158:160]
            sndprn=line[162:171]
            rcvpor=line[263:269]
            rcvprt=line[273:275]
            rcvprn=line[277:287]
            kydc='''DC40_DIRECT\t{}\nDC40_MESTYP\t{}\nDC40_CREDAT\t{}\nDC40_SMDPOR\t{}\nDC40_SDNPRT\t{}\nDC40_SNDPRN\t{}\nDC40_RCVPOR\t{}\nDC40_RCVPRT\t{}\nDC40_RCVPRN\t{}\n'''.format(direct,mestyp,credat,smdpor,sdnprt,sndprn,rcvpor,rcvprt,rcvprn)

            menu+=kydc

        if 'EDK01' in line:
            curcy=line[67:251].strip()
            vsart=line[252:290].strip()
            augru=line[290:293]
            ky01='EDK01_CURVY\t{}\nEDK01_VSART\t{}\nEDK01_AUGRU_BEZ\t{}\n'.format(curcy,vsart,augru)
            menu+=ky01


        if 'EDK14' in line:
            qualf=line[63:66]
            orgid=line[66:70]
            ky14='EDK14_QUALF\t{}\nEDK14_ORGID\t{}\n'.format(qualf,orgid)
            menu+=ky14

        if 'EDK02' in line:
            qualf=line[63:66]
            belnr=line[66:106].strip()
            datum=line[107:115]
            ky02='EDK02_QUALF\t{}\nEDK02_BELNR\t{}\nEDK02_DATUM\t{}\n'.format(qualf,belnr,datum)
            menu+=ky02

        if 'EDK03' in line:
            iddat=line[63:69]
            ky03='EDK03_IDDAT\t{}\n'.format(iddat)
            menu+=ky03
        if 'EDKA1' in line:
            parvw=line[63:65]
            name=line[205:211]
            ilnnr=line[936:939]
            kyA1='EDKA1_PARVW\t{}\nEDKA1_NAME4\t{}\nEDKA1_ILNNR\t{}\n'.format(parvw,name,ilnnr)
            menu+=kyA1

        if 'EDKT1' in line:
            tdid=line[63:67]
            tss=line[67:69]
            kyt1='EDKT1_TDID\t{}\nEDKT1_TSSPRAS\t{}\n'.format(tdid,tss)
            menu+=kyt1
        if 'EDKT2' in line:
            tdline=line[63:69].strip()
            tdformat=line[133:135]
            if tdline and tdformat:
                kyt2='EDKT2_TDLINE\t{}\nEDKT2_TDFORMAT.\t{}\n'.format(tdline,tdformat)
                menu+=kyt2
        if 'EDP01' in line:
            posex=line[63:74].strip()
            menge=line[74:89].strip()
            menee=line[89:91]
            kyedp='EDP01_POSEX\t{}\nEDP01_MENGE\t{}\nEDP01_MENEE\t{}\n'.format(posex,menge,menee)
            menu+=kyedp

        if 'EDP05' in line:
            alckz=line[63]
            kschl=line[66:176].strip()
            krate=line[176:183].strip()
            uprbs=line[191:200].strip()
            meaun=line[200:].strip()
            kyedp2='EDP05_ALCKZ\t{}\nEDP05_KSCHL\t{}\nEDP05_KRATE\t{}\nEDP05_UPRBS\t{}\nEDP05_MEAUN\t{}\n'.format(alckz,kschl,krate,uprbs,meaun)
            menu+=kyedp2
        if 'EDP19' in line:
            qualf=line[63:66]
            idtnr=line[66:].strip()
            ky19='EDP19_QUALF\t{}\nEDP19_IDTNR\t{}\n'.format(qualf,idtnr)
            menu+=ky19
        if 'EDPT1' in line:
            tdid=line[63:67]
            tss=line[67:69]
            kyt1='EDPT1_TDID\t{}\nEDPT1_TSSPRAS\t{}\n'.format(tdid,tss)
            menu+=kyt1
        if 'EDPT2' in line:
            tdline=line[63:133].strip()
            tdformat=line[133:].strip()
            kyPt2='EDPT2_TDLINE\t{}\nEDPT2_TDFORMAT\t{}\n'.format(tdline,tdformat)
            menu+=kyPt2

newfile=open('Newfile.txt','w')
newfile.write(menu)
newfile.close()




# >EDKT2	<TDLINE>	63,68	int	length=6,trim
# 	<TDFORMAT>	133，134
# EDP01	<POSEX>	63：64
# 	<MENGE> 	74，76
# 	<MENEE> 	89,90	string
# >EDP05 	<ALCKZ>	63		length=1
# 	<KSCHL>	66,175		trim
# 	<KRATE>	176,190	double	trim
# 	<UPRBS>	191
# 	 <MEAUN>	200,201
# EDP19	<QUALF>	63,65		length=3
# 	<IDTNR>	66,79
# EDPT1	<TDID>	63,66
# 	<TSSPRAS>	67,70
# >EDPT2	<TDLINE>	63,132		trim
# 	<TDFORMAT>	133,134
# rex = re.compile(r'''(?P<title>Longitude
#                            |QUALF
#                            |ORGID
#                          )
#                          \s*:?\s*
#                          (?P<value>.*)
#                          ''', re.VERBOSE)
#
#     root = ET.Element('root')
#     root.text = '\n'    # newline before the celldata element
#

#     with open('7ELEVEN.F-37319592.txt') as f:
#         celldata = ET.SubElement(root, 'celldata')
#         celldata.text = '\n'    # newline before the collected element
#         celldata.tail = '\n\n'  # empty line after the celldata element
#         for line in f:
#             # Empty line starts new celldata element (hack style, uggly)
#             if line.isspace():
#                 celldata = ET.SubElement(root, 'celldata')
#                 celldata.text = '\n'
#                 celldata.tail = '\n\n'
#
#             # If the line contains the wanted data, process it.
#             m = rex.search(line)
#             if m:
#                 # Fix some problems with the title as it will be used
#                 # as the tag name.
#                 title = m.group('title')
#                 title = title.replace('&', '')
#                 title = title.replace(' ', '')
#
#                 e = ET.SubElement(celldata, title.lower())
#                 e.text = m.group('value')
#                 e.tail = '\n'
#

#     # Display for debugging
#     ET.dump(root)

    # Include the root element to the tree and write the tree
    # to the file.

# tree = ET.ElementTree(root)
# tree.write('cell.xml', encoding='utf-8', xml_declaration=True)
