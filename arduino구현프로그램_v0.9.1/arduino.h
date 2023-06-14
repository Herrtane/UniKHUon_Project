#ifndef __ARDUINO__
#define __ARDUINO__

#include <stdio.h>
#include <stdint.h>
#include <time.h>

#if defined(__APPLE__) || defined(__linux__) || defined(__gnu_linux__) || defined(__unix__)
#include <unistd.h>
#endif
#if defined(_WIN32) || defined(_WIN64)
#include <Windows.h>
#endif

#define LOW 0x0
#define HIGH 0x1

#define INPUT 0x0
#define OUTPUT 0x1

#define LED_BUILTIN 13u

typedef struct _PinDescription
{
    uint8_t *pIORegister; // DDRx[i]
    uint8_t *pPORT;       // PORTx[i]
    uint8_t *pPIN;        // PINx[i]
} PinDescription;

extern PinDescription g_aArduinoDueTable[81];

void delay(uint32_t);
void pinMode(uint8_t, uint8_t);
void digitalWrite(uint8_t, uint8_t);
// void setup();
// void loop();

#endif