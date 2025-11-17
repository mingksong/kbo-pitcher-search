# ⚾ KBO 투수 레파토리 검색 앱

KBO 투수의 구종별 프로파일, 구속 티어 분포, 무브먼트를 검색하고 시각화하는 웹 애플리케이션

**🌐 Live Demo**: [배포 후 URL 추가]

---

## 📊 주요 기능

### 🔍 투수 검색
- **텍스트 검색**: 2글자만 입력하면 실시간 검색
- **필터링**: 좌완/우완, 시즌 선택
- **직관적**: 드롭다운 대신 검색창 사용

### 📈 시각화
1. **연도별 구종 분포** (Stacked Bar Chart)
2. **구속 티어 분포** (Stacked Bar Chart - S/A/B/C/D)
3. **무브먼트 분석** (Interactive Scatter Plot)
4. **상세 통계** (데이터 테이블)

### 🎯 구속 티어 시스템
- **구종별 독립 티어**: 직구 150km/h = S급, 커브 129km/h = S급
- **5단계 등급**: S(상위 20%) → A → B → C → D(하위 20%)
- **시각적 표현**: 색상 코드로 한눈에 파악

---

## 🚀 빠른 시작

### 온라인 사용
[배포 URL] 접속 (회원가입 불필요)

### 로컬 실행

#### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

#### 2. 앱 실행
```bash
streamlit run app.py
```

#### 3. 브라우저 접속
```
http://localhost:8501
```

---

## 📦 필요 패키지

- **streamlit** (1.29.0+): 웹 앱 프레임워크
- **pandas** (2.1.4+): 데이터 처리
- **plotly** (5.18.0+): 인터랙티브 차트
- **pyarrow** (14.0.1+): Parquet 파일 지원

---

## 📊 데이터

### 데이터 출처
- **기간**: 2021-2025 KBO 정규시즌
- **투구 수**: 1,060,591개
- **투수**: 299명
- **데이터 크기**: 38MB (Parquet 압축)

### 분류 체계
```
[구속티어] [구종명] ([수평무브먼트], [수직무브먼트])

예: S급 슬라이더 (강글러브, 중립)
```

---

## 🎨 사용 예시

### 1. 투수 검색
```
사이드바에서 "폰세" 입력
→ 1명 검색됨
→ 폰세 (우) 선택
```

### 2. 구종별 티어 확인
```
🎯 구속 티어 탭 클릭
→ Stacked Bar Chart 확인
→ 직구: 64.5% S급 (빨강)
→ 슬라이더: 고르게 분포
```

### 3. 무브먼트 분석
```
🌐 무브먼트 탭 클릭
→ 구종별 Scatter Plot
→ 직구는 암사이드+라이징
→ 커브는 글러브+싱킹
```

---

## 🏗️ 프로젝트 구조

```
pitchclassification_deploy/
├── app.py                  # Streamlit 앱 메인
├── requirements.txt        # Python 패키지
├── .streamlit/
│   └── config.toml        # Streamlit 설정
├── data/
│   └── pitches_classified_v2.parquet  # 투구 데이터
└── README.md              # 본 문서
```

---

## 🔧 기술 스택

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **Data Format**: Parquet (Apache Arrow)
- **Deployment**: Streamlit Cloud

---

## 📝 분류 기준

### 구속 티어 (Velocity Tier)
- 구종별, 투수손별 백분위 기반
- S급: 상위 20%, A급: 60-80%, B급: 40-60%, C급: 20-40%, D급: 하위 20%

### 무브먼트 분류
#### 수평 (Horizontal)
- 강암사이드 / 암사이드 / 중립 / 글러브 / 강글러브

#### 수직 (Vertical)
- 강라이징 / 약라이징 / 중립 / 약싱킹 / 강싱킹

---

## 🌐 배포

### Streamlit Cloud
1. GitHub에 Push
2. https://streamlit.io/cloud 접속
3. "New app" → Repository 선택 → Deploy

자세한 내용은 `.claude/` 폴더의 가이드 참고

---

## 📱 호환성

- ✅ 데스크톱 브라우저 (Chrome, Safari, Firefox)
- ✅ 모바일 브라우저 (iOS, Android)
- ✅ 태블릿

---

## 🐛 문제 해결

### 데이터 로딩 느림
→ Parquet 형식 사용 (이미 적용됨)

### 투수를 찾을 수 없음
→ 2글자 이상 입력, 정확한 이름 확인

### 차트가 안 보임
→ 브라우저 새로고침 (Ctrl+F5)

---

## 📞 문의 및 기여

- **이슈**: GitHub Issues
- **기여**: Pull Requests 환영
- **라이선스**: MIT

---

## 🙏 Credits

### 데이터 출처
- KBO 투구 추적 데이터 (2021-2025)

### 기술
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)

---

**⚾ Happy Analyzing!**

*최종 업데이트: 2025-11-17*
