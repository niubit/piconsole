/*
 * Phantom Slayer
 *
 * @version     1.0.2
 * @author      smittytone
 * @copyright   2021, Tony Smith
 * @licence     MIT
 *
 */
#ifndef _PHANTOMS_MAIN_HEADER_
#define _PHANTOMS_MAIN_HEADER_


// Standard, Pico includes
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include "pico/stdlib.h"
#include "pico/binary_info.h"
#include "hardware/gpio.h"
#include "hardware/spi.h"
#include "hardware/adc.h"

// Game includes
#include "gfx.h"
#include "map.h"
#include "phantoms.h"
#include "ssd1306.h"
#include "tinymt32.h"
#include "utils.h"


/*
 * STRUCTURE DEFINITIONS
 */
typedef struct {
    uint8_t  x;
    uint8_t  y;
    uint8_t  width;
    uint8_t  height;
    uint8_t  spot;
} Rect;

typedef struct {
    uint8_t  x;
    uint8_t  y;
    uint8_t  hp;
    uint8_t  hp_max;
    uint8_t  direction;
    uint8_t  back_steps;
} Phantom;

typedef struct {
    bool     in_play;
    bool     show_reticule;
    bool     can_fire;
    bool     is_firing;
    bool     can_teleport;
    bool     is_joystick_centred;
    bool     show_compass;

    uint8_t  phantoms;
    uint8_t  audio_range;
    uint8_t  tele_x;
    uint8_t  tele_y;
    uint8_t  start_x;
    uint8_t  start_y;
    uint8_t  level_kills;
    uint8_t  map;

    uint16_t level;
    uint16_t level_score;
    uint16_t high_score;

    uint32_t zap_time;
    uint32_t debounce_count_press;
    uint32_t debounce_count_release;
    uint32_t phantom_speed;
} Game;


/*
 * PROTOTYPES
 */
void    setup();
void    play_intro();
void    create_world();
void    init_game();

void    game_loop();
bool    check_joystick(uint16_t x, uint16_t y) ;
uint8_t get_direction(uint16_t x, uint16_t y);

void    update_world(uint32_t now);
void    check_senses();

void    do_teleport();
void    fire_laser();

void    death();
void    show_scores();


/*
 *  CONSTANTS
 */
#define SPI_PORT                                        spi0

#define ON                                              true
#define OFF                                             false

#define PIN_DC                                          16
#define PIN_CS                                          17
#define PIN_SCL                                         18  //SCK
#define PIN_SDA                                         19  //MOSI
#define SSD1306_RST_PIN                                 20
#define PIN_SPEAKER                                     10
#define PIN_TELE_BUTTON                                 7
#define PIN_FIRE_BUTTON                                 11
#define PIN_LED                                         25
#define PIN_RIGHT                                       12
#define PIN_LEFT                                        13
#define PIN_DOWN                                        14
#define PIN_UP                                          15

// Player movement directions
#define DIRECTION_NORTH                                 0
#define DIRECTION_EAST                                  1
#define DIRECTION_SOUTH                                 2
#define DIRECTION_WEST                                  3

#define MOVE_FORWARD                                    0
#define TURN_RIGHT                                      1
#define MOVE_BACKWARD                                   2
#define TURN_LEFT                                       3

// Joystick
#define UPPER_LIMIT                                     2448
#define LOWER_LIMIT                                     1648
#define JOY_MAX                                         4096

// Timer limits
#define DEBOUNCE_TIME_US                                5000
#define ANIM_TIME_US                                    22000
#define PHANTOM_MOVE_TIME_US                            1000000
#define LASER_RECHARGE_US                               2000000
#define MAP_POST_KILL_SHOW_MS                           3000

// Map square types
#define MAP_TILE_WALL                                   0xEE
#define MAP_TILE_CLEAR                                  0xFF
#define MAP_TILE_TELEPORTER                             0xAA
#define MAX_VIEW_RANGE                                  5

#define MAX_PHANTOMS                                    3
#define ERROR_CONDITION                                 99
#define PHANTOM_NORTH                                   1
#define PHANTOM_EAST                                    2
#define PHANTOM_SOUTH                                   4
#define PHANTOM_WEST                                    8


/*
 *  GLOBALS
 */
uint8_t     oled_height;
uint8_t     oled_width;
bool        oled_inverted;

// Graphics buffer
uint8_t     oled_buffer[1024];
uint8_t     temp_buffer[1024];
uint8_t     side_buffer[1024];
uint8_t     spi_tx_buffer[1025];
uint16_t    oled_buffer_size;
uint16_t    spi_tx_buffer_size;

uint8_t     *draw_buffer;

// Player
uint8_t     player_x;
uint8_t     player_y;
uint8_t     player_direction;

// Graphics structures
Rect        rects[7];

// Game data
Phantom     phantoms[3];
Game        game;

uint32_t    last_draw;
uint32_t    last_phantom_move;
bool        chase_mode;
bool        map_mode;
uint16_t    high_score;

tinymt32_t  tinymt_store;

// _PHANTOMS_MAIN_HEADER_
#endif
