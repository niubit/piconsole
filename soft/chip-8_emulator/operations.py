"""
Módulo que define las funciones que emulan las instrucciones de código
máquina de CHIP-8.
"""
import random
import font

def add_to_x(opcode, cpu):
    cpu.reg_Vx[opcode.x] += opcode.nn
    cpu.reg_Vx[opcode.x] &= 0xFF # Restringimos a 8 bit

def add_x_to_i(opcode, cpu):
    cpu.clear_arithmetic_flag()
    original_value = cpu.reg_I
    result = cpu.reg_I + cpu.reg_Vx[opcode.x]
    result &= 0xFFFF  # Restringimos a 16 bit

    if result < original_value:
        cpu.set_arithmetic_flag()

    cpu.reg_I = result

def add_y_to_x(opcode, cpu):
    cpu.clear_arithmetic_flag()
    original_value = cpu.reg_Vx[opcode.x]
    result = cpu.reg_Vx[opcode.x] + cpu.reg_Vx[opcode.y]
    result &= 0xFF # Restringimos a 8 bit

    if result < original_value:
        cpu.set_arithmetic_flag()

    cpu.reg_Vx[opcode.x] = result

def take_x_from_y(opcode, cpu):
    cpu.set_arithmetic_flag()
    original_value = cpu.reg_Vx[opcode.x]
    result = cpu.reg_Vx[opcode.y] - cpu.reg_Vx[opcode.x]
    result &= 0xFF # Restringimos a 8 bit

    if result > original_value:
        cpu.clear_arithmetic_flag()

    cpu.reg_Vx[opcode.x] = result

def take_y_from_x(opcode, cpu):
    cpu.set_arithmetic_flag()
    original_value = cpu.reg_Vx[opcode.x]
    result = cpu.reg_Vx[opcode.x] - cpu.reg_Vx[opcode.y]
    result &= 0xFF # Restringimos a 8 bit

    if result > original_value:
        cpu.clear_arithmetic_flag()

    cpu.reg_Vx[opcode.x] = result

def bitwise_and(opcode, cpu):
    cpu.reg_Vx[opcode.x] = cpu.reg_Vx[opcode.x] & cpu.reg_Vx[opcode.y]

def bitwise_or(opcode, cpu):
    cpu.reg_Vx[opcode.x] = cpu.reg_Vx[opcode.x] | cpu.reg_Vx[opcode.y]

def bitwise_xor(opcode, cpu):
    cpu.reg_Vx[opcode.x] = cpu.reg_Vx[opcode.x] ^ cpu.reg_Vx[opcode.y]

def shift_x_left(opcode, cpu):
    most_significant_bit = (cpu.reg_Vx[opcode.x] >> 7)
    cpu.reg_Vx[cpu.ARITHMETIC_FLAG_REGISTER] = most_significant_bit
    cpu.reg_Vx[opcode.x] = (cpu.reg_Vx[opcode.x] << 1) & 0xFF    # Restringimos a 8 bit

def shift_x_right(opcode, cpu):
    least_significant_bit = cpu.reg_Vx[opcode.x] & 0x01
    cpu.reg_Vx[cpu.ARITHMETIC_FLAG_REGISTER] = least_significant_bit
    cpu.reg_Vx[opcode.x] = cpu.reg_Vx[opcode.x] >> 1

def clear_display(opcode, cpu):
    cpu.display.fill(0)

def draw_sprite(opcode, cpu):
    cpu.clear_arithmetic_flag()
    x = cpu.reg_Vx[opcode.x]
    y = cpu.reg_Vx[opcode.y]
    height = opcode.n

    for current_row_offset in range(height):
        row = y + current_row_offset
        new_pixels = cpu.ram[cpu.reg_I + current_row_offset]

        for x_offset in range(8):
            mask = 128 >> x_offset
            column = x + x_offset

            ssd_x = cpu.SCALE * column
            ssd_y = cpu.SCALE * row
            # Restringimos el pixel al tamaño de la pantalla
            if ssd_x >= cpu.DISPLAY_W or ssd_y >= cpu.DISPLAY_H:
                continue
            ssd_byte = cpu.display.buffer[(ssd_y // 8) * cpu.DISPLAY_W + ssd_x]
            ssd_mask = 1 << (ssd_y % 8)
            old_bit = bool(ssd_byte & ssd_mask)
            new_bit = bool(new_pixels & mask)
            bit_value = old_bit ^ new_bit
            cpu.display.fill_rect(ssd_x, ssd_y, cpu.SCALE, cpu.SCALE, bit_value)

            if old_bit and new_bit:
                cpu.set_arithmetic_flag()

def skip_if_key_not_pressed(opcode, cpu):
    key = cpu.reg_Vx[opcode.x]
    if key not in cpu.keys:
        cpu.move_to_next_instruction()

def skip_if_key_pressed(opcode, cpu):
    key = cpu.reg_Vx[opcode.x]
    if key in cpu.keys:
        cpu.move_to_next_instruction()

def wait_for_key_press(opcode, cpu):
    keys = cpu.last_keys - cpu.keys
    if not keys:
        cpu.move_to_previous_instruction()
    else:
        cpu.reg_Vx[opcode.x] = sorted(keys)[0]

def call_function(opcode, cpu):
    cpu.stack.append(cpu.reg_PC)
    cpu.reg_PC = opcode.nnn

def goto_plus(opcode, cpu):
    cpu.reg_PC = cpu.reg_Vx[0] + opcode.nnn
    cpu.reg_PC &= 0xFFFF  # Restringimos a 16 bit

def goto(opcode, cpu):
    cpu.reg_PC = opcode.nnn
    cpu.reg_PC &= 0xFFFF  # Restringimos a 16 bit

def return_from_function(opcode, cpu):
    address = cpu.stack.pop()
    cpu.reg_PC = address

def skip_if_equal(opcode, cpu):
    if(cpu.reg_Vx[opcode.x] == opcode.nn):
        cpu.move_to_next_instruction()

def skip_if_not_equal(opcode, cpu):
    if(cpu.reg_Vx[opcode.x] != opcode.nn):
        cpu.move_to_next_instruction()

def skip_if_x_y_equal(opcode, cpu):
    if(cpu.reg_Vx[opcode.x] == cpu.reg_Vx[opcode.y]):
        cpu.move_to_next_instruction()

def skip_if_x_y_not_equal(opcode, cpu):
    if(cpu.reg_Vx[opcode.x] != cpu.reg_Vx[opcode.y]):
        cpu.move_to_next_instruction()

def load_character_address(opcode, cpu):
    cpu.reg_I = cpu.reg_Vx[opcode.x] * font.CHAR_SIZE

def load_registers_zero_to_x(opcode, cpu):
    for i in range(opcode.x + 1):
        cpu.reg_Vx[i] = cpu.ram[cpu.reg_I + i]

def generate_random(opcode, cpu):
    random_int = random.randint(0, 255)
    cpu.reg_Vx[opcode.x] = opcode.nn & random_int

def save_registers_zero_to_x(opcode, cpu):
    for i in range(opcode.x + 1):
        cpu.ram[cpu.reg_I + i] = cpu.reg_Vx[i]

def save_x_as_bcd(opcode, cpu):
    value = cpu.reg_Vx[opcode.x]
    # Guardamos el dígito de la izquierda como un byte
    cpu.ram[cpu.reg_I] = int(value / 100) & 0xFF
    # Guardamos el dígito central como un byte
    cpu.ram[cpu.reg_I + 1] = int((value / 10) % 10) & 0xFF
    # Guardamos el dígito de la derecha como un byte
    cpu.ram[cpu.reg_I + 2] = int(value % 10) & 0xFF

def set_i(opcode, cpu):
    cpu.reg_I = opcode.nnn

def set_x_to_y(opcode, cpu):
    cpu.reg_Vx[opcode.x] = cpu.reg_Vx[opcode.y]

def set_x(opcode, cpu):
    cpu.reg_Vx[opcode.x] = opcode.nn

def set_delay_timer(opcode, cpu):
    cpu.delay_timer = cpu.reg_Vx[opcode.x]

def set_sound_timer(opcode, cpu):
    cpu.sound_timer = cpu.reg_Vx[opcode.x]

def set_x_to_delay_timer(opcode, cpu):
    cpu.reg_Vx[opcode.x] = cpu.delay_timer
