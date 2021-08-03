def calculate_total(ppostf):
    operadores = ["*", "/", "", "+", "-", "(", ")"]
    i = 0
    r = 0
    j = 0
    pila = []
    for j in ppostf:
        if j in operadores:
            n1 = float(pila[len(pila) - 2])
            n2 = float(pila[len(pila) - 1])
 
            if j == "+":
                r = n1 + n2
 
            if j == "-":
                r = n1 - n2
 
            if j == "*":
                r = n1 * n2
 
            if j == "/":
                r = n1 / n2
 
            if j == "**":
                r = n1 ** n2
 
            pila[len(pila) - 2] = r
            pila.pop(len(pila) - 1)
        else:
            pila.append(j)
 
        i = i + 1
 
    return pila
 
 
def apilar(pcar, ppila, ppostfijo):
    # * Prioridades de la expresion Infija y de la pila***
    prioridad_infija = {"*": 4, "": 2, "/": 2, "+": 1, "-": 1, "(": 5, ")": "NA"}
    prioridad_pila = {"*": 3, "": 2, "/": 2, "+": 1, "-": 1, "(": 0, ")": "NA"}
 
    # Verificarsi la pila esta vacia
    if len(ppila) == 0:
        ppila.append(pcar)
        return ppila
 
    if pcar == "(":
        ppila.append(pcar)
        return ppostfijo
 
    # Sacar todos los operadores de la pila hasta encontrar el parentesis ( que abre
    if pcar == ")":
        indice = - 1
        k= 0
        i = 0
        for k in ppila:
            ppostfijo.append(ppila[indice])
            ppila.pop(indice)
            indice = -1
            if ppila[indice] == "(":
                ppila.pop(indice)
                break
        return ppostfijo
    #--------------------------------------------------------------------------------------------------
    # ***Buscar valor del caracter leido en prioridad_infija
    valor_infija = prioridad_infija[pcar]
 
    # ***Buscar valor del ultimo operador en prioridad_pila
    car_pila = ppila[-1]
    valor_pila = prioridad_pila[car_pila]
 
    # Si valor de infija = al valor de la pila sacamos el operador
    # anterior de la pila y lo colocamos en postfijo
    if valor_infija == valor_pila:
        if car_pila != "(":
            ppostfijo.append(car_pila)
        ppila.pop(- 1)
        ppila.append(pcar)
        return ppostfijo
    #--------------------------------------------------------------------------------------------------
    if valor_infija > valor_pila:
        ppila.append(pcar)
        return ppostfijo
 
    # si valor_pila > valor_infija sacar de la pila todos los operadores de mayor precendencia y
    # luego introducir el valor de la infija en la pilai
    indice = - 1
    while valor_pila > valor_infija:
        ppostfijo.append(ppila[indice])
        ppila.pop()
        if ppila == []:
            break
        indice = - 1
        if len(ppila) > 0:
            car_pila = ppila[indice]
            valor_pila = prioridad_pila[car_pila]
    ppila.append(pcar)
    return ppostfijo
# ******************
def formar_postfijo(pexpinfija):
 
    operadores = ["*", "/", "", "+", "-", "(", ")"]
    exp_postfija = []
    pila = []
    for i in pexpinfija:
 
        if i in operadores:
            apilar(i, pila, exp_postfija)
        else:
            exp_postfija.append(i)
 
    # Si la pila aun tiene elementos
    z = -1
    for ii in pila:
        exp_postfija.append(pila[z])
        #pila.pop(z)
        z = z - 1
    return exp_postfija
# *****************
def basico(pexpinf):
    exp_infija = []
    cad = ""
    indice = 0
 
    for i in pexpinf:
 
        if i.isdigit():
            cad = cad + i
            anterior = i
            # Verifica la posibilidad : 1 + (3 + 4) 12 lo transforma en  1 + (3 + 4) * 12
            if indice > 0 and indice <= len(pexpinf) - 2 and pexpinf[indice-1] == ")":
                exp_infija.append("*")
        else:
            # si la cadena tiene alamcenado numeros
            if cad != "":
                exp_infija.append(cad)
                cad = ""
                # Verifica la posibilidad : 1 + 2 (3 + 4)  lo transforma en 1 + 2 * (3 + 4)
                if i == "(" and indice > 0 and indice <= len(pexpinf) - 2 and anterior != '':
                    exp_infija.append("*")
                    anterior = ''
 
                if i == "*" and indice <= len(pexpinf) - 2:
                    if pexpinf[indice + 1] == "*":
                        exp_infija.append("**")
                    elif pexpinf[indice - 1] != "*":
                        exp_infija.append(i)
                else:
                    exp_infija.append(i)
 
            else:
                if i == "*":
                    if exp_infija[-1] != "**":
                        exp_infija.append(i)
                else:
                    exp_infija.append(i)
        indice = indice + 1
 
    # Si finalizo el for y aun tiene car en cad
    if cad != ' ' and cad != '':
        exp_infija.append(cad)
    return exp_infija
 
# ******************
#expinfija = "3*4/(3+1)"
#expinfija = "4(5+6-8)"
#expinfija = "2 * 300 + (4500 + 50000) 10"
expinfija = "24 * (150 + 6000 - (81/20**3)-789) - 100 (5+1) 25"
infija = basico(expinfija.replace(' ', ''))
print("Infija :", infija)
# ----------------------------------------
postfijo = formar_postfijo(infija)
print("Post Fijo :", postfijo)
# #----------------------------------------
TOTAL = calculate_total(postfijo)
# if len(TOTAL) > 1:
#     TOTAL.pop()
print("Resultado :", TOTAL)