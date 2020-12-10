from lxml import html
from lxml import etree
import sys

tree = etree.parse(sys.stdin, etree.HTMLParser())
#tree = etree.parse("./pokus.html", etree.HTMLParser())
divs = tree.xpath('//div[@class="table__wrapper"]')
trs = divs[0].xpath('.//tr[@class != "head" or not(@class)]')
print("Div,Date,Time,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR,HS,AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR,B365H,B365D,B365A,BWH,BWD,BWA,IWH,IWD,IWA,PSH,PSD,PSA,WHH,WHD,WHA,VCH,VCD,VCA,MaxH,MaxD,MaxA,AvgH,AvgD,AvgA,B365>2.5,B365<2.5,P>2.5,P<2.5,Max>2.5,Max<2.5,Avg>2.5,Avg<2.5,AHh,B365AHH,B365AHA,PAHH,PAHA,MaxAHH,MaxAHA,AvgAHH,AvgAHA,B365CH,B365CD,B365CA,BWCH,BWCD,BWCA,IWCH,IWCD,IWCA,PSCH,PSCD,PSCA,WHCH,WHCD,WHCA,VCCH,VCCD,VCCA,MaxCH,MaxCD,MaxCA,AvgCH,AvgCD,AvgCA,B365C>2.5,B365C<2.5,PC>2.5,PC<2.5,MaxC>2.5,MaxC<2.5,AvgC>2.5,AvgC<2.5,AHCh,B365CAHH,B365CAHA,PCAHH,PCAHA,MaxCAHH,MaxCAHA,AvgCAHH,AvgCAHA")
for tr in trs:
  tds = tr.xpath('.//*/text()')
  tds = tds[1:] if len(tds) == 8 else tds # remove date which is eventually the first element
  tds = [''.join(filter(lambda x: x is ':' or str.isalnum(x),td)) for td in tds]
  print("HL,0/0/0,"+tds[0]+','+tds[1]+','+tds[5]+','+tds[3].split(':')[0]+','+''.join(filter(str.isnumeric,tds[3].split(':')[1])))
