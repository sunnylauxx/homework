import calendar
cal = calendar.TextCalendar()
cal.pryear(2012)

#b
cal = calendar.TextCalendar(3)
cal.pryear(2018)


#c
cal = calendar.TextCalendar(6)
cal.prmonth(2018,10)

#d
d = calendar.LocaleTextCalendar(6, "LATIN")
d.pryear(2012)