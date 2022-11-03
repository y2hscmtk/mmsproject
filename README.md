# Mobile&Smart System Project

라즈베리파이를 이용한 스마트 홈 관리 시스템

다수의 라즈베리파이를 이용, 다양한 모듈을 활용하여 mqtt서버로 통신하며
네이버의 클로바, 카카오의 카카오미니 등과 같은 AI Speaker를 파이썬으로 구현하여
사용자가 특정 명령어를 음성으로 호출시 해당 명령에 맞춰 mqtt서버로 명령을 보내어
각각의 토픽으로 구독된 라즈베리파이 기기에서 해당 명령을 수행함
위 과제의 경우 다수의 라즈베리파이를 이용할수 없으므로, 하나의 라즈베리파이에 
모든 모듈이 연결하여 사용하며 추후 분류하여 사용할 수 있도록 코드는 분리하여 작성한다.
또한 같은 이유로 AI Speaker는 데스크탑에서 구현하여 사용한다. AI Speaker를 라즈베리파이
로 구현할 경우, 라즈베리 파이에 블루투스 둥글과 마이크 모듈, 블루투스 스피커, 등을 달면 된다. 이 시스템을 사용하여 집안의 다양한 가구,등을 손을 대지 않고 이용할 수 있다. 예를 들어
사용자가 '불 꺼줘' 라고 명령을 내리면 AI Speaker에서 '불'이라는 키워드와 '꺼'라는
키워드를 인식하여 라즈베리파이에 연결된 led전등(led를 led전등이라고 가정) 꺼주고 그 반대의
경우도 마찮가지이다. 
작성할 기능의 계획은 
1. 불 키고 끄기(led모듈 이용) 
2. 감시카메라 키고 끄기(정문에 카메라 모듈을 달은 라즈베리파이를 이용) => 쓰레기 무단 투척 방지, 침입 방지, 등에 연관지어 이용가능 위 경우 초음파 센서를 이용
3. 온도 측정(조도 센서 이용), 등이 있다.
