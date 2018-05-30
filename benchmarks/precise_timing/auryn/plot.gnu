 
plot '< aube -i output.0.spk -l 7' using (int($1/0.01+0.5)%700):2  w p pt 7 lc -1
