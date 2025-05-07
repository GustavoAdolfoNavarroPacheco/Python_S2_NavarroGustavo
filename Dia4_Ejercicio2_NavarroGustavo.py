# Empresa ACME Nomina

print("Bienvenido a la web de la Empresa ACME")
print("Ingrese el n�mero de empleados a los cuales desea calcular la nomina:")
numeroEmpleados=int(input())

totalSueldoBruto = 0
totalSueldoNeto = 0
totalEPS = 0
totalPension = 0
sueldoNetoMaximo = -1
sueldoNetoMinimo = 999999999  
empleadoNetoMaximo = "" 
empleadoNetoMinimo = ""  
limiteMax = 1

for limiteMax  in range(numeroEmpleados,1):
		print("Ingrese el nombre del empleado ",limiteMax)
        nombreEmpleado = input("write something")
		Escribir " "
		Escribir "=============================================="
        Escribir " Ingrese las horas trabajadas por el empleado                    " nombreEmpleado
		Escribir " "
		Escribir "=============================================="
        Leer horasTrabajadasEmpleado
		Escribir " "
		Escribir "=============================================="
		
        sueldoBruto <- horasTrabajadasEmpleado * 20000
        descuentoEPS <- sueldoBruto * 0.04  
        descuentoPension <- sueldoBruto * 0.04  
        sueldoNeto <- sueldoBruto - (descuentoEPS + descuentoPension)
        totalSueldoBruto <- totalSueldoBruto + sueldoBruto
        totalSueldoNeto <- totalSueldoNeto + sueldoNeto
        totalEPS <- totalEPS + descuentoEPS
        totalPension <- totalPension + descuentoPension
		
        Si sueldoNeto > sueldoNetoMaximo Entonces
            sueldoNetoMaximo <- sueldoNeto
            empleadoNetoMaximo <- nombreEmpleado
        FinSi
		
        Si sueldoNeto < sueldoNetoMinimo Entonces
            sueldoNetoMinimo <- sueldoNeto
            empleadoNetoMinimo <- nombreEmpleado
        FinSi
		
        Escribir "                 El Empleado: "
		Escribir "                   ",nombreEmpleado
		Escribir " "
		Escribir "=============================================="
        Escribir "              Sueldo Bruto: ", sueldoBruto
        Escribir "             Descuento EPS: ", descuentoEPS
        Escribir "         Descuento Pensi�n: ", descuentoPension
        Escribir "               Sueldo Neto: ", sueldoNeto
		Escribir " "
		Escribir "============================================================================================"
    FinPara
	
    promedioBruto <- totalSueldoBruto / numeroEmpleados
    promedioNeto <- totalSueldoNeto / numeroEmpleados
	
	Escribir "        Total Sueldos Brutos: ", totalSueldoBruto
    Escribir "         Total Sueldos Netos: ", totalSueldoNeto
    Escribir "        Total Descuentos EPS: ", totalEPS
    Escribir "    Total Descuentos PENSION: ", totalPension
	Escribir " "
	Escribir "=============================================="
    Escribir "           Empleado que MAS GANA: "
	Escribir "                  ",empleadoNetoMaximo
	Escribir "             Total Sueldo NETO: "
	Escribir "                  ", sueldoNetoMaximo
	Escribir " "
	Escribir "=============================================="
	Escribir "           Empleado que MENOS GANA: "
	Escribir "                  ",empleadoNetoMinimo
	Escribir "             Total Sueldo NETO: "
	Escribir "                  ", sueldoNetoMinimo
	Escribir " "
	Escribir "=============================================="
	Escribir "           Promedio Sueldo Bruto: "
	Escribir "                  ",promedioBruto
    Escribir "           Promedio Sueldo Neto: "
	Escribir "                  ",promedioNeto
	Escribir " "
	Escribir "============================================================================================"