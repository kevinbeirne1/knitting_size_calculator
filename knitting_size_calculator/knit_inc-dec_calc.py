#! python 3

"""
knit_inc-dec_calc.py - Calculator to determine to figure out knit size change

Enter the starting stitches, the end stitches and/or the amount increase,
and the calculator returns how to achieve the size change required

>>> Enter your starting stitches: 60
>>> Do you want to enter final stitch count or change: final
>>> Enter your target: 73
To go from 60 stitches to 73 (adding 13 stitches) you need to:
(k4 m1)*8 (k5 m1 * 5)

>>> Enter your starting stitches: 60
>>> Do you want to enter final stitch count or change: change
>>> Enter your target: 13
To go from 60 stitches to 73 (adding 13 stitches) you need to:
(k4 m1)*8 (k5 m1 * 5)

"""

start_stitches = 60
final_stitches = 73

stitch_change = final_stitches - start_stitches
lower_inc_dec_interval = start_stiches//stitche_change
higher_inc_dec_interval = lower_inc_dec_interval + 1

inc_dec_intervals = [lower_inc_dec_interval, lower_inc_dec_interval + 1]


