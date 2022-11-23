# Project 구ㅎ11조
## 1. 프로젝트 소개
![recruit_transparent](https://user-images.githubusercontent.com/108647466/203455288-d11d6708-ddf3-4fef-91cc-f568f7e709d4.png)

채용 공고 정보 제공 서비스 및 구직 커뮤니티 <구해조>

### 프로젝트 기간
2022.11.09 ~ 2022.11.21 2주

### 사용 기술 스택
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
## 2. 팀원
![image](https://user-images.githubusercontent.com/108647466/203455959-b54cdcd9-1d56-4d76-9546-9995b4527cc7.png)
강동현
- 팀장
- 백엔드
  - 정보수집(크롤링)
  - 구직 정보 페이지 기능 전반
  
![image](https://user-images.githubusercontent.com/108647466/203455909-7f6c46eb-a02e-4ed6-bf3c-e28869a9ffc5.png)

김명환
- 프론트엔드
  - 커뮤니티, 로그인
- search 기능 구현
- 발표자

![image](https://user-images.githubusercontent.com/108647466/203455934-8b0dfe91-74dd-42cb-a816-c96c5d517aa4.png)

김현정
- 프론트엔드
  - 채용, 회원 가입, 마이페이지
- 프론트엔드 전반

![image](https://user-images.githubusercontent.com/108647466/203456000-4dee07e0-bddc-4c17-ba6d-a35346b4b1b5.png)

김지영
- 백엔드
  - 회원관리 기능 전반
  - 북마크, 팔로우 등 비동기 구현
  - 구글 소셜로그인 구현
  
![image](https://user-images.githubusercontent.com/108647466/203455944-e9beb998-ec45-4dfd-acdb-061ce33108e0.png)

이진욱
- 백엔드
  - 커뮤니티 기능 전반, 쪽지, AWS 배포
  - Github 소셜로그인 구현

## 3. 벤치마킹
![image](https://user-images.githubusercontent.com/108647466/203455683-8137da0e-63bd-4da3-90ab-63183e1c4b21.png)
![image](https://user-images.githubusercontent.com/108647466/203455698-405fd88f-5672-421b-97b8-6c60ab82c117.png)
![image](https://user-images.githubusercontent.com/108647466/203455708-5329ea5f-c87c-4fbb-bf7f-dd0090fbd49a.png)
![image](https://user-images.githubusercontent.com/108647466/203455850-7bdabcc6-ad74-4151-a1df-fbc3b29bb6db.png)

## 화면 설계
![image](https://user-images.githubusercontent.com/108647466/203456808-edaecb67-a92b-4b81-9b9b-53142eec3835.png)
## ERD
https://www.figma.com/file/IM8q7Q4bM09UYLyfnOo61G/semipjt_2?node-id=303%3A348&t=0Q6WCSuYNWuqG7V2-0
![image](https://user-images.githubusercontent.com/108647466/203456905-26842475-6e24-4dae-89c1-7fec7def7f4b.png)

## 주요 기능 설계
### **accounts**

- 회원가입
- 로그인, 로그아웃
  - 소셜로그인(github,google)
- 유저정보
  - 팔로우/팔로잉
    - 팔로우/팔로잉 리스트 조회,
    - 로그인한 유저만 자신의 팔로잉, 팔로워 삭제가능
    - 비동기
- 작성한 글, 댓글, 좋아요한 글 조회
- post 태그 빈도 순 세개 출력
- 경력의 개월 수 표시
- 수정, 삭제
- 회원탈퇴
  - 회원탈퇴 확인
  - 탈퇴 후 유저 게시글, 댓글 삭제
  - 회원가입, 로그인 제한

### **messages**

-  유저간 쪽지 송수신
-  유저 - 관리자 메세지

### **articles** - 구직사이트

-  구직 정보 조회
  - 크롤링
- 북마크
  - 비동기 구현
-  댓글

### **Post** - 구직 후기 게시판

구직 후기, 커뮤니티 기능

-  조회
  -  조회수, 좋아요 수, 인기순, 최신순 정렬 조회 (비동기)
  -  태그 필터링(ex: #백엔드 팔로우)
  -  무한스크롤
      - [https://a-littlecoding.tistory.com/43](https://a-littlecoding.tistory.com/43)
  -  top button footer
      - ref: [https://okky.kr/community](https://okky.kr/community)
-  작성
  - 다중 이미지
-  수정
-  삭제

### **searches** 서치 크롤링 (앱 따로)

-  커뮤니티 게시글, 채용사이트 글 검색 가능

### **comment**

-  댓글, 대댓글 비동기 작성
-  삭제
-  수정

## 서비스 전체 화면
### 로그인
![Untitled (1)](https://user-images.githubusercontent.com/108647466/203453672-3e8bceb0-3c45-473c-91af-73f679a979c0.png)
### 회원 가입
![Untitled (2)](https://user-images.githubusercontent.com/108647466/203453687-f2b70ed7-0543-4a80-b095-10219654b7c2.png)
### 사용자 페이지
![Untitled (3)](https://user-images.githubusercontent.com/108647466/203453714-f8805223-89c0-4581-aa44-a2502d68820c.png)
### 회원 정보 수정 페이지
![Untitled (4)](https://user-images.githubusercontent.com/108647466/203453718-cf503f50-bc7a-4470-be8e-dcf84c610fc3.png)
### 회원 탈퇴 페이지
![Untitled (5)](https://user-images.githubusercontent.com/108647466/203453721-dabe6f2e-70c9-4a01-bdf9-d1783111057f.png)
### 채용 정보 페이지
![Untitled (6)](https://user-images.githubusercontent.com/108647466/203453727-b579f8c2-92f4-4da7-b2b5-6837f9fe248c.png)
### 채용 정보 상세 페이지
![Untitled (7)](https://user-images.githubusercontent.com/108647466/203453744-135dec7f-f348-4614-87c4-b9ec4a19fa65.png)
### 채용 정보 상세 페이지 - 댓글
![Untitled (8)](https://user-images.githubusercontent.com/108647466/203453748-08c4dcaf-18e4-41a7-9c06-68735756bb0e.png)
### 커뮤니티 메인페이지
![Untitled (9)](https://user-images.githubusercontent.com/108647466/203453756-8536a414-11a1-4c7d-a730-9ccc7422f785.png)
### 커뮤니티 메인페이지 - 무한스크롤
![ezgif com-gif-maker](https://user-images.githubusercontent.com/108647466/203453842-9fa336c0-72e2-423e-9ace-5fbae30fdc70.gif)
### 커뮤니티 게시글 상세 페이지
![Untitled (10)](https://user-images.githubusercontent.com/108647466/203453765-31572e2f-3575-47de-affb-801e734c47e5.png)
### 쪽지 기능 구현
![Untitled (11)](https://user-images.githubusercontent.com/108647466/203453768-91cd4960-c33f-459c-be7d-01175ddc28f0.png)
![Untitled (12)](https://user-images.githubusercontent.com/108647466/203453783-2ec0af3d-9c9e-4f27-b072-2b29722f3cf7.png)
![Untitled (13)](https://user-images.githubusercontent.com/108647466/203453788-3ea68558-3497-49b8-a0fa-a9797e8e7cd6.png)
### 채널톡
![Untitled (14)](https://user-images.githubusercontent.com/108647466/203453792-94151a29-215a-4a7a-befd-4d02ce67eff0.png)
![Untitled (15)](https://user-images.githubusercontent.com/108647466/203453798-daadb107-ac79-4a6d-851a-e6c734c2f3af.png)


## 후기

### 강동현

흔히들 겪는 조별과제 징크스를 겪지 않고 서로 각자의 역할에 최선을 다하여 기능과 화면을 구현한 것이 너무 감사할 따름입니다. 제가 부족한 것은 아닌지 프로젝트가 마무리되는 시점에 다시 한번 돌아보면서 모두 수료까지 건승하길 바랍니다.

### 김명환

첫번째 프로젝트가 끝나고 바로 시작하는 프로젝트 여서 초반에 갈피를 못잡고 헤매고 있을때마다 각자의 자리에서 맡은 바 충실히 해주는 팀원들 모습을 보고
자극 받아서 부족한 실력이지만 최선을 다하려고 노력했던것 같습니다. 익숙하지 않은 프론트엔드 작업이라 서툴기도 하고 이전에 배웠던 내용들에 대해서 기억이 나지 않아 작은 부분을 구현하는데도 많은 시간이 걸리고 오래 붙잡고 있다보니 능률적으로 참여하지 못한거 같아 아쉽지만 그래도 배워가는 부분은 있어 다행인것 같습니다.
다같이 노력해준 덕분에 끝까지 완성 할수 있었습니다 팀원분들께 너무 감사합니다
모두들 고생하셨습니다.

### 김지영

새로운 기능 이것저것 시도해봐서 즐거웠고
그동안 시도해보지 않았던 비동기까지 공부하고 구현할 수 있었던 알찬 시간이었습니다.
팀원분들 모두 고생하셨습니다!!

### 김현정

모각코의 정석이다 할정도로 역할
분배도 적절했고 누구 하나 빠짐없이
열심히 해주셔서 즐겁게 프로젝트
할 수 있었어요. 모두 감사해요

### 이진욱

팀원분들 모두가 최선을 다해준 덕분에 좋은 결과물을 만들 수 있어서 좋았습니다.
특히, 프론트 작업하시는 분들이 고생을 많이 하신 덕분에 퀄리티가 올라갈 수 있었습니다.
그리고 이번에 백엔드를 하면서 배운게 많아 알찬 시간이 되었습니다.
