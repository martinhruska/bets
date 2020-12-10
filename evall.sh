#! /bin/bash

LGS=(I2 I1 SP1 SP2 E0 E1 D1 D2 F1 F2)
echo ${LGS[*]}
./download.sh ${LGS[*]}

for i in ${LGS[*]}
do
  echo "Evaluating " $i
  python3 filter.py < $i.csv | python3 bets.py
done
