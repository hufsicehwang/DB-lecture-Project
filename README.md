# 🎬📗 Movie Note
<p align="center"><img src="https://user-images.githubusercontent.com/67450413/182373214-9f6e8eb3-4dc5-4764-8186-ee6e8c62c6c6.PNG"></p>

> 자신이 감상한 영화에 대한 기록을 남길 수 있는 플랫폼입니다. 선택적으로 자신의 감상을 사람들과 함께 공유하며, 영화에 대한 추억을 새롭게 만들어나갈 수 있습니다. 더불어 자신이 기록한 영화에 대한 기본적인 정보를 함께 열람하고, 기록에 남길 수 있어 자신만의 영화록을 만들어 나갈 수 있습니다.

# ⚙ 개발 환경
- Language : `HTML`, `CSS`
- Framework : `Django`
- DataBase : `SQLite3`

# 🚀 OpenAPI
- 기본 요청 URL : `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`
- 요청 parameter : 3번항의 요청 인터페이스 정보를 참조하여 GET 방식으로 호출
> 영화진흥위원회 OpenAPI 데이터를 지정 RESTAPI 형식으로 request하여 JSON 형식으로 response 받았습니다. 전달 받은 JSON 형식의 데이터에서 필요로 하는 요소를 dictionary 구조에 parsing 하여 data set을 형성 하였습니다.

### Interface 예시
- `key`	문자열(필수)	발급받은키 값을 입력합니다.
- `targetDt`	문자열(필수)	조회하고자 하는 날짜를 yyyymmdd 형식으로 입력합니다.
- `itemPerPage`	문자열	결과 ROW 의 개수를 지정합니다.(default : “10”, 최대 : “10“)
- `multiMovieYn`	문자열	다양성 영화/상업영화를 구분지어 조회할 수 있습니다. “Y” : 다양성 영화 “N” : 상업영화 (default : 전체)
- `repNationCd`	문자열	한국/외국 영화별로 조회할 수 있습니다. “K: : 한국영화 “F” : 외국영화 (default : 전체)
- `wideAreaCd`	문자열	상영지역별로 조회할 수 있으며, 지역코드는 공통코드 조회 서비스에서 “0105000000” 로서 조회된 지역코드입니다. (default : 전체)
  - response 예시 : <http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20120101>
   
# 🤨 요구조건 분석
- 영화 커뮤니티 웹 사이트에 가입하려면 가입하려는 회원의 이메일, 비밀번호, 성명 정보를 입력해야 한다.
- 회원들은 자신이 원하는 영화마다 무비 노트를 작성할 수 있는데, 게시판에 올려 사람들과 공유할 수도 있고, 자신만 볼 수 있게 저장할 수도 있다. 세부적으로 무비노트를 작성하기 위해서 무비노트 작성을 원하는 영화 제목, 작성할 무비노트의 내용, 게시판 공개 여부 정보를 입력해야 한다. 입력한 것을 저장하게 되면 영화에 대한 장르, 개봉년도, 별점, 등록 날짜 등이 함께 보여진다.
- 회원이 자신만의 무비 노트를 작성하는데, 회원 한 명은 무비노트를 여러개를 작성 할 수 있고, 회원 없이는 무비노트가 존재 할 수 없다.
- 영화 커뮤니티 웹에 게시판 기능이 있는데, 이 게시판을 통해서 여러 회원들이 올려 놓은 무비노트 내용을 볼 수 있다. 게시판 목록에서는 게시판ID, 글쓴이 이메일, 영화제목, 별점, 작성날짜를 볼 수 있고, 그 목록을 눌렀을 때, 세부적으로 다른 회원들이 쓴 무비노트 내용, 영화의 장르, 개봉일등을 볼 수 있다.
- 게시판에 회원들이 쓴 여러 무비노트들이 올라올 수 있다.
- 우리 커뮤니티 사이트는 원하는 영화를 검색 할 수 있다. 검색 결과로는 영화의 장르, 개봉년도, 개봉국가를 보여준다.
- 우리 커뮤니티 사이트는 원하는 영화에 대한 상세정보를 볼 수 있다. 검색 결과로는 검색한 영화에 대한 상영시간, 제작국가, 상세장르, 심의정보를 보여준다.
- 한 회원은 여러 개의 영화를 검색 할 수 있고, 반대로 공개여부에 따라 영화는 여러 명의 회원에게 검색 될 수 있다.
- 검색된 영화 한 개당 그 영화와 관련된 영화의 상세정보를 볼 수 있다.

# 👩‍💻 Scenario
<p align="center"><img height="600px" width="500px" src="https://user-images.githubusercontent.com/67450413/182372807-c7ab3e37-b0a8-4683-b2ad-7a2c67f4adfd.PNG"></p>

# 🛠 ER diagram
<p align="center"><img height="600px" width="650px" src="https://user-images.githubusercontent.com/67450413/182372317-72b92a99-c49c-4a0b-970d-731b55bb7812.PNG"></p>

# 🎛 Entity Relation
<p align="center"><img height="450px" width="900px" src="https://user-images.githubusercontent.com/67450413/182372612-2ce56945-f789-4586-823d-240392bb5752.PNG"></p>

# Application Image
> 회원가입
<p align="center"><img height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376458-8fc0d979-8caf-4ea2-8465-1753686c2ee7.PNG"></p>

> 로그인
<p align="center"><img  height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376570-f629a54e-91f2-463f-94c7-36a954790563.PNG"></p>

> Movie Note 작성
<p align="center"><img  height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376605-0610d7b8-a91e-4593-80f5-f6536cbb43c3.PNG"></p>

> 전체 공개 게시판
<p align="center"><img  height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376630-b26cfa8b-b034-4e36-86ba-cf1c9630be34.PNG"></p>

> 비공개 개인 게시판
<p align="center"><img  height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376662-0c3f65f6-6f24-4b5b-84e5-5d0a6d753c82.PNG"></p>

> Movie Note
<p align="center"><img  height="400px" width="800px" src="https://user-images.githubusercontent.com/67450413/182376686-be679d18-a525-4c1f-a718-5c9be941ec47.PNG"></p>







