#!/bin/bash

# 로컬 앱 실행 스크립트

echo "========================================="
echo "KBO 투수 검색 앱 - 로컬 실행"
echo "========================================="
echo ""

# 포트 설정
PORT=8501

echo "앱 실행 중..."
echo "URL: http://localhost:$PORT"
echo ""
echo "종료하려면 Ctrl+C를 누르세요"
echo ""

# Streamlit 실행
streamlit run app.py --server.port=$PORT --server.headless=true
