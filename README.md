# Hadoop Command

1. ` hdfs dfs -ls /`
    - 하둡 파일 시스템에서 내가 확인 하고 싶은 경로

2. `mkdir`
    - `hdfs dfs -mkdir /input`
    - `hdfs dfs -mkdir /<folder_name>` : 폴더 생성

3. `put`
    - `hdfs dfs -put <upload_file_root> <upload_place>`

4. `cat`
    - `hdfs dfs -cat <read_file_root>` : 출력하고자 하는 파일 

5. `head/tail`
    - `hdfs dfs -head(tail) <read_file_root>` : 앞(뒤) 일정 갯수만 출력

6. `rm`
    - `hdfs dfs -rm <delete_file_root>` : 파일 삭제

7. `rm -r` : 폴더 삭제
    - `hdfs dfs -rm -r <delete_folder_root>` : 파일 삭제


8. `cat <data> | <python file>`
    - ex) `cat text.txt | python3 mapper.py ` : 'text.txt'파일을 'mapper.py'라는 파이썬 파일에게 넘겨줘서 실행시킨다.


9. `chmod <권한> <file>` : file에 권한을 부여하는 방법  
![권한](../../Desktop/code/vkxuqbatopk21.png)  





`#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌`
`글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다.`