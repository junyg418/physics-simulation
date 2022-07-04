# physics

__고등학교 3학년 5월달(2022-05) 제작__  

물리 완전탄성충돌 시뮬레이션 제작  
총 3가지의 시뮬레이션
시뮬레이션 중 무중력 상태 시뮬레이션을 변환한 게임을 제작하였습니다.

__3가지 시뮬레이션은__

 1. 완전 탄성 충돌 시뮬레이션
 2. 완전 탄성 충돌 + x축으로 등가속도 운동 시뮬레이션
 3. 무중력 진공상태(설명 추가 예정)


__모든 속도, 위치 단위는 pixel 단위입니다.__
  
매 프레임마다 배경을 하얀색으로 덮고   
공의 위치를 변경시키며 공을 그리는 형식으로  
덮고 그려지는것이 매우 빠르게 실행되어 공이 움직이는 것처럼 보이게 됩니다.  
  
## 1) 완전탄성충돌 시뮬레이션  
기본값으로 가속도는 0.1px   
     x,y 방향의 속도 : 0  
방향 기본값 : down  
  
방향이 down 일때  
최대 100fps로 한번 연산 될 때마다   
속도는 0.1씩 증가하고  
위치는 현재 위치 + 속도 와 같이 연산됩니다.  
  
만약 시뮬레이션이 실행되고 있는 창의 크기 -  공의 반지름 = 현재 위치 일 때  
방향이 up 으로 전환 됩니다.  
  
방향이 up 일 떄   
속도는 0.1 씩 감소하게 되고  
위 연산과 같이   
위치는 현재 위치 + 속도와 같이 초당 100번 연산되어 위치가 변환됩니다.  
만약 이 속도가 0이 된다면 방향의 down으로 변경됩니다.  
  
## 2)포물선 운동
__완전 탄성충돌 + x축, -x축 방향으로의 등속도 운동 입니다.__  
  
y축 운동으로는 위 설명과 같고  
defult 값으로 right으로 오른쪽으로 먼저 x축방향의 운동이 진행 되고  
  
오른쪽 충돌 연산은  
__시뮬레이션 창의 넓이 - 공의 반지름__ 일 때 __x축의 진행값을 left__ 로 변경됩니다.  
  
왼쪽 충돌 연산은   
__x축의 위치가 공의 반지름__ 일 때 __x축의 진행값을 right__ 으로 변경하게 됩니다.  
  
등속도운동은 속도가 일정해야 하기에  
매 프레임 마다 기본값으로 설정된 10px씩  

right 연산에서는 현재 위치 + 속도  
left 연산에서는 현재위치 - 속도  

와 같이 연산하여 등속도 운동을 구현하면서  
완전탄성충돌을 동시에 실행하며  
__포물선 운동을 구현하였습니다.__  
  
## 3) 무중력 시뮬레이션  
x_posMove, y_posMove 함수를 구현  
x_posMove 함수는  
위치 = 현재 위치 + x의 속도  

    만약 속도가 양수일 경우 오른쪽으로 가고있다고 판단  
    오른쪽 충돌 연산은 현재 시뮬레이션 창 - 공의 반지름 > 현재 위치일 경우  
    현재 속도에 -를 붙혀 속도의 방향을 왼쪽으로 변환 시킵니다.  
    
    만약 속도가 음수일 경우 왼쪽으로 가고있다고 판단  
    왼쪽 충돌 연산은 현재 위치 <= 공의 반지름이면   
    속도에 절대값을 붙혀 양수로 변환시켜 오른쪽방향으로 운동하게 바꿉니다.  

y_posMove 함수는   
위치 = 현재 위치 + y의 속도  
    x_posMove 함수의 연산과 x축이 y축으로 바꿔 논리적으로 비슷함  
  
그리고 매 실행때마다 키입력을 받게 되는데  
방향키를 누르게 되면 절대값 x, y방향의 속도가 증가하거나 감소하게됩니다.  
이 방향키는 __현재 상태__ 의 따라서 위방향 키를 눌렀을 때   
공이 윗쪽으로 운동중이라면 절대값 y 방향의 속도가 증가하게 되고  
공이 아랫쪽으로 운동중이라면 절대값 y방향의 속도가 감소하게 됩니다.  
  
위와같이 위 아래 오른쪽 왼쪽 방향키를 눌렀을 때   
공의 현재 운동 상태에 따라서 절댓값 방향의 속도가 증가하거나 감소하게 됩니다.  
  
## 3-2)위 무중력 시뮬레이션을 게임화  
위 게임에서 속도를 증가시킬 때 공의 상태에 따라서   
절대값 속도가 증가, 감소하는것을 응용시켜

만약 절대값 속도가 연속해서 2번 감속하게 된다면 1아웃이 되고  
3아웃이 된다면 게임이 끝나게 됩니다  
  
이것이 속도 0.1당 10점으로 계산하여 자신의 점수가 표시가 되며   
최고기록은 로컬데이터(txt파일)에 저장되어   
자신의 최고기록도 확인 할 수 있습니다.  
