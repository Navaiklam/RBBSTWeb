#/bin/bash
sed 's/}/},/g' Bulk.json > 1.json
sed '$ s/.$//' 1.json > 2.json
sed '1 s/./[{/' 2.json > 3.json
sed '$ s/.$/}]/' 3.json > pathdomain.json
#cp Bulk.json pathdomain.json
mv pathdomain.json ../core_web/static/pathdomain.json
rm 1.json
rm 2.json
rm 3.json
rm Bulk.json
