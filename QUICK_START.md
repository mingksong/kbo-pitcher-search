# 🚀 빠른 시작 가이드

## 📍 현재 위치
```
/Users/mksong/Documents/pitchclassification_deploy
```

---

## ⚡ 3단계로 배포하기

### 1단계: Git 초기화 (1분)

```bash
cd /Users/mksong/Documents/pitchclassification_deploy

git init
git branch -M main
git add .
git commit -m "Initial commit: KBO pitcher search app"
```

---

### 2단계: GitHub Repository 생성 (2분)

1. https://github.com/new 접속
2. Repository name: `kbo-pitcher-search`
3. Visibility: **Public** ✓
4. "Create repository" 클릭
5. 터미널에서 실행:

```bash
git remote add origin git@github.com:[username]/kbo-pitcher-search.git
git push -u origin main
```

---

### 3단계: Streamlit Cloud 배포 (2분)

1. https://streamlit.io/cloud 접속
2. "Sign up" → GitHub 로그인
3. "New app" 클릭
4. Repository: `[username]/kbo-pitcher-search`
5. Main file: `app.py`
6. **Deploy!** 클릭

---

## ✅ 완료!

앱 URL:
```
https://kbo-pitcher-search.streamlit.app
```

**총 소요 시간: 5분**

---

## 🧪 로컬 테스트 (배포 전)

```bash
# 패키지 설치
pip install -r requirements.txt

# 앱 실행
./run_local.sh

# 또는
streamlit run app.py
```

브라우저: http://localhost:8501

---

## 📚 상세 가이드

### 배포 관련
- `.claude/deployment_guide.md` - 완전한 배포 가이드
- `README.md` - 프로젝트 설명

### 앱 관련
- `app.py` - 앱 소스 코드
- `requirements.txt` - 패키지 목록
- `.streamlit/config.toml` - Streamlit 설정

---

## 🐛 문제 발생 시

### Git Push 실패
```bash
# HTTPS 사용
git remote set-url origin https://github.com/[username]/kbo-pitcher-search.git
git push -u origin main
```

### SSH 키 설정
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# GitHub → Settings → SSH keys에 추가
```

---

## 📞 도움말

- `.claude/deployment_guide.md` - 상세 가이드
- https://docs.streamlit.io - Streamlit 문서

---

**지금 바로 시작하세요!** 🚀
