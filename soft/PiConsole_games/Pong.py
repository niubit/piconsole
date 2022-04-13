# Juego Pong con la API Thumby y controlado con potenciómetro
import thumby
import machine
import utime
import random

# Constantes
HALF_WIDTH = int(thumby.DISPLAY_W / 2)  # Media anchura de pantalla
HALF_HEIGHT = int(thumby.DISPLAY_H / 2) # Media altura de pantalla
BALL_SIZE = 3                           # Tamaño de la bola
PAD_WIDTH = 2                           # Anchura de los bates
PAD_HEIGHT = 8                          # Altura de los bates
HALF_PAD_HEIGHT = int(PAD_HEIGHT / 2)   # Media altura de los bates
POT_MIN = 20000                         # Valor del potenciómetro asociado a la posición superior del bate en pantalla
POT_MAX = 63000                         # Valor del potenciómetro asociado a la posición inferior del bate en pantalla
LOOP_DELAY = 20                         # Retraso en milisegundos en cada bucle. Controla velocidad del juego

# Sonido de comienzo de juego
def play_startup_sound():
    thumby.audio.playBlocking(600, 250, 1000)
    thumby.audio.playBlocking(800, 250, 1000)
    thumby.audio.playBlocking(1200, 250, 1000)

# Sonido de rebote
def play_bounce_sound():
    thumby.audio.play(900, 250, 1000)

# Sonido de punto
def play_score_sound():
    thumby.audio.playBlocking(600, 250, 1000)
    thumby.audio.playBlocking(800, 250, 1000)

# Toma el valor 'value' perteneciente al rango [istart, iend] y calcula el valor proporcional
# dentro del nuevo rango [ostart, oend]
def valmap(value, istart, iend, ostart, oend):
    return int(ostart + (oend - ostart) * ((value - istart) / (iend - istart)))

# Dibuja el bate
def draw_paddle(paddle_no, paddle_center):
    if paddle_no == 1:
         x = 0
    else:
         x = thumby.DISPLAY_W - PAD_WIDTH
    y = paddle_center - HALF_PAD_HEIGHT
    thumby.display.fillRect(x, y, PAD_WIDTH, PAD_HEIGHT)

# Dibuja la bola
def draw_ball(x, y):
    thumby.display.fillRect(x, y, BALL_SIZE, BALL_SIZE)

# Variables globales
# Los dos bates los controlamos con el potenciómetro de PiConsole conectado a ADC1
pot_pin_l = machine.ADC(1)
pot_pin_r = machine.ADC(1)
# Puntuaciones
l_score = 0
r_score = 0
# Posición de la bola (inicialmente en el centro de la pantalla)
ball_x = HALF_WIDTH
ball_y = HALF_HEIGHT
# Dirección de la bola (inicialmente hacia abajo a la derecha)
ball_x_dir = 1
ball_y_dir = 1

play_startup_sound()

# Bucle principal
while True:
    # Lee los potenciómetros de los mandos
    pot_val_l = pot_pin_l.read_u16()
    pot_val_r = pot_pin_r.read_u16()

    # Escala los valores leídos del potenciómetro a la altura de la pantalla donde dibujar los bates
    paddle_l = valmap(pot_val_l, POT_MIN, POT_MAX, HALF_PAD_HEIGHT, thumby.DISPLAY_H - HALF_PAD_HEIGHT - 2)
    paddle_r = valmap(pot_val_r, POT_MIN, POT_MAX, HALF_PAD_HEIGHT, thumby.DISPLAY_H - HALF_PAD_HEIGHT - 2)

    # Calcula la nueva posición de la bola
    ball_x = ball_x + ball_x_dir
    ball_y = ball_y + ball_y_dir

    # Calcula los rebotes en la parte superior e inferior de la pantalla
    if ball_y < 0:
        ball_y_dir = 1
        #play_bounce_sound()
    if ball_y > thumby.DISPLAY_H - BALL_SIZE:
        ball_y_dir = -1
        #play_bounce_sound()

    # Control del rebote en la pared izquierda
    if ball_x < PAD_WIDTH:
        top_paddle = paddle_l - HALF_PAD_HEIGHT
        bottom_paddle = paddle_l + HALF_PAD_HEIGHT
        if ball_y > top_paddle - BALL_SIZE and ball_y < bottom_paddle:
            # La bola rebota en el bate izquierdo
            play_bounce_sound()
            ball_x_dir = 1
            ball_x = PAD_WIDTH
        else:
            # Punto para el jugador derecho
            play_score_sound()
            r_score += 1
            ball_x = HALF_WIDTH
            ball_y = HALF_HEIGHT
            ball_x_dir = random.randint(0, 1)
            if ball_x_dir == 0:
                ball_x_dir = -1
            ball_y_dir = random.randint(-2, 2)
            utime.sleep_ms(250)

    # Control del rebote en la pared derecha
    if ball_x > thumby.DISPLAY_W - PAD_WIDTH - BALL_SIZE:
        top_paddle = paddle_r - HALF_PAD_HEIGHT
        bottom_paddle = paddle_r + HALF_PAD_HEIGHT
        if ball_y > top_paddle - BALL_SIZE and ball_y < bottom_paddle:
            # La bola rebota en el bate derecho
            play_bounce_sound()
            ball_x_dir = -1
            ball_x = thumby.DISPLAY_W - PAD_WIDTH - BALL_SIZE
        else:
            # Punto para el jugador izquierdo
            play_score_sound()
            l_score += 1
            ball_x = HALF_WIDTH
            ball_y = HALF_HEIGHT
            ball_x_dir = random.randint(0, 1)
            if ball_x_dir == 0:
                ball_x_dir = -1
            ball_y_dir = random.randint(-2, 2)
            utime.sleep_ms(250)

    # Borra la pantalla
    thumby.display.fill(0)
    # Dibujamos la red
    thumby.display.drawLine(HALF_WIDTH, 0, int(thumby.DISPLAY_W / 2), thumby.DISPLAY_H)
    # Dibujamos el marcador de puntos
    thumby.display.drawText(str(l_score), HALF_WIDTH - 20, 5)
    thumby.display.drawText(str(r_score), HALF_WIDTH + 5, 5)
    # Dibuja los bates y la bola
    draw_paddle(1, paddle_l)
    draw_paddle(2, paddle_r)
    draw_ball(ball_x, ball_y)
    # Refrescamos pantalla con lo que hemos dibujado en el bucle principal
    thumby.display.update()
    # Retardo para ajustar velocidad del juego
    utime.sleep_ms(LOOP_DELAY)
