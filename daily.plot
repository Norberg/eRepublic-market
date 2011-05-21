#!/usr/bin/env gnuplot
set title "Temperature"
set xlabel "Datetime"
set ylabel "Celcius"

set terminal png
set output "~/www/erepublik/daily.png"
set datafile separator "|"
set style data lines
set grid
set xdata time
set timefmt x "%Y-%m-%d %H:%M"
set format x "%H:%M"
plot "< sqlite3 market.db \"SELECT datetime, price from market where datetime > datetime('now','-1 days', 'localtime') and item = '7';\"" using 1:2 title "outdoor"
