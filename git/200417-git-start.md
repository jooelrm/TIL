#git start

## Learn git structure

## TODO
   review mathmatics

workspace  -----> index --------> local repository --------> remote repository
 
 
git config --list
hyunjoon$ git config --global user.name "jooelrm"
hyunjoon$ git config --global user.email "jooelrm@outlook.com"
git config --global core.editor "vim"
git config --global core.pager "cat"
 
git config --unset --global user.name
git init  :  해당 폴더 안의 파일을 전부 git 으로 관리.
git status : git 상태
git remote add origin(관습. 별명) https://github.com/jooelrm/first-repo.git
git remote -v : 해당 별명으로 어떤 주소가 있는지 확인.
git add index.py : worksspace -> index
git commit :  index -> commit
 feat : Create index.py
Create index.py to practice git commands.
 
Categories
- feat : features
- docs : documentations
- conf : configurations
- bug-fix : bug fix
git commit -m “ ” : vim으로 넘어가지않고 바로 메세지 입력 가능.
“  : 다음 줄 부터 내용.
git push -u(처음에만) origin(별명) master(브렌치 개념) :  git hub에 등록
git clone https://github.com/jooelrm/TIL.git : git 복제
 

