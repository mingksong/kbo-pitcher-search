#!/usr/bin/env python3
"""
KBO 투수 레파토리 검색 앱

투수를 검색하여 구종별 프로파일, 티어 분포, 무브먼트 등을 시각화
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="KBO 투수 레파토리 검색",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 데이터 경로
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'

@st.cache_data
def load_data():
    """데이터 로드 (캐싱)"""
    # Parquet 사용 (CSV보다 10배 빠름)
    pitches = pd.read_parquet(DATA_DIR / 'pitches_classified_v2.parquet')

    # pitch_result 추가 (whiff rate 계산용)
    # 여기서는 간단히 스킵하고 나중에 추가

    return pitches

@st.cache_data
def get_pitcher_list(df):
    """투수 목록 생성"""
    pitchers = df[['pitcher_pcode', 'pitcher_name', 'pitcher_hand']].drop_duplicates()
    pitchers = pitchers.sort_values('pitcher_name')
    return pitchers

def get_pitcher_summary(df, pitcher_pcode):
    """투수 기본 정보"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    summary = {
        'name': pitcher_df['pitcher_name'].iloc[0],
        'hand': '좌완' if pitcher_df['pitcher_hand'].iloc[0] == 'L' else '우완',
        'total_pitches': len(pitcher_df),
        'seasons': sorted(pitcher_df['season_year'].unique()),
        'pitch_types': pitcher_df['pitch_type'].nunique()
    }

    return summary

def plot_yearly_pitch_distribution(df, pitcher_pcode):
    """연도별 구종 분포"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    # 연도별 구종 집계
    yearly = pitcher_df.groupby(['season_year', 'pitch_type']).size().reset_index(name='count')

    # Stacked bar chart
    fig = px.bar(
        yearly,
        x='season_year',
        y='count',
        color='pitch_type',
        title='연도별 구종 분포',
        labels={'season_year': '시즌', 'count': '투구 수', 'pitch_type': '구종'},
        height=400
    )

    fig.update_layout(
        xaxis_title='시즌',
        yaxis_title='투구 수',
        legend_title='구종',
        hovermode='x unified'
    )

    return fig

def plot_velocity_tier_distribution(df, pitcher_pcode):
    """구종별 구속 티어 분포 (Stacked Bar Chart)"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    # 구종별 티어 집계
    tier_dist = pitcher_df.groupby(['pitch_type', 'velocity_tier']).size().reset_index(name='count')

    # 각 구종별로 비율 계산
    tier_dist['total'] = tier_dist.groupby('pitch_type')['count'].transform('sum')
    tier_dist['percentage'] = (tier_dist['count'] / tier_dist['total'] * 100).round(1)

    # 티어 순서 정렬
    tier_order = ['S', 'A', 'B', 'C', 'D']
    tier_dist['velocity_tier'] = pd.Categorical(
        tier_dist['velocity_tier'],
        categories=tier_order,
        ordered=True
    )
    tier_dist = tier_dist.sort_values(['pitch_type', 'velocity_tier'])

    # Stacked bar chart (비율 기준)
    fig = px.bar(
        tier_dist,
        x='pitch_type',
        y='percentage',
        color='velocity_tier',
        title='구종별 구속 티어 분포 (비율)',
        labels={
            'pitch_type': '구종',
            'percentage': '비율 (%)',
            'velocity_tier': '티어'
        },
        color_discrete_map={
            'S': '#e74c3c',
            'A': '#e67e22',
            'B': '#f39c12',
            'C': '#2ecc71',
            'D': '#3498db'
        },
        height=500,
        text='percentage'
    )

    # 텍스트 포맷 (소수점 1자리 + %)
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont_size=10
    )

    fig.update_layout(
        xaxis_title='구종',
        yaxis_title='비율 (%)',
        legend_title='구속 티어',
        hovermode='x unified',
        barmode='stack',
        yaxis=dict(range=[0, 100])
    )

    return fig

def plot_movement_scatter(df, pitcher_pcode):
    """무브먼트 scatter plot"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    # 유효한 무브먼트만
    valid = pitcher_df[pitcher_df['pfx_x'].notna() & pitcher_df['pfx_z'].notna()]

    fig = px.scatter(
        valid,
        x='pfx_x',
        y='pfx_z',
        color='pitch_type',
        title='구종별 무브먼트 분포',
        labels={'pfx_x': '수평 무브먼트 (inches)', 'pfx_z': '수직 무브먼트 (inches)', 'pitch_type': '구종'},
        height=500,
        opacity=0.6
    )

    # 축 선 추가
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)

    fig.update_layout(
        xaxis_title='수평 무브먼트 (inches)',
        yaxis_title='수직 무브먼트 (inches)',
        legend_title='구종'
    )

    return fig

def create_pitch_stats_table(df, pitcher_pcode):
    """구종별 상세 통계 테이블"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    # 구종별 집계
    stats = pitcher_df.groupby('pitch_type').agg({
        'pitch_no': 'count',
        'speed': ['mean', 'std', 'min', 'max'],
        'pfx_x': 'mean',
        'pfx_z': 'mean'
    }).reset_index()

    stats.columns = ['구종', '투구 수', '평균 구속', '표준편차', '최소', '최대', 'pfx_x', 'pfx_z']

    # 비율 추가
    stats['비율'] = (stats['투구 수'] / stats['투구 수'].sum() * 100).round(1)

    # 정렬
    stats = stats.sort_values('투구 수', ascending=False)

    # 소수점 정리
    stats['평균 구속'] = stats['평균 구속'].round(1)
    stats['표준편차'] = stats['표준편차'].round(1)
    stats['최소'] = stats['최소'].round(0)
    stats['최대'] = stats['최대'].round(0)
    stats['pfx_x'] = stats['pfx_x'].round(1)
    stats['pfx_z'] = stats['pfx_z'].round(1)

    # 컬럼 순서
    stats = stats[['구종', '투구 수', '비율', '평균 구속', '표준편차', '최소', '최대', 'pfx_x', 'pfx_z']]

    return stats

def create_tier_breakdown_table(df, pitcher_pcode):
    """구종별 티어 분포 상세 테이블"""
    pitcher_df = df[df['pitcher_pcode'] == pitcher_pcode]

    # 피벗 테이블
    tier_pivot = pd.crosstab(
        pitcher_df['pitch_type'],
        pitcher_df['velocity_tier'],
        normalize='index'
    ) * 100

    # 티어 순서
    tier_order = ['S', 'A', 'B', 'C', 'D']
    tier_pivot = tier_pivot.reindex(columns=[t for t in tier_order if t in tier_pivot.columns], fill_value=0)

    # 소수점 정리
    tier_pivot = tier_pivot.round(1)

    # 컬럼명 변경
    tier_pivot.columns = [f'{t}급 (%)' for t in tier_pivot.columns]
    tier_pivot.index.name = '구종'

    return tier_pivot.reset_index()

# ============================================================================
# 메인 앱
# ============================================================================

def main():
    st.title("⚾ KBO 투수 레파토리 검색")
    st.markdown("---")

    # 데이터 로드
    with st.spinner('데이터 로딩 중...'):
        df = load_data()
        pitchers = get_pitcher_list(df)

    st.success(f"✅ 데이터 로드 완료: {len(df):,}개 투구, {len(pitchers)}명 투수")

    # 사이드바: 투수 검색
    st.sidebar.header("🔍 투수 검색")

    # 텍스트 검색
    search_query = st.sidebar.text_input(
        "투수 이름 입력 (2글자 이상)",
        placeholder="예: 폰세, 양현종, 박세웅",
        help="투수 이름의 일부를 입력하세요"
    )

    # 손 필터
    hand_filter = st.sidebar.radio(
        "투수손 필터",
        options=['전체', '좌완', '우완'],
        index=0,
        horizontal=True
    )

    # 필터링
    if hand_filter == '좌완':
        filtered_pitchers = pitchers[pitchers['pitcher_hand'] == 'L'].copy()
    elif hand_filter == '우완':
        filtered_pitchers = pitchers[pitchers['pitcher_hand'] == 'R'].copy()
    else:
        filtered_pitchers = pitchers.copy()

    # 텍스트 검색 필터링
    if search_query and len(search_query) >= 2:
        filtered_pitchers = filtered_pitchers[
            filtered_pitchers['pitcher_name'].str.contains(search_query, na=False)
        ]

    # 검색 결과 표시
    if len(filtered_pitchers) == 0:
        st.sidebar.warning("⚠️ 검색 결과가 없습니다.")
        st.warning("투수를 찾을 수 없습니다. 다른 이름을 입력해주세요.")
        return

    st.sidebar.success(f"✅ {len(filtered_pitchers)}명 검색됨")

    # 투수 선택 (라디오 버튼으로 변경 - 검색 결과가 적을 때 편리)
    pitcher_display_list = [
        f"{row['pitcher_name']} ({'좌' if row['pitcher_hand'] == 'L' else '우'})"
        for _, row in filtered_pitchers.iterrows()
    ]

    # 검색 결과가 많으면 selectbox, 적으면 radio
    if len(filtered_pitchers) <= 10:
        selected_display = st.sidebar.radio(
            "투수 선택",
            options=pitcher_display_list,
            index=0
        )
    else:
        selected_display = st.sidebar.selectbox(
            "투수 선택",
            options=pitcher_display_list,
            index=0
        )

    # 선택된 투수의 pcode 찾기
    selected_idx = pitcher_display_list.index(selected_display)
    pitcher_pcode = filtered_pitchers.iloc[selected_idx]['pitcher_pcode']

    # 시즌 필터
    pitcher_seasons = sorted(df[df['pitcher_pcode'] == pitcher_pcode]['season_year'].unique())

    season_filter = st.sidebar.multiselect(
        "시즌 선택",
        options=pitcher_seasons,
        default=pitcher_seasons
    )

    # 데이터 필터링
    filtered_df = df[
        (df['pitcher_pcode'] == pitcher_pcode) &
        (df['season_year'].isin(season_filter))
    ]

    if len(filtered_df) == 0:
        st.warning("⚠️ 선택한 조건에 해당하는 데이터가 없습니다.")
        return

    # ========================================================================
    # 메인 화면
    # ========================================================================

    # 투수 요약
    summary = get_pitcher_summary(filtered_df, pitcher_pcode)

    st.header(f"📊 {summary['name']} ({summary['hand']})")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("총 투구 수", f"{summary['total_pitches']:,}개")

    with col2:
        st.metric("시즌", f"{min(summary['seasons'])}-{max(summary['seasons'])}")

    with col3:
        st.metric("구종 수", f"{summary['pitch_types']}종")

    with col4:
        seasons_text = ', '.join(map(str, summary['seasons']))
        st.metric("활동 시즌", seasons_text)

    st.markdown("---")

    # 탭 구성
    tab1, tab2, tab3, tab4 = st.tabs(["📈 연도별 분석", "🎯 구속 티어", "🌐 무브먼트", "📋 상세 통계"])

    with tab1:
        st.subheader("연도별 구종 분포")
        fig1 = plot_yearly_pitch_distribution(filtered_df, pitcher_pcode)
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("구종별 통계")
        stats_table = create_pitch_stats_table(filtered_df, pitcher_pcode)
        st.dataframe(stats_table, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("구종별 구속 티어 분포")

        # Stacked bar chart
        fig2 = plot_velocity_tier_distribution(filtered_df, pitcher_pcode)
        st.plotly_chart(fig2, use_container_width=True)

        st.info("""
        📊 **차트 해석**
        - 각 구종별로 S/A/B/C/D급 비율을 쌓은 막대로 표시
        - 막대 안의 숫자는 해당 티어의 비율(%)
        - 색상: 빨강(S급) → 주황(A급) → 노랑(B급) → 초록(C급) → 파랑(D급)
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**구속 티어 설명**")
            st.markdown("""
            - **S급**: 상위 20% (해당 구종 기준)
            - **A급**: 60-80%
            - **B급**: 40-60%
            - **C급**: 20-40%
            - **D급**: 하위 20%
            """)

        with col2:
            st.markdown("**참고**")
            st.markdown("""
            - 구종별로 독립적인 티어
            - 직구 150km/h = S급
            - 커브 129km/h = S급 (커브 기준)
            - 같은 구속이라도 구종마다 다른 티어
            """)

        st.subheader("구종별 티어 분포 상세 (숫자)")
        tier_table = create_tier_breakdown_table(filtered_df, pitcher_pcode)
        st.dataframe(tier_table, use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("구종별 무브먼트 분포")
        fig3 = plot_movement_scatter(filtered_df, pitcher_pcode)
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("**무브먼트 해석**")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **수평 무브먼트 (pfx_x)**:
            - 우완 기준: 음수(-) = 암사이드 (왼쪽)
            - 우완 기준: 양수(+) = 글러브사이드 (오른쪽)
            - 좌완은 반대
            """)

        with col2:
            st.markdown("""
            **수직 무브먼트 (pfx_z)**:
            - 양수(+) = 라이징 (중력 극복)
            - 음수(-) = 싱킹 (중력보다 떨어짐)
            - 직구: 대부분 양수
            - 커브: 대부분 음수
            """)

    with tab4:
        st.subheader("전체 상세 통계")

        # 투구 분류별 상위 20개
        pitch_labels = filtered_df['pitch_label'].value_counts().head(20).reset_index()
        pitch_labels.columns = ['투구 분류', '투구 수']
        pitch_labels['비율 (%)'] = (pitch_labels['투구 수'] / len(filtered_df) * 100).round(1)

        st.markdown("**가장 많이 사용하는 투구 (Top 20)**")
        st.dataframe(pitch_labels, use_container_width=True, hide_index=True)

        # 무브먼트 통계
        st.markdown("**무브먼트 통계**")

        h_movement = filtered_df['h_movement'].value_counts().reset_index()
        h_movement.columns = ['수평 무브먼트', '투구 수']
        h_movement['비율 (%)'] = (h_movement['투구 수'] / len(filtered_df) * 100).round(1)

        v_movement = filtered_df['v_movement'].value_counts().reset_index()
        v_movement.columns = ['수직 무브먼트', '투구 수']
        v_movement['비율 (%)'] = (v_movement['투구 수'] / len(filtered_df) * 100).round(1)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(h_movement, use_container_width=True, hide_index=True)

        with col2:
            st.dataframe(v_movement, use_container_width=True, hide_index=True)

    # 푸터
    st.markdown("---")
    st.markdown("""
    **데이터**: 2021-2025 KBO 정규시즌

    **분류 체계**: 구속 티어(S/A/B/C/D) × 수평 무브먼트 × 수직 무브먼트

    **제작**: KBO 투구 분류 체계 연구
    """)


if __name__ == '__main__':
    main()
