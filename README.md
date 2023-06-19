# UniKHUon_Project

## Overview

### UniKHUon_Project?

UniKHUon_Project는 Unicorn Engine을 이용하여 Navtive 아두이노 코드를 에뮬레이션 하는 프로젝트입니다. 이 프로그램을 이용하면 물리적인 하드웨어가 없어도 아두이노를 이용한 코딩이 가능합니다.

### Unicorn Engine? 에뮬레이션?

에뮬레이션은 다른 컴퓨터 시스템의 동작을 모방하는 것을 말합니다. 예를 들어, 닌텐도 전용 게임은 닌텐도 하드웨어 위에서만 구동됩니다. 하지만 이를 에뮬레이터를 이용하여 데스크탑 컴퓨터에서도 구동시킬 수 있죠!<br>
Unicorn Engine은 에뮬레이터의 한 종류로, 유명한 에뮬레이터 QEMU에 기반한 CPU 에뮬레이터입니다. 아두이노와 같은 소형 컴퓨팅 시스템에는 마이크로컨트롤러 동작이 중요하기 때문에, 현 프로젝트에서는 가볍고 좋은 성능을 낼 수 있는 Unicorn Engine을 선택하였습니다.

### 무슨 도움이 되나요?

현 프로젝트에서는 기존 아두이노 구동에서 느낄 수 있었던 두 가지 문제점을 해결하고자 진행되었습니다.

1. 아두이노를 사용하기 위해서는 물리적인 하드웨어(보드, 모듈 등)를 반드시 구매해야 함.
2. 기존에 구현된 아두이노 시뮬레이터의 경우, 실제 아두이노 구동 방식과 큰 차이가 존재함. 이로 인해 low level의 테스트를 하기 어려움. 더불어 온라인에서 동작하므로 반드시 인터넷 환경이 필요함.

이러한 문제점을 해결하고자, 오프라인에서 아두이노의 온전한 동작을 보장하는 에뮬레이터를 만들었습니다.

## Environments

이 프로젝트를 실행시키기 위해서는 아래와 같은 환경이 먼저 구축되어야 합니다.

- python3
- python3의 Unicorn 라이브러리
- python3의 Capstone 라이브러리
- python3의 pyQT5 라이브러리

라이브러리는 pip3 install 명령어를 통해 수행할 수 있습니다.

## Results

### Unicorn 기반 Arduino 에뮬레이터의 전체 구조도

<img width="512" src="https://github.com/Herrtane/UniKHUon_Project/blob/main/Image/overview.png"/><br>
프로젝트의 전체적인 구조도입니다. 각 구조에 대한 자세한 설명은 최종보고서를 참고해주시기 바랍니다.

### GUI 구현 결과

<img width="512" src="https://github.com/Herrtane/UniKHUon_Project/blob/main/Image/gui.png"/><br>
구현결과 입니다.

내부는 다음과 같이 구성됩니다.

<img width="512" src="https://github.com/Herrtane/UniKHUon_Project/blob/main/Image/structure2.png"/>

<img width="512" src="https://github.com/Herrtane/UniKHUon_Project/blob/main/Image/structure.png"/>

총 두개의 메인 스레드가 실행됩니다.

- Unicorn engine thread: 컴파일 된 바이트 코드를 에뮬레이션.
- GUI thread: Unicorn engine thread로부터 업데이트 값을 받아 화면에 출력함.

## Conclusion

- 가상화 아두이노 구현을 통해 실제 하드웨어의 제약을 받지 않고 아두이노와 LED, 모터등 다양한 모듈들을 컴퓨터 상에서 GUI로 조작하고 테스트할 수 있도록 하는 것이 최종 목표입니다. 
- 특히, 향후에는 현재 프로젝트 상에서 임의로 짠 C언어로 된 아두이노 예시 프로그램 외에도, 직접 Arduino IDE로 컴파일한 원본 ELF 파일을 이 프로젝트의 Input Code로 넣어서, 성공적으로 에뮬레이션을 동작시키는 것이 궁극적인 목표입니다.
- 아두이노 내의 하드웨어를 Unicorn Emulator를 통해 구현할 수 있으므로, GPIO와 같은 하드웨어 종속적인 기능들을 사용할 수 있으며, 이렇게 구현된 기능들은 추후 아두이노를 다루는 수업에서 교육적인 목적으로 사용하거나, 아두이노와 관련된 실험적인 기능을 구현하는 연구 분야에서 응용할 수 있을 것입니다.
- 경제적, 시간적인 측면에서도 아두이노 하드웨어에 들어가는 비용을 최소화할 수 있기 때문에 기대 효과를 볼 수 있습니다. 그리고 사용자가 직접 하드웨어를 세팅하고 모듈들을 연결해서 사용하는 것에 비해 간편하게 아두이노를 조작할 수 있으므로 시간적인 비용도 줄일 수 있을 것입니다. 

## References

- Unicorn Engine Documentation : https://www.unicorn-engine.org/docs/tutorial.html
- 4 Arduino Simulators You Can Use in Your Electronics Projects : https://www.makeuseof.com/arduino-simulators-electronics-projects/
- ‘AIoT 소프트웨어’ 조진성 교수님 강의자료
- Arduino Official Information: https://www.arduino.cc/
- Unicorn Engine Presentation: https://www.unicorn-engine.org/BHUSA2015-unicorn.pdf
- QEMU Documentation: https://www.qemu.org/docs/master/

## Contact

프로젝트에 대한 궁금한 사항은 아래의 메일로 연락주시면 답변드리겠습니다.

- 이철한 : herrtane@khu.ac.kr
- 안준섭 : anjs0918@khu.ac.kr
