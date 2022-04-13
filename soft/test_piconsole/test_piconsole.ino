#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Pins OLED
#define OLED_DC  16
#define OLED_CS  17
#define OLED_SCL 18
#define OLED_SDA 19
#define OLED_RES 20

// Pins LED
#define LED_YELLOW 8
#define LED_RED    9
#define LED_GREEN  21
#define LED_IR     22

// Pins Switch
#define SW_B     7
#define SW_A     11
#define SW_RIGHT 12
#define SW_LEFT  13
#define SW_DOWN  14
#define SW_UP    15

// Pins GPIO
#define GPIO_GP0     0
#define GPIO_GP1     1
#define GPIO_GP2     2
#define GPIO_GP3     3
#define GPIO_GP4     4
#define GPIO_GP5     5
#define GPIO_GP6     6
#define GPIO_ADC0    A0

// Pin Buzzer
#define BUZZER 10

// Pin Pot
#define POT_P A1

// Pin LDR
#define LDR_P A2

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, OLED_SDA, OLED_SCL, OLED_DC, OLED_RES, OLED_CS);

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize LED pins as output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_IR, OUTPUT);

  // initialize Switch pins as input.
  pinMode(SW_B, INPUT_PULLUP);
  pinMode(SW_A, INPUT_PULLUP);
  pinMode(SW_RIGHT, INPUT_PULLUP);
  pinMode(SW_LEFT, INPUT_PULLUP);
  pinMode(SW_DOWN, INPUT_PULLUP);
  pinMode(SW_UP, INPUT_PULLUP);


  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC)) {
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();
  display.display();
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_IR, !digitalRead(SW_UP));
  digitalWrite(LED_RED, !digitalRead(SW_LEFT));
  digitalWrite(LED_YELLOW, !digitalRead(SW_RIGHT));
  digitalWrite(LED_GREEN, !digitalRead(SW_DOWN));
  tone(BUZZER, (!digitalRead(SW_A) || !digitalRead(SW_B) ? 1000 : 0));

  display.clearDisplay();
  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.cp437(true);         // Use full 256 char 'Code Page 437' font

  display.setCursor(0, 10);     // Start at top-left corner
  display.write("Pot:");
  display.drawRect(25, 8, 100, 10, SSD1306_WHITE);
  display.setCursor(0, 40);     // Start at top-left corner
  display.write("LDR:");
  display.drawRect(25, 38, 100, 10, SSD1306_WHITE);

  display.fillRect(25, 8, map(analogRead(POT_P), 0, 4096, 0, 100), 10, SSD1306_WHITE);
  display.fillRect(25, 38, map(analogRead(LDR_P), 0, 4096, 0, 100), 10, SSD1306_WHITE);
  display.display();
}
