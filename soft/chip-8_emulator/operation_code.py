"""
Módulo que define la clase Opcode que parsea las instrucciones del código
máquina de CHIP-8. Toma los dos bytes de la instrucción y los descompone
en sus partes para facilitar la ejecución de las mismas.
"""

class Opcode:
    def __init__(self, word):
        """
        Argumentos:
            word: un valor de 2 byte/16 bit que representa un opcode.
        """

        # Limitamos la instrucción a 16 bit
        self.word = word & 0xFFFF

        # El tipo de instrucción se encuentra en los 4 primeros bits
        self.a = (word & 0xF000) >> 12

        # Leemos los datos de la instrucción en los tres tamaños posibles
        # de 12, 8 ó 4 bits
        self.nnn = word & 0x0FFF
        self.nn = word & 0x00FF
        self.n = word & 0x000F

        # Leemos el valor donde se suele encontrar la referencia al primer
        # registro
        self.x = (word & 0x0F00) >> 8

        # Leemos el valor donde se suele encontrar la referencia al segundo
        # registro
        self.y = (word & 0x00F0) >> 4
