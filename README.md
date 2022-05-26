# README



## 1. 팀원 정보 및 업무 분담

- 김창현(팀장)
  - 백앤드, 프론트, CSS, USUI및 ERD 구상
- 이창엽
  - 백앤드, 프론트, CSS, DB 구축
- 대부분의 프로젝트 업무를 상의 하에 실행했습니다.



## 2. 목표 서비스 구현 및 실제 구현 정도

- 목표 서비스
  - 서양의 한국의 '라면 먹고 갈래?'에 해당하는 'Netflix and Chill'에 아이디어를 얻어 영화가 주 목적은 아니지만 필요한 커플들을 위한 서비스
  - 흥미를 가질만 한 영화지만 실제로 두 사람의 관심사와는 거리가 있는 영화를 추천하도록 함
- 실제 구현 정도
  - 회원 가입 시 받은 '좋아하는 계절', '좋아하는 장르' 등을 통해 이에 해당하지 않는 영화를 추천
  - 흥미를 가지기엔 충분하도록 자신의 이름이 나오는 영화를 추천
  - 영화가 평점에 기반하여 출력되도록해서 어느 정도 흥미는 가질 수 있도록 함



## 3. 데이터베이스 모델링(ERD)

<img src="README.assets/unknown.png"  />

![](README.assets/unknown2.jpg)

## 4. 필수 기능에 대한 설명

### ACCOUNTS

- Login
  - 첫 화면이 메인 페이지로 이동하지 않고 로그인 창으로 들어옴
  - 두 명의 유저가 로그인을 해야 메인(Home)화면으로 이동 가능하다.
- Sign up
  - Custom된 user model을 통해 sign up시 좋아하는 계절 ,장르 등을 받음
- Profile
  - 기본적인 프로필 수정 기능과 추가적인 핵심적인 기능으로 RESET 기능이 있음
  - RESET을 하면 지금까지의 로그인 기록을 날려줌과 동시에
    마지막으로 로그인을 같이 한 상대가 나와 처음 로그인을 한 이후 몇 번 로그인을 한 지와
    내가 그 이후 몇 번 로그인을 같이 했는 지 알려줌
  - 탈퇴도 가능하며, 탈퇴 시에도 로그인 기록은 모두 삭제 해줌



### MOVIES

- BGM 기능
  - 제일 기본적인 기능은 좋아하는 장르에 해당하지 않는 영화와 좋아하는 계절에 개봉하지 않은 영화를
    추천해 주는 것
  - 배경으로서 영화의 기능을 하기 좋은 '음악' 장르의 영화를 추가적으로 '배경 음악이 좋은 영화'로 추천 함
  - 추천은 평점 기반으로 이루어져서 영화 초반에는 흥미를 가질 수 있도록 함
- NAME SEARCH 기능
  - 이름을 검색 할 시 그 이름의 배역이 나오는 영화 / 그 이름의 배우가 나오는 영화 목록을 추천 함
  - '영화 감상'이 목적이 아닐 것이라는 점에서 비슷한 맥락의 기능

- DETAIL 기능
  - 영화 추천 목록에서 영화에 대한 상세 설명 페이지로 이동할 수 있음
  - 이 페이지에서 영화에 대한 평점을 줄 수 있음
  - 각각의 영화에 대한 댓글도 달 수 있음 (수정, 삭제 가능)



## 느낀 점

1. 아이디어 제시 및 계획 단계

   - 브레인스토밍 방식으로 아이디어를 제시

   - 일정 계획 Tool에도 익숙하지 않아서 Jira를 사용하는 것이 어려웠음

2. UX / UI 및 ERD 작성 단계

   - Tool 사용 경험이 없다보니 draw.io 및 figma를 사용하는 것에도 어려움이 많았음.
   - ERD 툴이 익숙하지 않아 Model에 꼭 필요한 데이터들을 정하지 않고 막연하게 작성하다보니 어려움이 생김

3. 데이터 구축

   - 사용할 API가 제공하는 데이터 구조에 대해 파악하는 것이 중요함
     - 하나의 api 요청으로 모든 데이터를 구축할 수 있을 줄 알았으나 산발적으로 존재해서 그렇지 않았음
       - popular list가 제공하는 영화 정보와 영화 id를 통해 제공받는 영화 정보가 다름
       - genre나 provider는 총 list를 받은 후 db를 구축해야 했음
       - cast의 경우도 별도로 존재
       - example과 달리 실제로 비어있거나 없는 key값들이 존재해서 db구축 중 error가 발생
     - TMDB는 credits의 사람(배역) 이름을 영어로 제공하나 파악하지 못했음
       - 한글을 자음/모음 단위로 분절 해주는 코드 등을 미리 찾아놨으나 TMDB에는 전혀 사용할 수 없었음
   - 데이터 다운로드 방식의 문제
     - 데이터 구축을 위한 module을 python파일로 별도 작성하려 했으나 main 관련 오류가 발생
     - view 함수에서 url을 보내는 방식으로 해결
       - django 구조 상 적절한 방법인 지 의문
       - 본 목적의 view 함수들 아래에 위치하도록 해서 코드 구조 상 구분 했음

4. 백앤드(django)

   -  백앤드 구축을 미리 완료 한 후 프론트 작성을 하려 했으나 백앤드와 프론트를 번갈아 해야 했음
     - 이번엔 공동 작업으로 했으나 분업 했으면 소통이 중요했을 것
   - models.py는 프로젝트 과정에서 정말 많이 변경됨. 사전 ERD 작업 중요함을 느낌.
     - 추가적으로 id 값이 아닌 이상 null=True를 주고 하는 것이 바람직함.
   - models.py와 serializers.py와 views.py에 작성해야 하는 부분들을 명확히 구분하여 이해할 필요가 있음
   - ORM은 대부분 검색을 통해서 해결했는데 원하는 대부분의 기능은 구현되어 있었음
     - distinct, annotate, F(), nulls_last 등 익숙하지 않은 기능들 알게 됨
   - dj_rest_auth
     - account와 관련된 문제가 발생 시 dj_rest_auth 관련 settings.py에 작성해야 할 부분을 빠트린게 많았음
     - 작성하라고 해서 했지만 명확히 이해하지는 못함
     - 스스로 검색해서 해결해야 하는 부분이 있는 건 맞지만..(이하 생략)

5. 프론트(Vuex)

   - 교수님의 조언 명심할 것!!
     - `vue에서 기본은  (1) 컴포넌트가 생성되는 과정에서(created) 적절한 메서드가 호출이 되는지, data가 정의되어 있는지  (2) 메서드가 비동기 요청인 경우 비동기 요청은 제대로 수행되고 있는지  (3) 수행이 되고 있다면 혹시 data fetching 시점과 랜더링 되는 시점이 다르기에 어느 시점에 발생한 오류인지 확인 `
   - state에 데이터가 관리되는 것의 편리함에 대해서 많이 느낌
   - login 기능 관련
     - login을 두 번하게 구현하는 과정에서 첫 login 이후 logout을 하지 않고 login을 한다면 당연히 오류가 날 것이라고 생각해서 logout을 강제로 시키려는 과정에서 error가 발생
     - 그냥 login을 두 번 하더라도 error는 발생하지 않으며 token을 잘 처리해주면 되는 문제 였음
     - dj_rest_auth 및 corsheaders의 login 과정을 정확히 이해하지 못해서 생긴 문제라 생각함.

6.  CSS

   - bootstrap은 만능 키가 아님
     - 모든 기능을 bootstrap에 의존하여 만드려 했으나 별도 css 공부가 반드시 필요하다는 것을 느낌
   - tag 선택자를 주의할 것
     - vue는 어느 view 혹은 component에 작성해도 전체 vue에 적용이 됨
     - tag 선택자를 사용했다가 수정하려 할 때 어디에 작성되어 있는 지 찾느라 고생함
   - 구글링에 의존하지 말 것
     - 대부분 작동하지만 나의 component에 맞는 css 편집이 반드시 필요함.

### 마치며

- '오타'가 아니더라도 기본적인 것을 빼먹는 실수를 많이 함
  - mapActions 등에 ()를 하지 않고 대괄호만 작성
  - api_view를 미작성
- 그래도 최대의 적은 오타
  - 모르는 error이면 오타가 있을 것이라고 생각하고 오타부터 찾기
    - ctrl + F는 정말 유용

  
