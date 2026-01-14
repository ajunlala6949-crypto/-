import streamlit as st
from datetime import datetime
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="조아준 - 포트폴리오",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일링 - 심플하고 미니멀한 디자인
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* 심플한 헤더 */
    .header-section {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
        border: 1px solid #e9ecef;
    }
    
    .header-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        color: #6c757d;
        margin-bottom: 1rem;
    }
    
    .header-info {
        font-size: 0.95rem;
        color: #868e96;
        padding-top: 1rem;
        border-top: 1px solid #e9ecef;
    }
    
    /* 심플한 섹션 */
    .section {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        border: 1px solid #e9ecef;
    }
    
    .section-title {
        background: #495057;
        color: white;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 4rem 0 2.25rem 0;
        padding: 0.9rem 1.2rem;
        border-radius: 6px;
        display: inline-block;
        width: auto;
        letter-spacing: 0.03em;
    }

    /* 큰 섹션 구분선 (섹션이 확실히 끊겨 보이도록) */
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, #adb5bd 15%, #adb5bd 85%, rgba(255,255,255,0) 100%);
        margin: 3.5rem 0 1.75rem 0;
        border-radius: 2px;
    }
    
    /* 부제목 스타일 - 배경 없이 (흰색 텍스트) */
    .subsection-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 2.25rem 0 1.2rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #dee2e6;
        display: block;
    }
    
    .section-content {
        color: #495057;
        font-size: 1rem;
        line-height: 1.8;
        margin-bottom: 1rem;
    }
    
    /* 심플한 카드 */
    .activity-card {
        background: #f8f9fa;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 3px solid #6c757d;
    }
    
    .activity-title {
        background: #495057;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin: -1.25rem -1.25rem 0.5rem -1.25rem;
        padding: 0.75rem 1.25rem;
        border-radius: 8px 8px 0 0;
    }
    
    /* 심플한 스킬 태그 */
    .skill-tag {
        display: inline-block;
        background: #f8f9fa;
        color: #495057;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
        border: 1px solid #dee2e6;
    }
    
    /* 성장 기록 아이템 */
    .growth-item {
        background: #f8f9fa;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 3px solid #6c757d;
    }
    
    .growth-title {
        background: #495057;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin: -1.25rem -1.25rem 0.75rem -1.25rem;
        padding: 0.75rem 1.25rem;
        border-radius: 8px 8px 0 0;
    }
    
    /* 결론 아이템 - 다른 스타일 */
    .growth-conclusion {
        background: #e9ecef;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 2px solid #495057;
        border-left: 4px solid #495057;
    }
    
    .growth-conclusion-title {
        background: #495057;
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        margin: -1.5rem -1.5rem 0.75rem -1.5rem;
        padding: 0.75rem 1.5rem;
        border-radius: 8px 8px 0 0;
    }
    
    /* 마무리 섹션 스타일 */
    .closing-section {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        margin: 2rem 0;
        border: 1px solid #e9ecef;
    }
    
    .closing-content {
        color: #495057;
        font-size: 1.05rem;
        line-height: 2;
        text-align: justify;
    }
    
    /* 푸터 */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #868e96;
        margin-top: 3rem;
        border-top: 1px solid #e9ecef;
        font-size: 0.9rem;
    }
    
    /* 표 스타일 심플하게 */
    .dataframe {
        border-collapse: collapse;
        margin: 1rem 0;
        font-size: 0.95rem;
        width: 100%;
    }
    .dataframe thead tr {
        background: #495057;
        color: white;
        text-align: left;
    }
    .dataframe th {
        padding: 0.75rem;
        border: 1px solid #dee2e6;
        font-weight: 600;
    }
    .dataframe td {
        padding: 0.75rem;
        border: 1px solid #dee2e6;
        background-color: white;
    }
    .dataframe tbody tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    .dataframe tbody tr:hover {
        background-color: #e9ecef;
    }
    
    /* 프로젝트 이미지 카드 */
    .project-image-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .project-image-title {
        font-size: 1rem;
        font-weight: 600;
        color: #495057;
        margin-bottom: 0.75rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e9ecef;
    }
    
    .project-image {
        width: 100%;
        border-radius: 6px;
        margin-bottom: 0.5rem;
    }
    
    /* 이미지 스타일링 - 테두리 및 크기 조정 */
    .project-image-card img {
        width: 100%;
        max-width: 100%;
        max-height: 800px;
        height: auto;
        border: 1.5px solid #6c757d;
        border-radius: 8px;
        padding: 0.3rem;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        object-fit: contain;
    }
    
    /* Streamlit 이미지 컨테이너 스타일 */
    div[data-testid="stImage"] {
        margin: 1rem 0;
    }
    
    div[data-testid="stImage"] img {
        border: 1.5px solid #6c757d !important;
        border-radius: 8px !important;
        padding: 0.3rem !important;
        background: white !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        max-width: 100% !important;
        max-height: 800px !important;
        height: auto !important;
        width: auto !important;
        object-fit: contain !important;
        display: block !important;
        margin: 0.5rem auto !important;
    }
    
    /* 이미지 캡션 스타일 */
    .project-image-card figcaption,
    div[data-testid="stImage"] + p {
        text-align: center;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* 이미지가 있는 카드 내부 여백 조정 */
    .project-image-card {
        overflow: hidden;
    }
    
    .project-feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .project-feature-item {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #495057;
    }
    
    .project-feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #495057;
        margin-bottom: 0.75rem;
    }
    
    /* 반응형 */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        .section {
            padding: 1.5rem;
        }
        .main-container {
            padding: 1rem;
        }
        .project-feature-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # 메인 컨테이너
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # 헤더 섹션
    st.markdown("""
    <div class="header-section">
        <div class="header-title">조아준</div>
        <div class="header-subtitle">Portfolio</div>
        <div class="header-info">
            대왕중학교 1학년 9반 | 프로그래머를 꿈꾸는 학생
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 관심 분야 태그
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <span class="skill-tag">💻 IT</span>
        <span class="skill-tag">🎨 디자인</span>
        <span class="skill-tag">🎬 영상</span>
        <span class="skill-tag">🎮 게임</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    저는 대왕중학교 1학년 9반에 재학 중인 **조아준**입니다.

    IT, 디자인, 영상, 게임 분야에 관심을 가지고 다양한 활동과 학습을 이어오고 있습니다.
    새로운 기술을 배우고 직접 만들어보는 과정을 즐기며, 이를 통해 꾸준히 성장하는 것을 목표로 하고 있습니다.

    제가 가장 좋아하는 과목은 **체육**입니다.
    운동을 통해 몸을 움직이면 즐겁고 스트레스가 해소되며, 집중력 또한 높아진다고 느끼기 때문입니다.
    이러한 경험을 바탕으로 학습에서도 꾸준함과 성실함을 유지하려 노력하고 있습니다.

    앞으로의 장래희망은 **프로그래머**입니다.
    코딩을 통해 문제를 해결하고, 사람들에게 도움이 되는 프로그램이나 콘텐츠를 만드는 개발자가 되고 싶습니다.
    """)
    
    # 2. 활동 섹션
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🏆 활동</div>', unsafe_allow_html=True)
    
    # 2-1. 동아리 체험
    st.markdown("""
    <div class="activity-card">
        <div class="activity-title">🎥 동아리 체험</div>
        <div class="section-content">
            방송부 활동을 통해 영상 촬영과 편집, 콘텐츠 제작 과정을 간접적으로 경험하였습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2-2. 수상 이력 및 자격 사항
    st.markdown("""
    <div class="section-title" style="margin: 2rem 0 1rem 0;">🏅 수상 이력 및 자격 사항</div>
    """, unsafe_allow_html=True)
    
    awards_data = {
        "시기": [
            "유치부",
            "초등학교 1학년",
            "초등학교 2학년",
            "초등학교 2학년",
            "초등학교 6학년",
            "초등학교 6학년",
            "초등학교 6학년",
            "중학교 1학년"
        ],
        "대회/과정명": [
            "제83회 세계아동미술대회",
            "제7회 더줌어린이예술제",
            "제8회 더줌어린이예술제",
            "2020 샘표 어린이 그림대회",
            "파이썬 2급 자격증",
            "제6회 전국학생코딩경진대회",
            "포토샵·일러스트·프리미어프로 과정 수료",
            "청소년 IT 경시대회"
        ],
        "주관기관": [
            "한국미술교육학회",
            "더줌아트센터",
            "더줌아트센터",
            "샘표식품주식회사",
            "한국정보인재개발원",
            "한국경제신문사",
            "SBS아카데미컴퓨터아트학원",
            "한국정보기술진흥원"
        ],
        "수상/인증": [
            "우수상",
            "예술상",
            "예술상",
            "우리맛 연두상",
            "프로그래밍 기초 인증",
            "블록코딩 부문 은상",
            "디지털 그래픽 과정",
            "프로그래밍언어 중등부 부문 장려상"
        ]
    }
    
    df_awards = pd.DataFrame(awards_data)
    
    st.dataframe(
        df_awards,
        use_container_width=True,
        hide_index=True,
        column_config={
            "시기": st.column_config.TextColumn("시기", width="small"),
            "대회/과정명": st.column_config.TextColumn("대회/과정명", width="large"),
            "주관기관": st.column_config.TextColumn("주관기관", width="medium"),
            "수상/인증": st.column_config.TextColumn("수상/인증", width="medium")
        }
    )
    
    # 3. 개인 노력 및 자기주도 학습 섹션
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📚 개인 노력 및 자기주도 학습</div>', unsafe_allow_html=True)
    
    st.markdown("""
    저는 관심 있는 분야에 대해 스스로 학습하며 실력을 키우기 위해 노력해왔습니다.

    **🎬 영상 제작**  
    영상 녹화와 편집을 직접 진행하며 콘텐츠 제작 전반을 경험하였습니다.

    **🎨 디자인**  
    포토샵을 활용하여 그림 작업과 디자인 연습을 꾸준히 해왔습니다.

    **💻 프로그래밍**  
    매일경제 대회 프로젝트 준비를 통해 IT 관련 문제 해결 능력과 기획력을 기르기 위해 노력하고 있습니다.
    """)
    
    # 4. 성장 기록 섹션
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌱 성장 기록</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="growth-item">
        <div class="growth-title">💻 코딩</div>
        <div class="section-content">
            코딩을 처음 시작했을 때는 블록 코딩이 매우 재미있고 흥미롭게 느껴졌지만, 동시에 어려운 부분도 많아 힘들었던 기억이 있습니다.
            그러나 매일 코딩을 하며 간단한 게임을 만들어보는 과정을 반복하면서 점점 자신감과 열정이 생겼고, 이후 코딩을 더욱 적극적으로 배우기 시작했습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="growth-item">
        <div class="growth-title">🎨 디자인 툴</div>
        <div class="section-content">
            포토샵과 일러스트 역시 처음에는 유튜브와 인터넷 자료를 보며 어렵게 느껴졌지만, 학원 과정을 수료한 후에는 생각보다 체계적으로 배울 수 있다는 것을 알게 되었습니다.
            그 이후로 꾸준히 연습하며 실제 작업에 활용할 수 있는 수준까지 발전하게 되었습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="growth-item">
        <div class="growth-title">🎬 영상 편집</div>
        <div class="section-content">
            어릴 때부터 캡컷(CapCut)이라는 영상 편집 프로그램을 사용해 직접 영상을 기획하고 제작해왔습니다.
            영상 편집 알고리즘과 편집 기법을 인터넷 자료를 통해 독학하며, 스스로 배우고 적용하는 경험을 쌓아왔습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="growth-conclusion">
        <div class="growth-conclusion-title">✨ 결론</div>
        <div class="section-content">
            이러한 경험들은 제가 한 가지에 그치지 않고, 관심 분야를 넓히며 지속적으로 성장할 수 있는 기반이 되었습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 5. 현재 진행중인 작업 섹션
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🚀 현재 진행중인 작업</div>', unsafe_allow_html=True)
    
    # 프로젝트 소개
    st.markdown("""
    <div class="activity-card">
        <div class="activity-title">🤖 AI티처 - 제 5회 매일경제 창의발명대회</div>
        <div class="section-content">
            AI티치는 학생이 스스로 학습할 수 있도록 돕는 AI 선생님 기반의 자기주도 학습 웹 서비스입니다. 
            기존 학습 환경에서 학생이 질문할 기회가 제한되거나, 개인별 이해도 차이를 충분히 반영하지 못한다는 문제의식에서 출발한 프로젝트입니다.
            <br><br>
            이 서비스는 24시간 이용 가능한 AI 튜터를 통해 학습 내용을 설명받고, 문제를 풀면서 즉각적인 피드백을 받을 수 있도록 설계되어 있습니다. 
            이를 통해 학생이 학습 흐름을 끊지 않고 자신의 속도에 맞춰 공부할 수 있는 환경을 제공하는 것을 목표로 하고 있습니다.
            <br><br>
            저는 이 프로젝트에서 서비스 기획부터 웹 개발까지 전 과정을 담당하고 있습니다. 
            Python 기반의 Streamlit을 활용하여 실제로 동작하는 웹 서비스를 구현하였으며, UI 구성과 사용자 흐름을 직접 설계하여 학습에 집중할 수 있는 화면을 구성하였습니다.
            <br><br>
            AI티치는 단순히 정보를 제공하는 학습 사이트가 아니라, 모든 학생이 환경에 관계없이 평등한 학습 경험을 할 수 있도록 돕는 것을 목표로 한 프로젝트입니다. 
            현재 기능을 확장하며 완성도를 높이는 단계에 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 주요 기능 및 화면
    st.markdown("""
    <div class="subsection-title">📱 주요 화면 및 기능</div>
    """, unsafe_allow_html=True)
    
    # 메인 페이지
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="project-image-card">
            <div class="project-image-title">🏠 메인 페이지</div>
            <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
                AI티처의 핵심 가치, 추가 혜택(무료 학습 자료, 전문 상담, 성취 인증), 사용자 후기를 한눈에 볼 수 있는 메인 화면입니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
        try:
            st.image("images/mainpage.png", use_container_width=True, caption="AI티처 메인 페이지")
        except:
            st.info("💡 메인 페이지 이미지를 추가해주세요")
        try:
            st.image("images/benefit.png", use_container_width=True, caption="추가 혜택 섹션")
        except:
            pass
    
    with col2:
        st.markdown("""
        <div class="project-image-card">
            <div class="project-image-title">💬 AI 채팅 인터페이스</div>
            <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
                24시간 언제든지 AI 선생님과 대화하며 학습할 수 있는 채팅 화면입니다. 빠른 질문 기능과 대화 초기화 기능을 제공합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
        try:
            st.image("images/talkmassage.png", use_container_width=True, caption="AI 채팅 인터페이스")
        except:
            st.info("💡 채팅 화면 이미지를 추가해주세요")
    
    # 보호자 대시보드 및 회원가입
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown("""
        <div class="project-image-card">
            <div class="project-image-title">👨‍👩‍👧 보호자 대시보드</div>
            <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
                부모가 자녀의 학습 현황, 총 대화 수, 주요 과목, 최근 활동을 실시간으로 확인할 수 있는 대시보드입니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
        try:
            st.image("images/study.png", use_container_width=True, caption="보호자 대시보드 - 학습 현황 모니터링")
        except:
            st.info("💡 대시보드 이미지를 추가해주세요")
    
    with col4:
        st.markdown("""
        <div class="project-image-card">
            <div class="project-image-title">📝 회원가입 페이지</div>
            <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
                학생과 보호자 계정을 구분하여 가입할 수 있는 회원가입 화면입니다. 사용자 유형 선택과 계정 정보 입력을 지원합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
        try:
            st.image("images/signupin.png", use_container_width=True, caption="회원가입 페이지")
        except:
            st.info("💡 회원가입 화면 이미지를 추가해주세요")
    
    # 학습 통계 및 분석
    st.markdown("""
    <div class="project-image-card" style="margin-top: 1.5rem;">
        <div class="project-image-title">📊 학습 통계 및 분석</div>
        <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
            학생의 학습 활동을 시각화하여 보여주는 통계 페이지입니다. 총 대화 수, 주요 과목, 최근 활동, 과목별 학습 분포를 한눈에 확인할 수 있습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.image("images/gragh.png", use_container_width=True, caption="학습 통계 및 분석 - 과목별 학습 분포")
    except:
        st.info("💡 학습 통계 이미지를 추가해주세요")
    
    # 주요 기능 설명
    st.markdown("""
    <div class="subsection-title">✨ 주요 기능</div>
    """, unsafe_allow_html=True)
    
    col5, col6, col7 = st.columns(3)
    with col5:
        st.markdown("""
        <div class="project-feature-item">
            <div class="project-feature-title">🤖 24/7 AI 튜터</div>
            <p style="color: #495057; line-height: 1.6; margin: 0;">
                언제든지 AI 선생님에게 질문하고 즉각적인 피드백을 받을 수 있습니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="project-feature-item">
            <div class="project-feature-title">📊 학습 분석</div>
            <p style="color: #495057; line-height: 1.6; margin: 0;">
                학생의 학습 패턴과 성취도를 분석하여 맞춤형 학습을 제공합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col7:
        st.markdown("""
        <div class="project-feature-item">
            <div class="project-feature-title">👨‍👩‍👧 보호자 모니터링</div>
            <p style="color: #495057; line-height: 1.6; margin: 0;">
                부모가 자녀의 학습 현황을 실시간으로 확인하고 관리할 수 있습니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # 마무리 섹션
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💭 마무리</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="closing-section">
        <div class="closing-content">
            이 포트폴리오는 Python과 Streamlit을 활용하여 지금까지의 관심 분야와 작업 내용을 정리한 결과물입니다.<br><br>
            단순히 결과만 보여주는 것이 아니라, 기획부터 구현까지 스스로 고민하고 시도한 과정을 담고자 했습니다.<br><br>
            아직 배워야 할 것이 많지만, 새로운 기술을 배우는 과정 자체를 즐기며 꾸준히 성장하고 있습니다.<br>
            앞으로도 직접 만들고, 실패하고, 개선하는 경험을 통해 개발자로 성장해 나갈 계획입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 푸터
    st.markdown("""
    <div class="footer">
        <p>create by 조아준</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
