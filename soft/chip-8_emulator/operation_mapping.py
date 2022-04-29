"""
Módulo que mapea las instrucciones de código máquina CHIP-8 a funciones
que emulan su comportamiento.
"""
import operations

def find_operation(opcode):
    opcodes_0 = {
        0x00E0: operations.clear_display,
        0x00EE: operations.return_from_function
    }
    if opcode.word in opcodes_0:
        return opcodes_0[opcode.word]

    opcodes = {
        0x1: operations.goto,
        0x2: operations.call_function,
        0x3: operations.skip_if_equal,
        0x4: operations.skip_if_not_equal,
        0x5: operations.skip_if_x_y_equal,
        0x6: operations.set_x,
        0x7: operations.add_to_x,
        0x9: operations.skip_if_x_y_not_equal,
        0xA: operations.set_i,
        0xB: operations.goto_plus,
        0xC: operations.generate_random,
        0xD: operations.draw_sprite
    }
    if opcode.a in opcodes:
        return opcodes[opcode.a]

    if opcode.a == 0x8:
        opcodes_8 = {
            0x0: operations.set_x_to_y,
            0x1: operations.bitwise_or,
            0x2: operations.bitwise_and,
            0x3: operations.bitwise_xor,
            0x4: operations.add_y_to_x,
            0x5: operations.take_y_from_x,
            0x6: operations.shift_x_right,
            0x7: operations.take_x_from_y,
            0xE: operations.shift_x_left
        }
        if opcode.n in opcodes_8:
            return opcodes_8[opcode.n]

    if opcode.a == 0xE:
        opcodes_e = {
            0x9E: operations.skip_if_key_pressed,
            0xA1: operations.skip_if_key_not_pressed
        }
        if opcode.nn in opcodes_e:
            return opcodes_e[opcode.nn]

    if opcode.a == 0xF:
        opcodes_f = {
            0x07: operations.set_x_to_delay_timer,
            0x0A: operations.wait_for_key_press,
            0x15: operations.set_delay_timer,
            0x18: operations.set_sound_timer,
            0x1E: operations.add_x_to_i,
            0x29: operations.load_character_address,
            0x33: operations.save_x_as_bcd,
            0x55: operations.save_registers_zero_to_x,
            0x65: operations.load_registers_zero_to_x
        }
        if opcode.nn in opcodes_f:
            return opcodes_f[opcode.nn]

    raise KeyError(f"La instrucción {word:#06x} no se encuentra entre las previstas")
