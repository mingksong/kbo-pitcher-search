# 🚀 KBO 투수 검색 앱 배포 가이드

## 📍 현재 위치
```
/Users/mksong/Documents/pitchclassification_deploy
```

이 디렉토리는 **공개 배포 전용**입니다.

---

## ✅ 준비 완료 상태

### 파일 구조
```
pitchclassification_deploy/
├── app.py                              # ✅ Streamlit 앱
├── requirements.txt                    # ✅ 패키지 목록
├── .streamlit/config.toml              # ✅ 설정
├── data/pitches_classified_v2.parquet  # ✅ 데이터 (38MB)
├── README.md                           # ✅ 프로젝트 설명
├── .gitignore                          # ✅ Git 제외 목록
└── .claude/                            # ✅ 배포 가이드
```

### 데이터 크기 확인
- ✅ Parquet: 38MB (GitHub 업로드 가능)
- ✅ 메모리 최적화됨
- ✅ 로딩 속도 빠름

---

## 🎯 배포 단계 (Step-by-Step)

### Step 1: Git 초기화 (한 번만)

```bash
cd /Users/mksong/Documents/pitchclassification_deploy

# Git 초기화
git init

# 기본 브랜치 설정
git branch -M main

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: KBO pitcher search app

- Streamlit web app for pitcher repertoire analysis
- Text-based search with real-time filtering
- Stacked bar charts for velocity tier distribution
- Interactive movement scatter plots
- Parquet data format (38MB)
- 2021-2025 KBO regular season data
"
```

---

### Step 2: GitHub Repository 생성

#### 2-1. GitHub 웹사이트에서
1. https://github.com 접속
2. 로그인
3. 우측 상단 "+" → "New repository" 클릭

#### 2-2. Repository 설정
```
Repository name: kbo-pitcher-search
Description: KBO 투수 레파토리 검색 및 분석 웹 앱
Visibility: ✓ Public (Streamlit Cloud 무료 배포)
Initialize: □ README 추가 안 함 (이미 있음)
           □ .gitignore 추가 안 함 (이미 있음)
```

#### 2-3. Create repository 클릭

---

### Step 3: GitHub 연결 및 Push

```bash
cd /Users/mksong/Documents/pitchclassification_deploy

# GitHub repository 연결
git remote add origin git@github.com:[username]/kbo-pitcher-search.git

# 예시:
# git remote add origin git@github.com:mingksong/kbo-pitcher-search.git

# Push
git push -u origin main
```

**SSH 키 설정 필요 시**:
```bash
# SSH 키 생성 (한 번만)
ssh-keygen -t ed25519 -C "your_email@example.com"

# 공개 키 복사
cat ~/.ssh/id_ed25519.pub

# GitHub → Settings → SSH and GPG keys → New SSH key에 추가
```

---

### Step 4: Streamlit Cloud 배포

#### 4-1. Streamlit Cloud 접속
https://streamlit.io/cloud

#### 4-2. 로그인
- "Sign up" 또는 "Log in"
- **GitHub 계정으로 로그인** 선택
- Streamlit Cloud가 GitHub 접근 권한 요청 → "Authorize" 클릭

#### 4-3. New app 생성
1. "New app" 버튼 클릭
2. Repository 선택:
   ```
   Repository: [username]/kbo-pitcher-search
   Branch: main
   Main file path: app.py
   ```
3. App URL (선택):
   ```
   kbo-pitcher-search
   ```
   → 최종 URL: `https://kbo-pitcher-search.streamlit.app`

#### 4-4. Deploy 클릭

---

### Step 5: 배포 진행 상황 모니터링

Streamlit Cloud 대시보드에서 실시간 로그 확인:

```
Building...
├─ Installing requirements
│  ├─ streamlit ✓
│  ├─ pandas ✓
│  ├─ plotly ✓
│  └─ pyarrow ✓
├─ Loading data (38MB) ✓
└─ App is live! 🎉
```

**소요 시간**: 3-5분

---

## 🎉 배포 완료!

### 앱 URL
```
https://kbo-pitcher-search.streamlit.app
```

### 테스트
1. URL 접속
2. "폰세" 검색
3. 차트 확인
4. 모바일에서도 테스트

---

## 🔄 앱 업데이트 방법

### 코드 수정 후

```bash
cd /Users/mksong/Documents/pitchclassification_deploy

# 로컬 테스트
streamlit run app.py

# 만족하면 Git에 커밋
git add app.py
git commit -m "Update: [변경 내용]"
git push origin main
```

**자동 재배포**: Push 후 1-2분 내 Streamlit Cloud가 자동으로 재배포

---

## 📊 Streamlit Cloud 대시보드

### 주요 기능
- **Logs**: 실시간 로그 확인
- **Settings**:
  - App URL 변경
  - 환경 변수 설정
  - Python 버전 선택
- **Analytics**:
  - 방문자 수
  - 사용 통계
- **Reboot**: 앱 재시작

---

## 🐛 문제 해결

### 문제 1: Git push 실패
```bash
# SSH 키 확인
ssh -T git@github.com

# 또는 HTTPS 사용
git remote set-url origin https://github.com/[username]/kbo-pitcher-search.git
```

### 문제 2: 파일 크기 초과
```
Error: File exceeds 100MB
```
→ CSV 대신 Parquet 사용 (이미 적용됨 ✅)

### 문제 3: 배포 실패
Streamlit Cloud 로그 확인:
- requirements.txt 오타
- 데이터 파일 경로
- Python 버전 호환성

### 문제 4: 앱이 느림
→ Parquet 사용 (이미 최적화됨 ✅)
→ 또는 데이터 샘플링 (2024-2025년만)

---

## 💡 팁

### URL 공유
- 카톡, 이메일, SNS로 공유 가능
- QR 코드 생성하여 모바일 접속
- 누구나 회원가입 없이 접속 가능

### 도메인 커스터마이징
무료 플랜: `*.streamlit.app`
유료 플랜: 커스텀 도메인 (예: `kbo.yoursite.com`)

### 사용 통계
Streamlit Cloud 대시보드에서 확인:
- 일일 방문자 수
- 지역별 분포
- 사용 시간대

---

## 📞 도움말

### Streamlit 공식 문서
- 배포 가이드: https://docs.streamlit.io/streamlit-community-cloud
- API 문서: https://docs.streamlit.io
- 커뮤니티: https://discuss.streamlit.io

### 프로젝트 관련
- README.md: 프로젝트 설명
- app.py: 앱 소스 코드
- 로컬 테스트: `streamlit run app.py`

---

## ✅ 배포 체크리스트

### 배포 전
- [ ] 로컬에서 앱 테스트 완료
- [ ] requirements.txt 확인
- [ ] 데이터 파일 크기 확인 (38MB ✅)
- [ ] README.md 작성 완료

### Git 설정
- [ ] Git 초기화 (`git init`)
- [ ] 첫 커밋 완료
- [ ] GitHub repository 생성
- [ ] Remote 연결
- [ ] Push 완료

### Streamlit Cloud
- [ ] 계정 생성 (GitHub 로그인)
- [ ] Repository 연결
- [ ] App 배포 클릭
- [ ] 배포 완료 확인

### 배포 후
- [ ] 앱 URL 접속 테스트
- [ ] 모든 기능 작동 확인
- [ ] 모바일 테스트
- [ ] URL 공유

---

## 🎯 다음 단계

1. ✅ Git 초기화 및 커밋
2. ✅ GitHub repository 생성
3. ✅ Push to GitHub
4. ✅ Streamlit Cloud 배포
5. ✅ 테스트 및 공유

---

**준비 완료! 바로 시작하세요** 🚀

```bash
cd /Users/mksong/Documents/pitchclassification_deploy
git init
git branch -M main
git add .
git commit -m "Initial commit: KBO pitcher search app"
```
