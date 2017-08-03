
import urllib.request

url = "http://stock.gtimg.cn/data/hk_trend_cmp.php?time=1m&code1=hk00152&code2=hkHSI&var=hk_trend_cmp&_=1491458617142";
with urllib.request.urlopen(url) as response:
    html = response.read()

print(html);



