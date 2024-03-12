# gbm_challenge

1. Clonar el repositorio.
`git clone https://github.com/tu-usuario/nombre-del-proyecto.git`

2. Ir al directorio del proyecto.
`cd project-name`.

3. Instalar dependencias
`pip install -r requirements.txt`

**Ejericio 1:**
En la Carpeta "Ejercicio1", se encuentra la solución con el archivo "Ejercicio 1.ipynb", aquí se encuentra la función *valida_palindromo('Texto')* y con esta se hace la validación para cualquier texto de si la palabra ingresada es palíndromo o no.

**Ejercicio 2:**
En la Carpeta "Ejercicio2", se encuentra la solución con el archivo "Ejercicio 2.py", aquí se encuentra la función, para ejecutar el script basta con escribir en la terminal:
python3 Ejercicio2.py y escribir los números según sea el determinado caso.

**Ejercicio 3:**
En la Carpeta "Ejercicio3", se encuentra la solución con el archivo "Ejercicio 3.ipynb", aquí se encuentra la función *saltos_minimos(n,casos)* , para ejecutar se puede usar el siguiente ejemplo:
#n es el número de casos a evaluar
n = 5
#casos es la serie de números para generar los saltos
casos = [1, 2, 3, 4, 5]

**Ejercicio 4:**
En la Carpeta "Ejercicio4", se encuentra la solución con el archivo "Ejercicio 4.ipynb", aquí se encuentra una experimentación de modelos a partir de tensorflow.keras, con la base "data_customer_classification 1", se hace una definición de variable respuesta para con base en: 

condiciones = [
    (datos['tran_amount'] >= 0) & (datos['tran_amount'] < 40),
    (datos['tran_amount'] >= 40) & (datos['tran_amount'] < 80),
    (datos['tran_amount'] >= 80)
]
valores = ['low', 'medium', 'high']

Para finalmente entrenar y evaluar en un ejercicio de clasificación, el modelo con las variables (frecuencia de compra, hábito de gasto, máximo gasto)

## Contact:
- Jeisson Andres Castaño Aguirre
- Cel: 3164706869
- Mail: jeacastanoag@unal.edu.co
- Estadístico - Universidad Nacional de Colombia Sede Medellín
- Master of Business Administration (MBA) - Tecnológico de Monterrey
