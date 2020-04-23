#GIT

## git branch practice


git branch arm : 브렌치 arm을 생성... 브렌치는 공간 이동의 개념.
 
git branch : 브렌치 확인
 
git checkout arm : 브렌치 이동.
 
git checkout master 이후 git merge arm : arm에서 작성한걸 master로 가져옴.
 
git checkout -- .  : 모든 파일을 깃의 최신시점으로 돌리는 것. commit한 다음 시점.
 
git checkout -b leg : 없으면 만들면서 생성 & 이동.
 
reset > 잘못했다는걸 없앰
 
revert > 잘못을 시인
 
conflict 상황 시 :
 
노멀모드에서 <<<<  , ==== 지우기.
 
나머지 주석처리. 후 다시 add commit
 
git branch -D arm: 브랜치 삭제.. 해당 브랜치만 아니면 됌
 
https://danielkummer.github.io/git-flow-cheatsheet/index.ko_KR.html < git flow
 
 
 
PM
 
pm = 레포를 만든다. clone
 
pm - develop = > fizzbuzz.py
 
DEV
 
for 팀장의 레포
 
할 내용: issue 만들기
 
뜬 레포를 clone
 
branch -> git remote add pmorigin()
 
git branch develop -> git pull pmorigin develop
 
work!!!! -> add commit push(your develop)
 
github -> create pull request
 
PM
 
merge
 
DEV&PM
 
git pull pmorigin develop
