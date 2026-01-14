## ▶ 코드 실행 방법

이 프로젝트는 Python과 Streamlit을 사용한 웹 애플리케이션입니다.  
아래 순서를 위에서부터 그대로 따라 하면 실행됩니다.

---

### 1. Python 설치 여부 확인

터미널(cmd)에서 아래 명령어를 입력합니다.

python --version  
또는  
py --version  

`Python 3.x.x`가 출력되면 설치된 상태입니다.  
출력되지 않는 경우 https://www.python.org 에서 Python 3을 설치합니다.  
(설치 시 **Add Python to PATH** 체크 필수)

---

### 2. 프로젝트 파일 받기

1. GitHub 저장소 상단의 **Code** 버튼 클릭  
2. **Download ZIP** 선택  
3. 압축 해제

---

### 3. 프로젝트 폴더로 이동

압축을 푼 폴더에서  
**Shift + 우클릭 → 터미널 열기**

또는 직접 이동:

cd 폴더경로

---

### 4. Streamlit 설치

아래 명령어를 입력합니다.

pip install streamlit

설치 중에는 입력이 되지 않을 수 있으며,  
완료되면 터미널에 다시 입력 가능한 상태가 됩니다.

---

### 5. 실행

streamlit run main.py

만약 위 명령어가 실행되지 않으면 아래 명령을 사용합니다.

python -m streamlit run main.py

---

### 6. 웹사이트 접속

실행 후 터미널에 다음과 같은 주소가 출력됩니다.

Local URL: http://localhost:8501

브라우저에서 자동으로 열리거나,  
주소를 직접 입력해 접속하면 됩니다.

---

### 7. 종료 방법

터미널에서 다음 키를 누르면 서버가 종료됩니다.

Ctrl + C
# -
