KHL=HKHL.html
wget https://www.hokejportal.cz/rusko/khl/vysledky/
mv index.html $KHL

CZE=HCZE.html
wget https://www.hokejportal.cz/cesko/extraliga/vysledky/
mv index.html $CZE

for i in $KHL $CZE
do
  echo "Evaluating " $i
  python3 hokejportal-filter.py < $i | python3 filter.py | python3 bets.py
  python3 hokejportal-filter.py < $i | python3 filter.py > $i.csv
done
