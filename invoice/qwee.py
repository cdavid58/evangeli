<<<<<<< HEAD


VALUES = [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]

def payment(_payment, price_product):
	_p = price_product
	pay = _payment
	result = []
	for i in VALUES:
		if pay >= i:
			pay -= i
			result.append(i)
	return f"Valores devuelto {result}"

_payment = 15000
product = 3000

print(payment(_payment, product))
=======


VALUES = [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]

def payment(_payment, price_product):
	_p = price_product
	pay = _payment
	result = []
	for i in VALUES:
		if pay >= i:
			pay -= i
			result.append(i)
	return f"Valores devuelto {result}"

_payment = 15000
product = 3000

print(payment(_payment, product))
>>>>>>> fcce1250637949c4253f5212ecfaac71d2f5683d
