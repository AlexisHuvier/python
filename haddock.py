from requests import get
from json import loads


req = get("http://data.hugoland.fr/haddock.php/?method=json").text
req = loads(req)
print(req['resultat'])
