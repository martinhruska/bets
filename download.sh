#! /bin/bash

echo $@
for i in $@
do
  rm $i.csv
  wget https://www.football-data.co.uk/mmz4281/2021/$i.csv
  # wget http://www.football-data.co.uk/mmz4281/1920/E0.csv http://www.football-data.co.uk/mmz4281/1920/E0.csv http://www.football-data.co.uk/mmz4281/1920/D1.csv http://www.football-data.co.uk/mmz4281/1920/I1.csv http://www.football-data.co.uk/mmz4281/1920/I2.csv http://www.football-data.co.uk/mmz4281/1920/SP1.csv
done
