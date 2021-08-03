"""
Teniendo un arreglo en una estructura Json, según muestra la figura. Calcule y
muestre el total por ""ciudad"" para cada "mes".
"""
datos = [{"ciudad":"Medellin","almacen":"La 30","mes":"Enero","venta":1000},
       {"ciudad":"Medellin","almacen":"La 30","mes":"Febrero","venta":800},
       {"ciudad":"Medellin","almacen":"Los alpes","mes":"Enero","venta":1200},
       {"ciudad":"Medellin","almacen":"Los alpes","mes":"Febrero","venta":1000},
       {"ciudad":"Medellin","almacen":"Los alpes","mes":"Marzo","venta":2000},
       {"ciudad":"Cali","almacen":"La 30","mes":"Enero","venta":500},
       {"ciudad":"Cali","almacen":"La 30","mes":"Febrero","venta":400},
       {"ciudad":"Cali","almacen":"Los alpes","mes":"Enero","venta":800},
       {"ciudad":"Cali","almacen":"Los alpes","mes":"Febrero","venta":700},
       {"ciudad":"Cali","almacen":"Los alpes","mes":"Marzo","venta":600}]

enero = list(filter(lambda enero: enero["mes"] == "Enero", datos)) 
enero_medellin = list(filter(lambda medellin: medellin["ciudad"] == "Medellin", enero)) 
enero_cali=list(filter(lambda cali: cali["ciudad"] == "Cali", enero)) 


febrero = list(filter(lambda febrero: febrero["mes"]=="Febrero", datos)) 
febrero_medellin = list(filter(lambda medellin: medellin["ciudad"] == "Medellin", febrero)) 
febrero_cali = list(filter(lambda cali: cali["ciudad"]=="Cali", febrero)) 

marzo = list(filter(lambda marzo: marzo["mes"]=="Marzo", datos)) 
marzo_medellin = list(filter(lambda medellin: medellin["ciudad"] == "Medellin", marzo)) 
marzo_cali = list(filter(lambda cali: cali["ciudad"]=="Cali", marzo)) 

print("---TOTAL VENTAS POR CIUDAD----")
print("Medellin (Enero): ",sum([item["venta"] for item in enero_medellin]))
print("Medellin (Febrero): ",sum([item["venta"] for item in febrero_medellin]))
print("Medellin (Marzo): ",sum([item["venta"] for item in marzo_medellin]))

print("Cali (Enero): ",sum([item["venta"] for item in enero_cali]))
print("Cali (Febrero): ",sum([item["venta"] for item in febrero_cali]))
print("Cali (Marzo): ",sum([item["venta"] for item in marzo_cali]))


