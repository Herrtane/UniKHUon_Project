#include "arduino.h"

void setup()
{
    // LED_BUILTIN: Arduino에 탑재된 LED 제어 핀(13번 핀)
    // LED_BUILTIN을 출력으로 설정
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
    // LED_BUILTIN에 5V인가 - LED ON
    digitalWrite(LED_BUILTIN, HIGH);
    // 1초 지연
    delay(1000);
    // LED_BUILTIN에 0V인가 - LED OFF
    digitalWrite(LED_BUILTIN, LOW);
    // 1초 지연
    delay(1000);
}
