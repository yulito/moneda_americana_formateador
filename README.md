# moneda_lib.py

### *Librería de uso personal para formatear monedas de países del continente Americano.*
---
**moneda_lib.py** permite formatear un valor entero, ejemplo 1: **1000000** en **CLP** nos devolvera un 
string **"$1.000.000,00"** o, ejemplo 2: si es en **USD** devolvera **"$1,000,000.00"**.

---

## Modo de uso:

1) Importamos la librería:
* **from moneda_lib import Moneda**

2) A traves del objeto **Moneda** invocamos la función **.moneda(parametro_1, parametro_2)**
   donde **parametro_1** es el valor entero (int) o decimal (float), mientras que **parametro_2**
   es el código de moneda al que queremos formatear. Es de tipo string (str)
* **Moneda.moneda(250000, "MXN")**

3) Si quieres saber todos los códigos de monedas que puedes usar, invocar el metodo:
* **Moneda.tipoMoneda()**
