def es_bisiesto(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return("Es bisiesto")
  else:
	  return("No es bisiesto")

print(es_bisiesto(2020));
