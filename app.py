import streamlit as st
import pandas as pd

# =========================================================
# FINANCIAL DECISION ENGINE
# Executive Financial Planning & Analysis
# =========================================================

st.set_page_config(
    page_title="Financial Decision Engine",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BASELINE
# =========================================================

BASE_HEADCOUNT = 500
AVG_MONTHLY_COST = 16_936.05

BASE_WORKFORCE_COST = (
    BASE_HEADCOUNT
    * AVG_MONTHLY_COST
    * 12
)

BASE_REVENUE = 120_000_000
BASE_BUDGET = 77_000_000


# =========================================================
# SESSION STATE
# =========================================================

if "reset" not in st.session_state:
    st.session_state.reset = 0


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800'
        '&family=Noto+Sans+Arabic:wght@400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {
        font-family:
        Inter,
        "Noto Sans Arabic",
        sans-serif;
    }

    .stApp {
        background: #f7f4f9;
    }

    /* HERO */

    .hero {
        background:
        linear-gradient(
            135deg,
            #2e124a 0%,
            #4B1F73 55%,
            #74499a 100%
        );

        padding: 42px 38px;
        border-radius: 0 0 28px 28px;
        margin-bottom: 30px;
        color: white;
    }

    .hero-eyebrow {
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1.5px;
        opacity: 0.75;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 36px;
        font-weight: 800;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 17px;
        margin-top: 10px;
        opacity: 0.92;
        direction: rtl;
    }

    .hero-author {
        margin-top: 22px;
        font-size: 12px;
        letter-spacing: 1px;
        opacity: 0.72;
    }


    /* SECTION */

    .section-title {
        font-size: 27px;
        font-weight: 800;
        color: #28242d;
        margin-top: 15px;
    }

    .section-subtitle {
        color: #77717e;
        font-size: 14px;
        margin-bottom: 22px;
        direction: rtl;
    }


    /* CARDS */

    .card {
        background: white;
        border: 1px solid #e8e1ed;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 24px rgba(48,18,77,0.06);
        min-height: 145px;
    }

    .card-label {
        color: #77717e;
        font-size: 13px;
        direction: rtl;
    }

    .card-value {
        color: #28242d;
        font-size: 29px;
        font-weight: 800;
        margin-top: 12px;
    }

    .card-sub {
        color: #99929f;
        font-size: 11px;
        margin-top: 6px;
    }


    /* PANELS */

    .panel {
        background: white;
        border: 1px solid #e8e1ed;
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(48,18,77,0.06);
        margin-bottom: 20px;
    }

    .panel-title {
        font-size: 21px;
        font-weight: 800;
        color: #29242f;
        margin-bottom: 5px;
    }

    .panel-subtitle {
        color: #77717e;
        font-size: 12px;
        margin-bottom: 18px;
        direction: rtl;
    }


    /* RESULT */

    .result {
        background: #faf8fb;
        border: 1px solid #e8e1ed;
        border-radius: 16px;
        padding: 17px;
        min-height: 105px;
        margin-bottom: 12px;
    }

    .result-label {
        color: #77717e;
        font-size: 12px;
        direction: rtl;
    }

    .result-value {
        color: #28242d;
        font-size: 22px;
        font-weight: 800;
        margin-top: 8px;
    }

    .good {
        color: #14845b !important;
    }

    .bad {
        color: #b33d4a !important;
    }

    .neutral {
        color: #4B1F73 !important;
    }


    /* DECISION */

    .decision {
        background: #f2edf6;
        border-radius: 17px;
        padding: 18px;
        margin-top: 12px;
        border-left: 5px solid #4B1F73;
    }

    .decision-title {
        font-size: 18px;
        font-weight: 800;
    }

    .decision-text {
        color: #77717e;
        font-size: 12px;
        margin-top: 7px;
        direction: rtl;
    }


    /* NET IMPACT */

    .impact-box {
        background: white;
        border: 1px solid #e8e1ed;
        border-radius: 22px;
        padding: 28px;
        margin: 25px 0;
        box-shadow: 0 8px 24px rgba(48,18,77,0.06);
    }

    .impact-label {
        color: #77717e;
        font-size: 13px;
        letter-spacing: 0.5px;
    }

    .impact-value {
        font-size: 36px;
        font-weight: 800;
        margin-top: 10px;
    }


    /* BUTTON */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 0;
        background: #4B1F73;
        color: white;
        font-weight: 700;
        padding: 11px 16px;
    }

    .stButton > button:hover {
        background: #381656;
        color: white;
    }


    /* SLIDER */

    div[data-baseweb="slider"] {
        margin-bottom: 18px;
    }


    /* FOOTER */

    .footer {
        text-align: center;
        color: #99929f;
        font-size: 11px;
        padding: 30px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-eyebrow">
            FINANCIAL DECISION INTELLIGENCE
        </div>

        <div class="hero-title">
            Financial Decision Engine
        </div>

        <div class="hero-subtitle">
            من البيانات → الأثر المالي → القرار
        </div>

        <div class="hero-author">
            FINANCIAL PLANNING & ANALYSIS
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">Executive Financial Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'نظرة تنفيذية سريعة على الوضع المالي الحالي قبل اتخاذ القرار.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# KPI CARDS
# =========================================================

kpi_cols = st.columns(4)

kpis = [
    (
        "عدد الموظفين",
        f"{BASE_HEADCOUNT:,}",
        "Current Headcount"
    ),
    (
        "تكلفة القوى العاملة السنوية",
        f"{BASE_WORKFORCE_COST / 1_000_000:.2f}M",
        "Annual Workforce Cost"
    ),
    (
        "الإيرادات السنوية",
        f"{BASE_REVENUE / 1_000_000:.2f}M",
        "Annual Revenue"
    ),
    (
        "الميزانية السنوية",
        f"{BASE_BUDGET / 1_000_000:.2f}M",
        "Annual Budget"
    )
]

for col, item in zip(kpi_cols, kpis):

    label, value, subtitle = item

    with col:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-label">
                    {label}
                </div>

                <div class="card-value">
                    {value}
                </div>

                <div class="card-sub">
                    {subtitle}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# SCENARIO ENGINE
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns(
    [0.85, 1.55],
    gap="large"
)


# =========================================================
# LEFT — DECISION DRIVERS
# =========================================================

with left:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Decision Drivers
            </div>

            <div class="panel-subtitle">
                غيّري الافتراضات وشاهدي الأثر المالي فورًا.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    new_employees = st.slider(
        "الموظفون الجدد",
        min_value=-100,
        max_value=200,
        value=0,
        step=5
    )

    salary_increase = st.slider(
        "زيادة الرواتب",
        min_value=0,
        max_value=20,
        value=0,
        step=1,
        format="%d%%"
    )

    revenue_growth = st.slider(
        "نمو الإيرادات",
        min_value=-10,
        max_value=30,
        value=0,
        step=1,
        format="%d%%"
    )

    efficiency = st.slider(
        "كفاءة التشغيل",
        min_value=0,
        max_value=20,
        value=0,
        step=1,
        format="%d%%"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("إعادة ضبط السيناريو"):

        st.rerun()

    st.markdown(
        """
        <div style="
            background:#f4eff7;
            border-radius:14px;
            padding:14px;
            font-size:11px;
            color:#645b69;
            line-height:1.8;
            margin-top:15px;
            direction:rtl;
        ">

        هذه نسخة MVP من محرك القرار المالي.
        <br><br>
        لاحقًا يمكن ربط المحرك ببيانات المؤسسة الفعلية
        وإضافة السيناريوهات والتقارير ومصادر البيانات.

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FINANCIAL ENGINE
# =========================================================

hc = BASE_HEADCOUNT + new_employees

payroll = (
    AVG_MONTHLY_COST
    * hc
    * 12
    * (1 + salary_increase / 100)
    * (1 - efficiency / 100)
)

revenue = (
    BASE_REVENUE
    * (1 + revenue_growth / 100)
)

incremental_cost = (
    payroll - BASE_WORKFORCE_COST
)

revenue_delta = (
    revenue - BASE_REVENUE
)

net_impact = (
    revenue_delta - incremental_cost
)

budget_ratio = (
    payroll / BASE_BUDGET
) * 100


# =========================================================
# DECISION LOGIC
# =========================================================

if net_impact > 1_000_000:

    decision = "قرار إيجابي مبدئي"
    explanation = (
        "الأثر المالي المتوقع موجب وفق الافتراضات الحالية."
    )
    decision_class = "good"

elif net_impact < -1_000_000:

    decision = "يحتاج مراجعة"
    explanation = (
        "الزيادة في التكلفة تتجاوز الأثر المالي المتوقع."
    )
    decision_class = "bad"

else:

    decision = "محايد"
    explanation = (
        "السيناريو قريب من الوضع الحالي ويحتاج تقييمًا إضافيًا."
    )
    decision_class = "neutral"


# =========================================================
# RIGHT — FINANCIAL IMPACT
# =========================================================

with right:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Financial Impact of Decision
            </div>

            <div class="panel-subtitle">
                الأثر المالي المتوقع بناءً على السيناريو المختار.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    result_cols = st.columns(3)

    results = [
        (
            "الموظفون بعد القرار",
            f"{hc:,}",
            ""
        ),
        (
            "التكلفة السنوية الجديدة",
            f"{payroll / 1_000_000:.2f}M",
            ""
        ),
        (
            "الزيادة في التكلفة",
            f"{incremental_cost:,.0f} SAR",
            ""
        ),
        (
            "الإيرادات المتوقعة",
            f"{revenue / 1_000_000:.2f}M",
            ""
        ),
        (
            "الأثر المالي الصافي",
            f"{net_impact:+,.0f} SAR",
            decision_class
        ),
        (
            "التكلفة مقابل الميزانية",
            f"{budget_ratio:.1f}%",
            ""
        )
    ]

    for i, item in enumerate(results):

        label, value, css_class = item

        with result_cols[i % 3]:

            st.markdown(
                f"""
                <div class="result">

                    <div class="result-label">
                        {label}
                    </div>

                    <div class="result-value {css_class}">
                        {value}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # Decision

    st.markdown(
        f"""
        <div class="decision">

            <div class="decision-title {decision_class}">
                {decision}
            </div>

            <div class="decision-text">
                {explanation}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# NET IMPACT HIGHLIGHT
# =========================================================

st.markdown(
    f"""
    <div class="impact-box">

        <div class="impact-label">
            NET FINANCIAL IMPACT
        </div>

        <div class="impact-value {decision_class}">
            {net_impact:+,.0f} SAR
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BUDGET UTILIZATION
# =========================================================

budget_col1, budget_col2 = st.columns(
    [1.4, 1]
)

with budget_col1:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Budget Utilization
            </div>

            <div class="panel-subtitle">
                نسبة تكلفة القوى العاملة من الميزانية السنوية.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        min(
            max(
                budget_ratio / 100,
                0
            ),
            1
        )
    )

    st.caption(
        f"{payroll / 1_000_000:.2f}M SAR "
        f"مقابل ميزانية "
        f"{BASE_BUDGET / 1_000_000:.2f}M SAR "
        f"— {budget_ratio:.1f}%"
    )


with budget_col2:

    st.markdown(
        f"""
        <div class="panel">

            <div class="panel-title">
                Cost per Employee
            </div>

            <div class="panel-subtitle">
                متوسط التكلفة الشهرية للموظف.
            </div>

            <div class="result-value">
                {AVG_MONTHLY_COST:,.0f} SAR
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# COMPARISON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="panel">

        <div class="panel-title">
            Current vs Scenario
        </div>

        <div class="panel-subtitle">
            مقارنة الوضع الحالي بالسيناريو المقترح.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

comparison = pd.DataFrame(
    {
        "Indicator": [
            "Headcount",
            "Annual Workforce Cost",
            "Revenue",
            "Net Financial Impact"
        ],

        "Current": [
            f"{BASE_HEADCOUNT:,}",
            f"{BASE_WORKFORCE_COST / 1_000_000:.2f}M",
            f"{BASE_REVENUE / 1_000_000:.2f}M",
            "0 SAR"
        ],

        "Scenario": [
            f"{hc:,}",
            f"{payroll / 1_000_000:.2f}M",
            f"{revenue / 1_000_000:.2f}M",
            f"{net_impact:+,.0f} SAR"
        ],

        "Change": [
            f"{new_employees:+,}",
            f"{incremental_cost:+,.0f} SAR",
            f"{revenue_delta:+,.0f} SAR",
            f"{net_impact:+,.0f} SAR"
        ]
    }
)

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# FINANCIAL IMPACT BRIDGE
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

bridge_col, scenario_col = st.columns(
    2,
    gap="large"
)


with bridge_col:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Financial Impact Bridge
            </div>

            <div class="panel-subtitle">
                مكونات التغير في الأثر المالي.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    bridge = pd.DataFrame(
        {
            "Component": [
                "Revenue Impact",
                "Incremental Cost",
                "Net Impact"
            ],

            "SAR": [
                revenue_delta,
                -incremental_cost,
                net_impact
            ]
        }
    )

    st.bar_chart(
        bridge.set_index("Component")
    )


# =========================================================
# SCENARIO SNAPSHOT
# =========================================================

with scenario_col:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Scenario Assumptions
            </div>

            <div class="panel-subtitle">
                الافتراضات التي بُني عليها القرار.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    snapshot = pd.DataFrame(
        {
            "Driver": [
                "New Employees",
                "Salary Increase",
                "Revenue Growth",
                "Efficiency"
            ],

            "Selected": [
                f"{new_employees:+}",
                f"{salary_increase}%",
                f"{revenue_growth}%",
                f"{efficiency}%"
            ]
        }
    )

    st.dataframe(
        snapshot,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MANAGEMENT INSIGHT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

if net_impact > 0:

    insight = (
        "السيناريو المقترح يحقق أثرًا ماليًا موجبًا. "
        "يوصى بمراجعة مصدر الإيرادات المتوقع والتأكد من "
        "استدامة التحسن قبل اعتماد القرار."
    )

else:

    insight = (
        "السيناريو المقترح يحقق أثرًا ماليًا سلبيًا. "
        "يوصى بإعادة تقييم التكلفة أو البحث عن بدائل "
        "تحقق الأثر التشغيلي بتكلفة أقل."
    )


st.markdown(
    f"""
    <div class="panel">

        <div class="panel-title">
            Management Insight
        </div>

        <div class="panel-subtitle">
            قراءة تحليلية للقرار.
        </div>

        <div style="
            background:#f4eff7;
            padding:18px;
            border-radius:15px;
            line-height:1.9;
            color:#51495a;
            direction:rtl;
        ">
            {insight}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Financial Decision Engine — MVP
        <br>
        Financial Planning & Analysis
    </div>
    """,
    unsafe_allow_html=True
)
