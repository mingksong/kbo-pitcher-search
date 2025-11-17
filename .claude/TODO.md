# ✅ 할 일 목록

## 🎯 배포 준비 상태

### ✅ 완료된 작업

- [x] 배포 전용 디렉토리 생성 (`/Users/mksong/Documents/pitchclassification_deploy`)
- [x] 앱 파일 복사 (app.py, requirements.txt, .streamlit/)
- [x] 데이터 파일 복사 (pitches_classified_v2.parquet, 38MB)
- [x] 데이터 경로 수정 (data/processed → data/)
- [x] README.md 작성
- [x] .gitignore 작성
- [x] Git 초기화 (`git init`)
- [x] 첫 커밋 완료
- [x] `.claude/` 폴더 생성
- [x] 배포 가이드 작성 (deployment_guide.md)
- [x] 빠른 시작 가이드 (QUICK_START.md)
- [x] 로컬 실행 스크립트 (run_local.sh)

---

## 📋 다음 단계 (순서대로)

### 1. GitHub Repository 생성 ⏳

```bash
# 1-1. GitHub 웹사이트에서 repository 생성
https://github.com/new

Repository name: kbo-pitcher-search
Description: KBO 투수 레파토리 검색 및 분석 웹 앱
Visibility: Public ✓

# 1-2. 로컬에서 GitHub 연결
cd /Users/mksong/Documents/pitchclassification_deploy
git remote add origin git@github.com:[username]/kbo-pitcher-search.git

# 1-3. Push
git push -u origin main
```

**예상 소요 시간**: 2-3분

---

### 2. Streamlit Cloud 배포 ⏳

```bash
# 2-1. Streamlit Cloud 접속
https://streamlit.io/cloud

# 2-2. GitHub 로그인
"Sign up" → GitHub 계정으로 로그인

# 2-3. New app 생성
"New app" 클릭
Repository: [username]/kbo-pitcher-search
Branch: main
Main file path: app.py

# 2-4. Deploy!
"Deploy" 버튼 클릭
```

**예상 소요 시간**: 3-5분 (빌드 시간 포함)

---

### 3. 테스트 및 공유 ⏳

```bash
# 3-1. 앱 URL 접속
https://kbo-pitcher-search.streamlit.app

# 3-2. 기능 테스트
- "폰세" 검색 → 1명 검색됨
- 🎯 구속 티어 탭 → Stacked bar 확인
- 🌐 무브먼트 탭 → Scatter plot 확인

# 3-3. 모바일 테스트
스마트폰에서 URL 접속

# 3-4. URL 공유
카톡, 이메일, SNS로 공유
```

**예상 소요 시간**: 5분

---

## 📊 진행 상황

```
[████████████████████████████] 100% - 배포 준비 완료
[□□□□□□□□□□□□□□□□□□□□] 0%   - GitHub 생성
[□□□□□□□□□□□□□□□□□□□□] 0%   - Streamlit 배포
[□□□□□□□□□□□□□□□□□□□□] 0%   - 테스트 및 공유
```

---

## 🎯 현재 할 일

### 즉시 실행 가능

1. **로컬 테스트** (선택):
   ```bash
   cd /Users/mksong/Documents/pitchclassification_deploy
   ./run_local.sh
   ```

2. **GitHub Repository 생성**:
   - https://github.com/new 접속
   - Repository name: `kbo-pitcher-search`
   - Public 선택
   - Create!

3. **Git Push**:
   ```bash
   git remote add origin git@github.com:[username]/kbo-pitcher-search.git
   git push -u origin main
   ```

---

## 📚 참고 문서

### 이 디렉토리 내
- `QUICK_START.md` - 빠른 시작 (3단계)
- `.claude/deployment_guide.md` - 상세 배포 가이드
- `README.md` - 프로젝트 설명

### 외부 링크
- GitHub: https://github.com/new
- Streamlit Cloud: https://streamlit.io/cloud
- Streamlit 문서: https://docs.streamlit.io

---

## ⚠️ 주의사항

### Git Push 전에
- [ ] 로컬에서 앱 테스트 (`./run_local.sh`)
- [ ] 데이터 파일 크기 확인 (38MB ✅)
- [ ] requirements.txt 확인 ✅

### GitHub Repository
- [ ] Public으로 설정 (Streamlit Cloud 무료)
- [ ] Repository name: `kbo-pitcher-search` (권장)

### Streamlit Cloud
- [ ] GitHub 로그인 사용 (OAuth)
- [ ] Main file path: `app.py` (정확히 입력)

---

## 🐛 문제 해결

### SSH 키 없음
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# GitHub → Settings → SSH keys에 추가
```

### HTTPS 사용
```bash
git remote set-url origin https://github.com/[username]/kbo-pitcher-search.git
```

### 앱 실행 오류
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ✨ 배포 후

### URL 확인
```
https://kbo-pitcher-search.streamlit.app
```

### 업데이트 방법
```bash
cd /Users/mksong/Documents/pitchclassification_deploy
git add .
git commit -m "Update: [변경 내용]"
git push origin main
# Streamlit Cloud가 자동으로 재배포 (1-2분)
```

### 분석 확인
Streamlit Cloud 대시보드 → Analytics
- 방문자 수
- 사용 통계

---

## 🎉 체크리스트

배포 완료 후:

- [ ] 앱이 정상 로드됨
- [ ] 투수 검색 작동
- [ ] 차트가 표시됨
- [ ] 모바일에서 테스트
- [ ] URL 공유 완료

---

**다음 단계**: GitHub Repository 생성

```bash
# GitHub 웹사이트 접속
https://github.com/new
```

**궁금한 점이 있으면 `.claude/deployment_guide.md`를 참고하세요!**
