*Things to keep in mind:
*percentage signs
*decimales
*headings

//  PRELIMINARES 
	clear all
	set more off
	set mem 32767
//===========================================================================//
//	CARGANDO BASE	
//	GLOBALS

	global data = "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Data"
	global latex = "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Latex"

	use "$data/sub_set_casen2017_v11.dta" , clear 
	
	ssc install   outtable
	
*===============================================================================
  *Parte 1 - Estadistica Descriptiva - Alpha*
*=============================================================================== 	
matrix K = J(24,8,.)
matrix colname K = "N" "Poblacion" "N_hombres" "Hombre" "N_mujeres" "Mujer" "Diferencia" "t-stat"
matrix rowname K = "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" "21" "22" "Total"

*Columna #1*********************************************************************
forval i = 1/23 {
sum yoprcor if esc == `i'-1
local N_`i' = `r(N)'
matrix K[`i',1]= `N_`i''
}

*Aqui el resumen de la data solo incluye las personas que tienen ingreso
*Si quisiera contar el total de personas en la muestra (incluyendo los que
*no tienen ingreso) se podria hacer ¨sum¨ a una variable sin datos faltantes
* (como region)

*Columna #2*********************************************************************
forval k = 1/23 {
sum yoprcor if esc == `k'-1
local Pob_`k' = `r(mean)'
matrix K[`k',2]= `Pob_`k''
}
*Columna #3*********************************************************************
forval i = 1/23 {
sum yoprcor if esc == `i'-1  & sexo == 1
local N_`i' = `r(N)'
matrix K[`i',3]= `N_`i''
}
*Columna #5*********************************************************************
forval i = 1/23 {
sum yoprcor if esc == `i'-1  & sexo == 2
local N_`i' = `r(N)'
matrix K[`i',5]= `N_`i''
}
*Columna #4*********************************************************************
forval i = 1/23 {
sum yoprcor if esc == `i'-1  & sexo == 1
local pobh_`i' = `r(mean)'
matrix K[`i',4]= `pobh_`i''
}
*Columna #6*********************************************************************
forval k = 1/23 {
sum yoprcor if esc == `k'-1  & sexo == 2
local Pobm_`k' = `r(mean)'
matrix K[`k',6]= `Pobm_`k''
}
*Columna #7*********************************************************************
forval i = 1/23 {
forval j = 1/2 {
sum yoprcor if esc == `i'-1  & sexo == `j'
local pobh_`i'_`j' = `r(mean)'
}
local dif_`i' = `pobh_`i'_1' - `pobh_`i'_2'
matrix K[`i',7] = `dif_`i''
}
*Columna #8*********************************************************************
forval i = 1/23 {
ttest yoprcor, by (sexo), if esc==`i'-1
local tst_`i'= `r(t)'
matrix K[`i',8]= `tst_`i''
}
*Ultima Fila********************************************************************
sum yoprcor
matrix K[24,1]=`r(N)'

sum yoprcor
matrix K[24,2]=`r(mean)'

sum region if sexo == 1
matrix K[24,3]=`r(N)'

sum yoprcor if sexo ==1
matrix K[24,4]=`r(mean)'

sum region if sexo == 2
matrix K[24,5]=`r(N)'

sum yoprcor if sexo ==2
matrix K[24,6]=`r(mean)'

ttest yoprcor, by (sexo)
matrix K[24,8]=`r(t)'

forval j= 1/2 {
sum yoprcor if sexo == `j'
local cashmoney_`j' = `r(mean)'
matrix K[24,7]= -(`cashmoney_2' - `cashmoney_1')
}

********************************************************************************
matrix li K

outtable  using "$latex/alpha"  ///
 , mat(K) caption( Ingreso por Genero ) center  ///
 replace  nobox   ///
 clabel(Alpha)  f(%9.1fc)
 
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
 *******************************************************************************
*==============================================================================
  *Parte 1 - Estadistica Descriptiva - Beta*
*=============================================================================== 
matrix L =J(8,3,.)
matrix colname L = "Total" "Prop_Hombre" "Prop_Mujeres"
matrix rowname L = "Cuenta_de_Ahorro" "Cuenta_Corriente" "Cuenta_Deposito_a_la_Vista" "Tarjet_de_Debito" "Tarjeta_Credito_Bancario" "Tarjeta_Credito_No_Bancaria" "Linea_de_Credito" "Total" 

*Columna #1*********************************************************************
local row=1
foreach j in y27a y27b y27c y27d y27e y27f y27g {
forval i =1/2 {
sum `j' if `j' ==1
matrix L[`row',1] = `r(N)'
}
local ++row
}

*Columna #2 y #3****************************************************************	
local row=1
foreach j in y27a y27b y27c y27d y27e y27f y27g {
forval i =1/2 {
sum `j' if `j' ==1 & sexo==`i'
local name = `r(N)'
sum `j' if `j' ==1
local gender = `r(N)'
matrix L[`row',`i'+1] =`name'/`gender'
}
local ++row
}

*Ultima Fila********************************************************************
matrix A = J(8,3,.)
local row=1
foreach j in y27a y27b y27c y27d y27e y27f y27g {
forval i =1/2 {
sum `j' if `j' ==1 & sexo==`i'
local name = `r(N)'
matrix A[`row',`i'+1] = `name'
}
local ++row
}
matrix li A

*Aqui sumamos la columna de primera matriz*
mata : st_matrix("M", colsum(st_matrix("L")))
matrix li M
*tamomos resultados de matriz M
matrix L[8,1] = 261505

*Aqui sumamos la columna #2 y #3*
mata : st_matrix("B", colsum(st_matrix("A")))
matrix li B
*tomamos resultados de matriz B
matrix L[8,2] = 124536/261505
matrix L[8,3] = 136969/261505

********************************************************************************
matrix li L

outtable  using "$latex/beta"  ///
 , mat(L) caption( Inclusion Financiera por Genero ) center ///
 replace  nobox   ///
 clabel(Beta)  f(%9.3fc) 

********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*===============================================================================
 *Parte 1 - Estadistica Descriptiva - Gamma*
*===============================================================================

*Tuve que acortar los rownames porque estaban demasiado largos*
matrix C = J(8,3,.)
matrix colname C = "Total" "Hombres" "Mujeres"
matrix rowname C = "AFP_-_Cotizacion_obligatoria" "AFP_-_Cotizacion_voluntaria_" "IPS_(ex_INP)" "Caja_de_Prevision_de_la_Defensa" "Direccion_Carabinero" "Otra" "No_esta_cotizando" "No_Sabe"

*Primera Coluna ****************************************************************
sum o29
*Vemos que total = 116974*

forval i = 1/8 {
sum o29 if o29 == `i'
local totales_`i' = `r(N)'
matrix C[`i',1] = (`totales_`i''/116974)*100
}

* Segunda Columna **************************************************************
sum o29 if sexo == 1
*Vemos que total = 60582

forval i = 1/8 {
sum  o29 if o29 == `i' & sexo == 1
local male_`i' = `r(N)'
matrix C[`i',2] = (`male_`i''/60582)*100
}

* Tercera Columna **************************************************************

sum o29 if sexo == 2
*Vemos que total = 56392

forval i = 1/8 {
sum  o29 if o29 == `i' & sexo == 2 
local female_`i' = `r(N)'
matrix C[`i',3] = (`female_`i''/56392)*100
}

********************************************************************************
*Hay que hacer fila 8 por seperado debido a que tiene el valor "9" en la encuesta"

sum o29 if o29 == 9
matrix C [8,1] = (`r(N)'/116974)*100

sum o29 if o29 == 9 & sexo == 1
matrix C [8,2] = (`r(N)'/60582)*100

sum o29 if o29 == 9 & sexo == 2
matrix C [8,3] = (`r(N)'/56392)*100

********************************************************************************
matrix li C, format ( %12.3f)

outtable  using "$latex/gamma"  ///
 , mat(C) caption( Porcentaje de Participacion por tipo de Cotizacion Previsional de la Poblacion Chilena seperado por grupo ) center  ///
 replace  nobox   ///
 clabel(Gamma)  f(%9.3fc)
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*===============================================================================
  *Parte 2 - Generacion de Variables - Nivel Principiante
*===============================================================================
*(1) Aqui se genero una variable aux que igual 1 para cada persona.
*Luego se sumo el total de esa nueva variable segun comuna

gen aux = 1
bys comuna : egen n_comuna = total(aux)

*(2) Primero se uso el comando pctile para dividir las personas en deciles.
*luego se uso delimt para crear nueva variable que contiene los 10 deciles

*No se pudo dividir en deciles con deciles iguales debido a que la distribucion
*de ingreso se acumula cerca a los numeros que terminan en 0000. Para tener
*deciles con la misma cantidad de gente, se tendria que arbitrariamente dividir
*entre grupos personas con el mismo nivel de ingreso

*Create dec1 containing the deciles of v
pctile decl = yoprcor, nq(10)

*Delimit
# delimit ;
recode yoprcor (0/144000 = 1 "Primer Decil de Ingreso")
			(144001/220000 = 2 "Segundo Decil de Ingreso")
			(220001/270000 = 3 "Tercero Decil de Ingreso")
			(270001/290000 = 4 "Cuarto Decil de Ingreso")
			(290001/320000 = 5 "Quinto Decil de Ingreso")
			(320001/400000 = 6 "Sexto Decil de Ingreso")
			(400001/480000 = 7 "Septimo Decil de Ingreso")
			(480001/600000 = 8 "Octavo Decil de Ingreso")
			(600001/950000 = 9 "Noveno Decil de Ingreso")
			(950001/max = 10 "Decimo Decil de Ingreso")
			,g(decil_de_ingreso) 
;
# delimit cr 


*(3) Primero, generamos la variable "Reg". Esta toma el valor 0 en todos los casos. 
*Segundo, definimos que tome el valor 1 si la region correspone a la region Metropolitana (13)
*Tercero, le damos los label que hacen que en vez del valor 1 y 0 aparece "Region Metropolitana"
* o "Region Diferente a la Metropolitana
*Cuarto, le damos el label "Encuestado en Region Metropolitana" a la variable para entender que
*explica la variable

gen Reg = 0
replace Reg = 1 if region == 13

label define Reg 1 "Region Metropolitana" 0 "Region Diferente a la Metropolitana"
label values Reg Reg

label variable Reg "Encuestado en Region Metropolitana"

*(3) Primero, generamos una variable "yoprcorz", la cual toma el valor 1 si el encuestado tiene
*ingreso mayor a 1000000 y desigual a ".". Ademas el encuestado debe ser mujer. 
*Segundo contamos la cantidad de personas que cumplen con estos requisitos separado por cada region

gen yoprcorz = 1 if yoprcor >= 1000000 & yoprcor != . & sexo == 2

bys region : egen numper = total(yoprcorz)


*===============================================================================
  *Parte 2 - Generacion de Variables - Nivel Experto
*===============================================================================


global data = "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Data"
global latex = "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Latex"

use "$data/base_productos_v11.dta" , clear 

*(1) Aqui se genero a varible prod_loss que igualo 0. Luego, reemplazamos  
*esta variable con 1 si sus ventas eran mayores a los costos
*

gen prod_loss =0

replace prod_loss =1 if ventas - costos < 0

*(2) Aqui se uso el comando egen para crear una nueva variable que pone 1 si
*por lo menos un producto no logro cubrir sus costos dentro del mismo periodo
*Este commando permite poner el maximum del prod_loss para cada producto que 
*corresponde por year y firma

egen y_prod_loss = max(prod_loss > 0), by(year firma)

*(3) Aqui se creo la variavle cumple_meta. Se puso cero a toda la variable.
*Luego, se puso 1 si las ventas son mayor o igual a la variable meta_ventas

gen cumple_meta = 0
replace cumple_meta = 1 if ventas >= meta_ventas

*(4) Este commando es muy parecido al comando del #2 de esa misma
*sección. Asigna el maximum de la variable comple_meta para todos que
*correspondan por year y firma.

egen cumple_meta_todos = max(cumple_meta > 0), by(year firma)

*(5) Este comando genera una variable que es el promodeio (mean) de la variable ventas
*separado por cada firma y ano
by firm year, sort: egen ventas_mean = mean(ventas)

*(6)Este comando genera una variable que es el promodeio (mean) de la variable costos
*separado por cada firma y ano
by firm year, sort: egen costos_mean = mean(costos)

*(7) Este comando genera una variable que demuestra los ingresos mas altos de un solo producto
*separado por cada firma y ano
by firm year, sort: egen prod_mas_vendido = max(ventas)

*===============================================================================
  *Parte 3 - Presentacion de Estimaciones *
*===============================================================================

*(1)
	
clear all
set more off

global data "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Data"
global latex "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Latex"

use "$data/base_present_resultados"

ssc instal outreg2

*Creamos una regresion lineal, explicando el leverage a traves de Tagibility, Market to Book Value,
*Log Sales y Profitability por Latino America y cada pais individualmente

reg leverage tang market_book ln_sales prof
estimates store LA

reg leverage tang market_book ln_sales prof if country == "Chile"
estimates store Chile

reg leverage tang market_book ln_sales prof if country == "Argentina"
estimates store Argentina

reg leverage tang market_book ln_sales prof if country == "Brazil"
estimates store Brazil

reg leverage tang market_book ln_sales prof if country == "Mexico"
estimates store Mexico

reg leverage tang market_book ln_sales prof if country == "Peru"
estimates store Peru

*Generamos una tabla mostrando todos los modelos creados anteriormente

outreg2 [ LA Chile Argentina Brazil Mexico Peru] using "$latex/tabla1.tex" ,label tex(frag) dec(3) adj bracket stats(coef tstat ) replace drop(leverage)
	

	
*(2)
clear all
set more off

global data "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Data"
global latex "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Latex"

use "$data/base_present_resultados"

label var age "Age"

*Creamos una regresion lineal, explicando el leverage a traves de Tagibility, Market to Book Value,
*Log Sales, Age y Profitability por Latino America y cada pais individualmente

reg leverage tang market_book ln_sales prof age
estimates store LA

reg leverage tang market_book ln_sales prof age if country == "Chile"
estimates store Chile

reg leverage tang market_book ln_sales prof age if country == "Argentina"
estimates store Argentina
	
reg leverage tang market_book ln_sales prof age if country == "Brazil"
estimates store Brazil
	
reg leverage tang market_book ln_sales prof age if country == "Mexico"
estimates store Mexico
	
reg leverage tang market_book ln_sales prof age if country == "Peru"
estimates store Peru

*Generamos una tabla mostrando todos los modelos creados anteriormente
	
outreg2 [ LA Chile Argentina Brazil Mexico Peru] using "$latex/tabla2.tex",label tex(frag) dec(3) adj bracket replace drop(leverage age) addtext(Control by Age, YES)
	
*(3)
clear all
set more off

global data "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Data"
global latex "C:\Users\andre\Desktop\Econometria Financiera\Tarea\My Stuff\Latex"

use "$data/base_present_resultados"
	
label var age "Age"

*Creamos una regresion lineal, explicando el leverage a traves de Tagibility, Market to Book Value,
*Log Sales, Age y Profitability por Latino America y cada pais individualmente
	
reg leverage tang market_book ln_sales prof age
estimates store LA

reg leverage tang market_book ln_sales prof age if country == "Chile"
estimates store Chile
	
reg leverage tang market_book ln_sales prof age if country == "Argentina"
estimates store Argentina
	
reg leverage tang market_book ln_sales prof age if country == "Brazil"
estimates store Brazil
	
reg leverage tang market_book ln_sales prof age if country == "Mexico"
estimates store Mexico
	
reg leverage tang market_book ln_sales prof age if country == "Peru"
estimates store Peru

*Generamos una tabla mostrando todos los modelos creados anteriormente, separandolos 
*en los segmentos "Performance" y "Assets"
	
outreg2 [ LA Chile Argentina Brazil Mexico Peru] using "$latex/tabla3.tex",label tex(frag) dec(3) adj bracket replace drop(leverage age) addtext(Control by Age, YES) groupvar(  "\textbf{Performance}"  ln_sales prof "\textbf{Assets}" tang market_book )
	 









 
