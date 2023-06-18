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

## Results

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

## References
