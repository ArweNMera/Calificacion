class Calificacion:
    def __init__(self, calificacion_numerica):
        self.calificacion_numerica = calificacion_numerica
        self.calificacion_literal = ""

    def asignar_calificacion_literal(self):
        if self.calificacion_numerica > 9.0:
            self.calificacion_literal = "A Excelente"
        elif self.calificacion_numerica > 8.0:
            self.calificacion_literal = "B Muy bien"
        elif self.calificacion_numerica >= 7.5:
            self.calificacion_literal = "C Bien"
        else:
            self.calificacion_literal = "R Reprobado"

    def mostrar_calificacion(self):
        print(f"La calificación numérica es {self.calificacion_numerica}, que corresponde a: {self.calificacion_literal}")

# Ejemplo de uso:
calificacion_numerica = float(input("Ingresa la calificación numérica: "))

# Crear una instancia de la clase Calificacion
calificacion = Calificacion(calificacion_numerica)

# Asignar la calificación literal
calificacion.asignar_calificacion_literal()

# Mostrar la calificación literal correspondiente
calificacion.mostrar_calificacion()
