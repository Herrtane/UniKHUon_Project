#include "arduino.h"

extern void setup();
extern void loop();

// DDRx - I/O 설정 레지스터
uint8_t DDRA[32];
uint8_t DDRB[32];
uint8_t DDRC[32];
uint8_t DDRD[32];

// PORTx - DDRx가 출력일 경우 HIGH or LOW 출력
uint8_t PORTA[32];
uint8_t PORTB[32];
uint8_t PORTC[32];
uint8_t PORTD[32];

// PINx - DDRx가 입력일 경우 현재 핀 상태 읽음
uint8_t PINA[32];
uint8_t PINB[32];
uint8_t PINC[32];
uint8_t PIND[32];

PinDescription g_aArduinoDueTable[81] =
    {
        {DDRA + 8, PORTA + 8, PINA + 8},    // 0, PA8
        {DDRA + 9, PORTA + 9, PINA + 9},    // 1, PA9
        {DDRB + 25, PORTB + 25, PINB + 25}, // 2, PB25
        {DDRC + 28, PORTC + 28, PINC + 28}, // 3, PC28
        {DDRC + 26, PORTC + 26, PINC + 26}, // 4, PC26 and PA29 (disable pa29)
        {DDRC + 25, PORTC + 25, PINC + 25}, // 5, PC25
        {DDRC + 24, PORTC + 24, PINC + 24}, // 6, PC24
        {DDRC + 23, PORTC + 23, PINC + 23}, // 7, PC23
        {DDRC + 22, PORTC + 22, PINC + 22}, // 8, PC22
        {DDRC + 21, PORTC + 21, PINC + 21}, // 9, PC21
        {DDRA + 8, PORTA + 8, PINA + 28},   // 10, PA28 and PC29 (disable pc29)
        {DDRD + 7, PORTD + 7, PIND + 7},    // 11, PD7
        {DDRD + 8, PORTD + 8, PIND + 8},    // 12, PD8
        {DDRB + 27, PORTB + 27, PINB + 27}, // 13, PB27
        {DDRD + 4, PORTD + 4, PIND + 4},    // 14, PD4
        {DDRD + 5, PORTD + 5, PIND + 5},    // 15, PD5
        {DDRA + 13, PORTA + 13, PINA + 13}, // 16, PA13
        {DDRA + 12, PORTA + 12, PINA + 12}, // 17, PA12
        {DDRA + 11, PORTA + 11, PINA + 11}, // 18, PA11
        {DDRA + 10, PORTA + 10, PINA + 10}, // 19, PA10
        {DDRB + 12, PORTB + 12, PINB + 12}, // 20, PB12
        {DDRB + 13, PORTB + 13, PINB + 13}, // 21, PB13
        {DDRB + 26, PORTB + 26, PINB + 26}, // 22, PB26
        {DDRA + 14, PORTA + 14, PINA + 14}, // 23, PA14
        {DDRA + 15, PORTA + 15, PINA + 15}, // 24, PA15
        {DDRD, PORTD, PIND},                // 25, PD0
        {DDRD + 1, PORTD + 1, PIND + 1},    // 26, PD1
        {DDRD + 2, PORTD + 2, PIND + 2},    // 27, PD2
        {DDRD + 3, PORTD + 3, PIND + 3},    // 28, PD3
        {DDRD + 6, PORTD + 6, PIND + 6},    // 29, PD6
        {DDRD + 9, PORTD + 9, PIND + 9},    // 30, PD9
        {DDRA + 7, PORTA + 7, PINA + 7},    // 31, PA7
        {DDRD + 10, PORTD + 10, PIND + 10}, // 32, PD10
        {DDRC + 1, PORTC + 1, PINC + 1},    // 33, PC1
        {DDRC + 2, PORTC + 2, PINC + 2},    // 34, PC2
        {DDRC + 8, PORTC + 8, PINC + 3},    // 35, PC3
        {DDRC + 8, PORTC + 8, PINC + 4},    // 36, PC4
        {DDRC + 8, PORTC + 8, PINC + 5},    // 37, PC5
        {DDRC + 8, PORTC + 8, PINC + 6},    // 38, PC6
        {DDRC + 8, PORTC + 8, PINC + 7},    // 39, PC7
        {DDRC + 8, PORTC + 8, PINC + 8},    // 40, PC8
        {DDRC + 8, PORTC + 8, PINC + 9},    // 41, PC9
        {DDRA + 19, PORTA + 19, PINA + 19}, // 42, PA19
        {DDRA + 20, PORTA + 20, PINA + 20}, // 43, PA20
        {DDRC + 19, PORTC + 19, PINC + 19}, // 44, PC19
        {DDRC + 18, PORTC + 18, PINC + 18}, // 45, PC18
        {DDRC + 17, PORTC + 17, PINC + 17}, // 46, PC17
        {DDRC + 16, PORTC + 16, PINC + 16}, // 47, PC16
        {DDRC + 15, PORTC + 15, PINC + 15}, // 48, PC15
        {DDRC + 14, PORTC + 14, PINC + 14}, // 49, PC14
        {DDRC + 13, PORTC + 13, PINC + 13}, // 50, PC13
        {DDRC + 12, PORTC + 12, PINC + 12}, // 51, PC12
        {DDRB + 21, PORTB + 21, PINB + 21}, // 52, PB21
        {DDRB + 14, PORTB + 14, PINB + 14}, // 53, PB14
        {DDRA + 16, PORTA + 16, PINA + 16}, // 54, PA16
        {DDRA + 24, PORTA + 24, PINA + 24}, // 55, PA24
        {DDRA + 23, PORTA + 23, PINA + 23}, // 56, PA23
        {DDRA + 22, PORTA + 22, PINA + 22}, // 57, PA22
        {DDRA + 6, PORTA + 6, PINA + 6},    // 58, PA6
        {DDRA + 4, PORTA + 4, PINA + 4},    // 59, PA4
        {DDRA + 3, PORTA + 3, PINA + 3},    // 60, PA3
        {DDRA + 2, PORTA + 2, PINA + 2},    // 61, PA2
        {DDRB + 17, PORTB + 17, PINB + 17}, // 62, PB17
        {DDRB + 18, PORTB + 18, PINB + 18}, // 63, PB18
        {DDRB + 19, PORTB + 19, PINB + 19}, // 64, PB19
        {DDRB + 20, PORTB + 20, PINB + 20}, // 65, PB20
        {DDRB + 15, PORTB + 15, PINB + 15}, // 66, PB15
        {DDRB + 16, PORTB + 16, PINB + 16}, // 67, PB16
        {DDRA + 1, PORTA + 1, PINA + 1},    // 68, PA1
        {DDRA, PORTA, PINA},                // 69, PA0
        {DDRA + 17, PORTA + 17, PINA + 17}, // 70, PA17
        {DDRA + 18, PORTA + 18, PINA + 18}, // 71, PA18
        {DDRC + 30, PORTC + 30, PINC + 30}, // 72, PC30
        {DDRA + 21, PORTA + 21, PINA + 21}, // 73, PA21
        {DDRA + 25, PORTA + 25, PINA + 25}, // 74, PA25
        {DDRA + 26, PORTA + 26, PINA + 26}, // 75, PA26
        {DDRA + 27, PORTA + 27, PINA + 27}, // 76, PA27
        {DDRA + 28, PORTA + 28, PINA + 28}, // 77, PA28
        {DDRB + 23, PORTB + 32, PINB + 23}, // 78, PB23
        {DDRB + 11, PORTB + 11, PINB + 11}, // 79, PB11
        {DDRB + 10, PORTB + 10, PINB + 10}, // 80, PB10

};

void delay(uint32_t ms)
{
    if (ms == 0)
    {
        return;
    }

#if defined(__APPLE__) || defined(__linux__) || defined(__gnu_linux__) || defined(__unix__)
    sleep(ms / 1000); // Linux의 sleep함수는 단위가 second이므로 주의
#endif
#if defined(_WIN32) || defined(_WIN64)
    Sleep(ms);
#endif
}

void pinMode(uint8_t pin, uint8_t mode)
{
    *(g_aArduinoDueTable[pin].pIORegister) = mode;
    // printf("Debug : pinMode()\n");
}

void digitalWrite(uint8_t pin, uint8_t val)
{
    *(g_aArduinoDueTable[pin].pPORT) = val;
    // printf("Debug : digitalWrite()\n");
    // printf("%d\n", *(g_aArduinoDueTable[pin].pPORT));
}

int main()
{
    setup();

    while (1)
    {
        loop();
    }

    return 0;
}