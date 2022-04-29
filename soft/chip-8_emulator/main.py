"""
Programa principal.
"""
from cpu import Cpu

# ROM a cargar
ROM = "Games/bc_test.ch8"

# Instancia de la CPU
cpu = Cpu()

# Cargamos ROM
rom_bytes = open(ROM, "rb").read()
cpu.load_rom(rom_bytes)

# Arrancamos procesador
cpu.run()
