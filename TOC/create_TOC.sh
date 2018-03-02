

head ../README.md > tmp
./gh-md-toc ../EVOP_Python_2018.md |  perl -pe 's/\(#/\(EVOP_Python_2018.md\/#/' >> tmp
mv tmp ../README.md
