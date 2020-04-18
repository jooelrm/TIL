#linux start


sh / csh/ bash / zsh
ls : 현재 위치의 디렉토리 목록 : -a 숨김파일까지 전부 / -l 순서대로
mkdir :  새로운 디렉토리 생성
touch : 새 파일 만들기 - 시트, 한글문서, ppt 등 프로그램을 통해서 만들어야하는 건 x
mv a b : a파일을 b로 이동
cp report ..  : 상위디렉토리로 복사
cd .. : 상위디렉토리로 이동
rm : 파일제거. 바로 디렉토리는 제거 불가. 파일이 전부 없을 때 가능.
rm -r  bin : 디렉토리 안의 파일을 모두 제거, 디렉토리도 제거. 자기 자신도 가능.
mv report.hwp report.java : 이름 변경.
mv report.hwp bin / report.java : 이동도 하면서 이름도 변경 가능
chmod , chown : 권한변경
chmod 777 hello.py < 모든 권한.
555   < 읽고 실행만 가능.
drwx < 앞에 d가 붙으면 디렉토리라는 뜻.
-rwx < 일반파일
rwx < 읽고 쓰고 실행.
rwxrwxrwx 소유자 유저 게스트 
 
 * vim에서 마크다운  .. 전부 간격이 커야 별도로 인식. 너무 가까우면 하나로 인식.
<h1>How to use Markdown<h1> -> # How to use Markdown   .... 보통 h는 제목.
## <h2>
<p>Hello, I am a boy.<\p> : 문단.
- : 순서가 없는 리스트
1. , 2. ..: 순서가 있는 리스트
<img src = “” alt = “cat with dogs”> : html 이미지 불러오기
![cat with dogs](../images/thumbnail.jpg) : 마크다운 이미지 불러오기
[] : alt 텍스트 불러오기.
<a href= “”> go to google<\a> : html 링크
[go to google](https://www.google.com/) : 마크다운 링크
type ‘$ touch hello.py’ on your terminal : ‘’는 소스코드 강조.
‘’’ python
def __init__():
name = self.name
def hello(name):
return print(name)
‘’’
‘’’python 처럼 언어를 적어 해야 해당 언어로 강조.
 
 
 
-vi
vi readme.md : vim으로 readme 파일을 오픈. 
i: insert -> 진입
esc : 노멀모드로 돌아옴.
(노멀모드 상태)
dd :  줄 제거.
p : 줄 복사 
u : 작업취소.
hjkl: 왼쪽 아래 위 오른쪽
shift + a : 맨 오른쪽 끝칸으로 들어가서 인설트
0 : 왼쪽 끝칸으로 이동
:  <-- 커멘드 모드로 진입
(커멘드 모드)
q ! : 전 상태로 덮어쓰고 나가기.
wq : 저장하고 나가기
w : 중간중간 저장하기
---------------------------
터미널상태
----------------------------
cat : vim 없이 파일 텍스트내용 보기.
 
 
 
 
 
 
 

