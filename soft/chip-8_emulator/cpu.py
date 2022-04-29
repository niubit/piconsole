"""
Módulo que define la clase Cpu que emula procesador, memoria y entradas/salidas
(pantalla, teclas y sonido) de CHIP-8.
Consultar la especificación de CHIP-8 en: https://es.wikipedia.org/wiki/CHIP-8
"""
from operation_code import Opcode
from operation_mapping import find_operation
import font
from machine import Pin, SPI, PWM
import ssd1306
import time

class Cpu:
    # La RAM empieza en la dirección 0x200 / 512
    PROGRAM_START_ADDRESS = const(0x200)
    # Dirección de memoria donde se carga el juego de caracteres
    FONT_OFFSET = const(0x0)
    # CHIP-8 trabaja con instrucciones de código máquina de 16 bit/2 byte
    WORD_SIZE = const(2)
    # V[15/0xF] se usa como flag de acarreo en ciertas instrucciones
    ARITHMETIC_FLAG_REGISTER = const(0xF)
    # Frecuencia del sonido
    SOUND_FREQ = const(500)

    # Parámetros de la pantalla de PiConsole
    SCALE = const(2)
    DISPLAY_W = const(128)
    DISPLAY_H = const(64)
    CONTRAST = const(0x7F)

    def __init__(self):
        self.ram = [0] * 4096                               # 4KB RAM
        self.reg_PC = self.PROGRAM_START_ADDRESS            # Program Counter

        self.reg_I = 0                                      # Registro I
        self.reg_Vx = [0] * 16                              # Registros Vx

        self.delay_timer = 0                                # Delay timer
        self.sound_timer = 0                                # Sound timer

        self.stack = []                                     # Pila de llamadas
        self.stack_pointer = 0                              # Puntero de pila

        # Teclas
        self.key_map = {
            0x0: Pin(7, Pin.IN, Pin.PULL_UP),               # B
            0x1: None,
            0x2: Pin(15, Pin.IN, Pin.PULL_UP),              # Arriba
            0x3: None,
            0x4: Pin(13, Pin.IN, Pin.PULL_UP),              # Izquierda
            0x5: Pin(11, Pin.IN, Pin.PULL_UP),              # A
            0x6: Pin(12, Pin.IN, Pin.PULL_UP),              # Derecha
            0x7: None,
            0x8: Pin(14, Pin.IN, Pin.PULL_UP),              # Abajo
            0x9: None,
            0xA: None,
            0xB: None,
            0xC: None,
            0xD: None,
            0xE: None,
            0xF: None
        }
        self.keys = set()                   # Teclas pulsadas
        self.last_keys = set()              # Teclas pulsadas en ciclo anterior

        # Carga juego caracteres en RAM
        offset = FONT_OFFSET
        for item in font.DATA:
            self.ram[offset] = item
            offset += 1

        # SSD1306
        spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
        self.display = ssd1306.SSD1306_SPI(DISPLAY_W, DISPLAY_H, spi, Pin(16), Pin(20), Pin(17), contrast=CONTRAST)

        # Buzzer
        self.buzzer = PWM(Pin(10))
        self.buzzer.freq(SOUND_FREQ)
        self.buzzer.deinit()

    # Avanza a la siguiente instrucción
    def move_to_next_instruction(self):
        self.reg_PC += Cpu.WORD_SIZE

    # Retrocede a la instrucción anterior
    def move_to_previous_instruction(self):
        self.reg_PC -= Cpu.WORD_SIZE

    # Carga una ROM en la memoria
    def load_rom(self, rom_bytes):
        for i, byte_value in enumerate(rom_bytes):
            self.ram[Cpu.PROGRAM_START_ADDRESS + i] = byte_value

    # Activa el flag de acarreo
    def set_arithmetic_flag(self):
        self.reg_Vx[self.ARITHMETIC_FLAG_REGISTER] = 1

    # Borra el flag de acarreo
    def clear_arithmetic_flag(self):
        self.reg_Vx[self.ARITHMETIC_FLAG_REGISTER] = 0

    # Ejecuta una instrucción de código máquina
    def emulate_cycle(self):
        current_word = self.fetch_word()

        opcode = Opcode(current_word)
        current_operation = find_operation(opcode)

        self.move_to_next_instruction()
        current_operation(opcode, self)

    # Carga de RAM la instrucción apuntada por el Program Counter
    def fetch_word(self):
        return self.ram[self.reg_PC] << 8 | self.ram[self.reg_PC + 1]

    # Actualiza los timers y gestiona el sonido
    def update_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
            self.buzzer.duty_u16(32768)
        else:
            self.buzzer.deinit()

    # Registra la pulsación de teclas
    def handle_input(self):
        for key, pin in self.key_map.items():
            if pin:
                if pin.value():
                    self.keys.discard(key)
                else:
                    self.keys.add(key)

    # Proceso de instrucciones
    def run(self):
        self.display.fill(0)

        # Contadores de tiempo para sincronizar reloj procesador y pantalla
        last_ticks_op = time.ticks_us()
        last_ticks_sc = last_ticks_op

        # Bucle principal
        while True:
            self.handle_input()
            self.emulate_cycle()
            self.last_keys = self.keys.copy()
            self.update_timers()

            # La frecuencia más recomendable para CHIP-8 es de 500 hz => Cada
            # iteración del bucle debería durar 2000 ms
            current_ticks = time.ticks_us()
            leftover_ticks = 2000 - time.ticks_diff(current_ticks, last_ticks_op)
            if leftover_ticks > 0:
                time.sleep_us(leftover_ticks)
                current_ticks += leftover_ticks
            last_ticks_op = current_ticks

            # Refrescamos la pantalla a 60FPS => Sólo refrescamos cada 16667 ms
            if time.ticks_diff(current_ticks, last_ticks_sc) > 16667:
                self.display.show()
                last_ticks_sc = current_ticks
