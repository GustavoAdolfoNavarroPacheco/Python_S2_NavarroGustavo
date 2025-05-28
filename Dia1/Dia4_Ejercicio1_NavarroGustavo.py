# Menu Restaurante Custom Rappid
	
max=int(input('Ingrese la cantidad de hamburguesas que desea:'))
subtotal = 0
cajita = 0
while cajita!=max:
		print(" ")
		print('Selecciona el pan que deseas agregar a tu hamburguesa:')
		print('1.) Pan Centeno = $1.000')
		print('2.) Pan Avena = $1.500')
		pan=int(input())
		if pan==1:
			subtotal = subtotal+1000
			print("Seleccionaste Pan Centeno y llevas un Total de: $",subtotal)
		elif pan==2:
				subtotal = subtotal+1500
				print("Seleccionaste Pan Avena y llevas un Total de: $",subtotal)
				
		print(" ")
		print('Seleccione cuantos gramos de CARNE desea agregar:')
		print('1.) 250g = $5.000')
		print('2.) 300g = $7.000')
		carne=int(input())		
		if carne==1:
			subtotal = subtotal+5000
			print("Seleccionaste 250g de Carne y llevas un total de: $",subtotal)
		elif carne==2:
				subtotal = subtotal+7000
				print("Seleccionaste 300g de Carne y llevas un total de: $",subtotal)

		print(" ")
		print('Seleccione cuantos gramos de POLLO desea agregar:')
		print('1.) 250g = $4.500')
		print('2.) 350g = $5.500')
		pollo=int(input())	
		if pollo==1:
			subtotal = subtotal+4500
			print("Seleccionaste 250g de Pollo y llevas un total de: $",subtotal)
		elif pollo==2:
				subtotal = subtotal+5500
				print("Seleccionaste 350g de Pollo y llevas un total de: $",subtotal)
			
		print(" ")
		print('Seleccione cuantos gramos de POLLO DESMECHADO desea agregar:')
		print('1.) 250g = $6.500')
		print('2.) 350g = $7.500')
		polloDesmechado=int(input())
		if polloDesmechado==1:
			subtotal = subtotal+6500
			print("Seleccionaste 250g de Pollo Desmechado y llevas un total de: $",subtotal)
		elif polloDesmechado==2:
				subtotal = subtotal+7500
				print("Seleccionaste 350g de Pollo Desmechado y llevas un total de: $",subtotal)

		print(" ")
		print('Seleccione cuantas lonjas de TOCINETA desea agregar:')
		print('1.) 1 Lonja = $1.500')
		print('2.) 2 Lonjas = $2.500')
		tocineta=int(input())
		if tocineta==1:
			subtotal = subtotal+1500
			print("Seleccionaste 1 Lonjas de Tocineta y llevas un total de: $",subtotal)
		elif tocineta==2:
				subtotal = subtotal+2500
				print("Seleccionaste 2 Lonjas de Tocineta y llevas un total de: $",subtotal)

		print(" ")
		print('Seleccione que tipo de PAPA FRITA desea agregar:')
		print('1.) A la francesa = $5.000')
		print('2.) En cascos = $6.000')
		papaFrita=int(input())
		if papaFrita==1:
			subtotal = subtotal+5000
			print("Seleccionaste Papa Frita a la Francesa y llevas un total de: $",subtotal)
		elif papaFrita==2:
				subtotal = subtotal+6000
				print("Seleccionaste Papa Frita en Cascos y llevas un total de: $",subtotal)

		print(" ")
		print('Seleccione el tipo de BEBIDA que desea agregar:')
		print('1.) Gaseosa = $5.000')
		print('2.) Cerveza Club Colombia = $8.000')
		print('3.) Naranjada = $9.000')
		bebidas=int(input())
		if bebidas==1:
			subtotal = subtotal+5000
			print("Seleccionaste como Bebida: Gaseosa y llevas un total de: $",subtotal)
		elif bebidas==2:
				subtotal = subtotal+8000
				print("Seleccionaste como Bebida: Cerveza Club Colombia y llevas un total de: $",subtotal)
		elif bebidas==3:
					subtotal = subtotal+9000
					print("Seleccionaste como Bebida: Naranjada y llevas un total de: $",subtotal)

		cajita = cajita+1
	
costoDeServicio = subtotal*0.10
totalAPagar = subtotal+costoDeServicio
print(" ")
print("El total de Costo de Servicio es de: $",costoDeServicio)
print('El total a pagar es de: $',totalAPagar)

#Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969
