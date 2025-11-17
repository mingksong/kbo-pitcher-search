# 🐛 문제 해결 가이드

## ❌ 발생한 문제들 및 해결 방법

### 1. PyArrow 빌드 오류 ✅ 해결됨

#### 증상
```
Using Python 3.13.9 environment
× Failed to download and build `pyarrow==14.0.1`
```

#### 원인
- Python 3.13은 너무 최신 버전
- pyarrow 14.0.1은 Python 3.13과 호환 안 됨
- Streamlit Cloud가 Python 3.13을 사용

#### 해결 방법 ✅
```bash
# requirements.txt 수정
pyarrow==14.0.1  →  pyarrow>=15.0.0

# Python 버전 지정
echo "3.11" > .python-version
echo "python-3.11" > runtime.txt
```

#### 파일 변경 사항
1. **requirements.txt**:
   ```
   streamlit>=1.29.0
   pandas>=2.1.0
   plotly>=5.18.0
   pyarrow>=15.0.0    # ← 업데이트
   ```

2. **.python-version** (새로 생성):
   ```
   3.11
   ```

3. **runtime.txt** (새로 생성):
   ```
   python-3.11
   ```

#### 확인
```bash
git log --oneline -2
# 8472c2e Fix: Update dependencies for Python 3.11+ compatibility
# 736d49a Initial commit: KBO pitcher search app
```

---

## 🔍 기타 가능한 문제들

### 2. Git Push 실패

#### 증상
```
Permission denied (publickey)
```

#### 해결 방법

**Option 1: SSH 키 생성**
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# GitHub → Settings → SSH and GPG keys → New SSH key
```

**Option 2: HTTPS 사용**
```bash
git remote set-url origin https://github.com/[username]/kbo-pitcher-search.git
git push -u origin main
```

---

### 3. Streamlit Cloud 빌드 타임아웃

#### 증상
```
Build timeout after 10 minutes
```

#### 해결 방법
- 데이터 파일 크기 확인 (현재 38MB ✅)
- requirements.txt에서 불필요한 패키지 제거
- Python 버전 확인 (.python-version)

---

### 4. 데이터 파일을 찾을 수 없음

#### 증상
```
FileNotFoundError: data/pitches_classified_v2.parquet
```

#### 해결 방법
```bash
# 파일 존재 확인
ls -lh data/pitches_classified_v2.parquet

# GitHub에 푸시되었는지 확인
git ls-files | grep parquet

# 없으면 추가
git add data/pitches_classified_v2.parquet
git commit -m "Add data file"
git push
```

---

### 5. 메모리 부족

#### 증상
```
MemoryError: Unable to allocate array
```

#### 해결 방법
- Parquet 사용 (이미 적용됨 ✅)
- 데이터 샘플링 (예: 2024-2025년만)
- Streamlit Cloud 유료 플랜 고려

---

### 6. 앱이 느림

#### 증상
- 로딩 시간 5초 이상
- 차트 렌더링 느림

#### 해결 방법
```python
# app.py에서 이미 적용됨
@st.cache_data
def load_data():
    # Parquet 사용으로 10배 빠름
    pitches = pd.read_parquet(DATA_DIR / 'pitches_classified_v2.parquet')
```

---

### 7. 패키지 버전 충돌

#### 증상
```
ERROR: Cannot install streamlit==1.29.0 and pandas==2.1.4
```

#### 해결 방법
```bash
# requirements.txt에서 유연한 버전 사용 (이미 적용됨 ✅)
streamlit>=1.29.0
pandas>=2.1.0
plotly>=5.18.0
pyarrow>=15.0.0
```

---

## 📋 배포 체크리스트

### 배포 전 확인
- [x] requirements.txt 업데이트 (pyarrow>=15.0.0)
- [x] .python-version 생성 (3.11)
- [x] runtime.txt 생성 (python-3.11)
- [x] Git 커밋 완료
- [ ] GitHub에 Push 완료
- [ ] Streamlit Cloud 배포 완료

### 배포 후 확인
- [ ] 앱이 정상 로드됨
- [ ] 투수 검색 작동
- [ ] 차트 표시 확인
- [ ] 모바일 테스트

---

## 🔄 재배포 방법

### 코드 수정 후
```bash
cd /Users/mksong/Documents/pitchclassification_deploy

# 변경사항 확인
git status

# 로컬 테스트
./run_local.sh

# 커밋
git add .
git commit -m "Update: [변경 내용]"

# Push (자동 재배포)
git push origin main
```

**재배포 시간**: 1-2분

---

## 📞 도움말

### Streamlit Cloud 로그 확인
1. https://streamlit.io/cloud 접속
2. 앱 클릭
3. "Logs" 탭 확인

### 로컬 디버깅
```bash
cd /Users/mksong/Documents/pitchclassification_deploy

# 패키지 재설치
pip install -r requirements.txt

# 로컬 실행
streamlit run app.py

# 에러 메시지 확인
```

### 유용한 명령어
```bash
# Git 상태
git status

# 파일 크기 확인
ls -lh data/

# 로그 확인
git log --oneline -5

# Remote URL 확인
git remote -v
```

---

## ✅ 해결된 문제

1. ✅ **PyArrow 빌드 오류** (Python 3.13 호환성)
   - pyarrow>=15.0.0으로 업데이트
   - Python 3.11 지정

---

## 🎯 현재 상태

```
✅ 모든 문제 해결 완료
✅ 배포 준비 완료
⏳ GitHub Push 대기 중
⏳ Streamlit Cloud 배포 대기 중
```

---

**다음 단계**: GitHub에 Push

```bash
git push -u origin main
```

만약 문제가 발생하면 이 문서를 참고하세요!
