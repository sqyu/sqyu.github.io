for f in *.jemdoc; do python2 jemdoc.py $f; done
cd Travel
python3 template.py
for f in *.jemdoc; do python2 ../jemdoc.py $f; done
cd ..
