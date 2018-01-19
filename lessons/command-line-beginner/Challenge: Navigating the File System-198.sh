## 1. Introduction ##


pwd
ls -l

## 2. Moving Problematic Files to a Separate Folder ##

/home/dq$ mv forest_fires.cssv problematic/

## 3. Fixing File Extensions ##

/home/dq/problematic$ mv legislators legislators.csv

## 4. Consolidating Files ##


cd /home/dq/
mv nfl.csv problematic/nfl.csv
mv titanic_survival.csv problematic/titanic_survival.csv
mv problematic/ csv_datasets/

## 5. Restricting Permissions ##


cd /home/dq/csv_datasets
chmod 0740 nfl.csv
chmod 0740 titanic_survival.csv
chmod 0740 crime_rates.csv
chmod 0740 forest_fires.csv
chmod 0740 legislators.csv
ls -l