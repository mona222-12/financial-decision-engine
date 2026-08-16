import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Financial Decision Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DEMO BASELINE
# =========================================================
BASE_HEADCOUNT = 500
AVG_MONTHLY_COST = 16_936.05

BASE_WORKFORCE_COST = BASE_HEADCOUNT * AVG_MONTHLY_COST * 12
BASE_REVENUE = 120_000_000
BASE_BUDGET = 77_000_000

# =========================================================
# SESSION STATE
# =========================================================
defaults = {
    "new_employees": 0,
    "salary_increase": 0,
    "revenue_growth": 0,
    "efficiency": 0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# RESET
# =========================================================
def reset_scenario():
    for key, value in defaults.items():
        st.session_state[key] = value


# =========================================================
# CALCULATION ENGINE
# =========================================================
new_employees = st.session_state.new_employees
salary_increase = st.session_state.salary_increase
revenue_growth = st.session_state.revenue_growth
efficiency = st.session_state.efficiency

scenario_headcount = BASE_HEADCOUNT + new_employees

scenario_workforce_cost = (
    AVG_MONTHLY_COST
    * scenario_headcount
    * 12
    * (1 + salary_increase / 100)
    * (1 - efficiency / 100)
)

scenario_revenue = BASE_REVENUE * (1 + revenue_growth / 100)

incremental_cost = scenario_workforce_cost - BASE_WORKFORCE_COST
revenue_impact = scenario_revenue - BASE_REVENUE

net_financial_impact = revenue_impact - incremental_cost

budget_pressure = (
    scenario_workforce_cost / BASE_BUDGET * 100
    if BASE_BUDGET
    else 0
)

cost_per_employee = (
    scenario_workforce_cost / scenario_headcount / 12
    if scenario_headcount
    else 0
)

# =========================================================
# DECISION ENGINE
# =========================================================
score = 50

# Revenue
score += revenue_growth * 1.5

# Efficiency
score += efficiency * 2

# Headcount pressure
score -= max(new_employees, 0) * 0.10

# Salary pressure
score -= salary_increase * 1.5

# Net financial impact
if net_financial_impact > 5_000_000:
    score += 15
elif net_financial_impact > 1_000_000:
    score += 8
elif net_financial_impact < -5_000_000:
    score -= 20
elif net_financial_impact < -1_000_000:
    score -= 10

# Budget pressure
if budget_pressure > 130:
    score -= 15
elif budget_pressure > 110:
    score -= 8

score = max(0, min(100, round(score)))

if score >= 70 and net_financial_impact > 0:
    decision = "PROCEED"
    decision_ar = "المضي في القرار"
    decision_class = "proceed"
    decision_text = (
        "السيناريو يحقق أثرًا ماليًا إيجابيًا وفق الافتراضات الحالية."
    )

elif score >= 50:
    decision = "REVIEW"
    decision_ar = "يحتاج مراجعة"
    decision_class = "review"
    decision_text = (
        "القرار قابل للتنفيذ، لكن الضغط على التكلفة أو الميزانية "
        "يتطلب مراجعة الافتراضات قبل الاعتماد."
    )

else:
    decision = "DO NOT PROCEED"
    decision_ar = "لا يُوصى بالقرار"
    decision_class = "reject"
    decision_text = (
        "الأثر المالي المتوقع لا يبرر التكلفة الإضافية وفق السيناريو الحالي."
    )


# =========================================================
# CSS
# =========================================================
st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: Inter, "Noto Sans Arabic", sans-serif;
}

.stApp {
    background: #f7f5f9;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* HERO */
.hero {
    background:
        linear-gradient(
            135deg,
            #25103d 0%,
            #421a61 48%,
            #70439a 100%
        );

    padding: 38px 42px;
    border-radius: 26px;

    color: white;

    box-shadow:
        0 18px 45px rgba(55, 24, 79, 0.20);

    margin-bottom: 28px;
}

.hero-eyebrow {
    font-size: 12px;
    letter-spacing: 2px;
    opacity: 0.70;
    font-weight: 600;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 42px;
    line-height: 1.1;
    font-weight: 800;
    margin: 0;
}

.hero-subtitle {
    font-family: "Noto Sans Arabic", sans-serif;
    font-size: 18px;
    margin-top: 14px;
    opacity: 0.90;
}

.hero-author {
    margin-top: 22px;
    font-size: 12px;
    opacity: 0.65;
}

/* Section */
.section-title {
    font-size: 22px;
    font-weight: 800;
    color: #292633;
    margin-top: 12px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #77727f;
    font-size: 13px;
    margin-bottom: 18px;
}

/* KPI */
.kpi {
    background: white;
    border: 1px solid #e9e3ed;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;

    box-shadow:
        0 8px 25px rgba(57, 27, 77, 0.055);
}

.kpi-label {
    font-family: "Noto Sans Arabic", sans-serif;
    color: #77727f;
    font-size: 12px;
}

.kpi-value {
    color: #292633;
    font-size: 28px;
    font-weight: 800;
    margin-top: 12px;
}

.kpi-en {
    color: #99939f;
    font-size: 11px;
    margin-top: 4px;
}

/* Panels */
.panel {
    background: white;
    border: 1px solid #e9e3ed;
    border-radius: 22px;
    padding: 24px;

    box-shadow:
        0 8px 25px rgba(57, 27, 77, 0.055);

    margin-bottom: 20px;
}

.panel-title {
    font-size: 20px;
    font-weight: 800;
    color: #292633;
}

.panel-subtitle {
    font-family: "Noto Sans Arabic", sans-serif;
    font-size: 12px;
    color: #817a88;
    margin-top: 5px;
    margin-bottom: 20px;
}

/* Decision */
.decision-card {
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
}

.decision-card.proceed {
    background: #eef8f3;
    border: 1px solid #c9e9d8;
}

.decision-card.review {
    background: #fbf6e9;
    border: 1px solid #eee0b7;
}

.decision-card.reject {
    background: #fceff1;
    border: 1px solid #efcdd3;
}

.decision-label {
    font-size: 11px;
    color: #77727f;
    letter-spacing: 1px;
}

.decision-title {
    font-size: 30px;
    font-weight: 800;
    margin-top: 7px;
}

.proceed .decision-title {
    color: #14784f;
}

.review .decision-title {
    color: #9a7215;
}

.reject .decision-title {
    color: #ae3949;
}

.decision-ar {
    font-family: "Noto Sans Arabic", sans-serif;
    font-size: 15px;
    margin-top: 3px;
    color: #4d4854;
}

.decision-text {
    font-family: "Noto Sans Arabic", sans-serif;
    font-size: 13px;
    color: #77727f;
    margin-top: 13px;
    line-height: 1.8;
}

/* Score */
.score-box {
    text-align: center;
    background: #f7f3fa;
    border-radius: 18px;
    padding: 18px;
    margin-top: 12px;
}

.score-number {
    color: #4B1F73;
    font-size: 46px;
    font-weight: 800;
}

.score-label {
    color: #77727f;
    font-size: 11px;
}

/* Impact */
.impact-card {
    background: #faf9fb;
    border: 1px solid #ebe5ee;
    border-radius: 16px;
    padding: 18px;
    min-height: 115px;
}

.impact-label {
    font-family: "Noto Sans Arabic", sans-serif;
    color: #77727f;
    font-size: 11px;
}

.impact-value {
    font-size: 22px;
    font-weight: 800;
    margin-top: 9px;
    color: #292633;
}

.positive {
    color: #14784f !important;
}

.negative {
    color: #ae3949 !important;
}

.purple {
    color: #4B1F73 !important;
}

/* Driver */
.driver {
    background: #faf9fb;
    border: 1px solid #ebe5ee;
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
}

.driver-title {
    font-size: 12px;
    color: #6f6976;
}

.driver-value {
    font-size: 18px;
    font-weight: 800;
    color: #292633;
    margin-top: 3px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 0;
    background: #4B1F73;
    color: white;
    font-weight: 700;
    min-height: 44px;
}

.stButton > button:hover {
    background: #361554;
    color: white;
}

/* Sliders */
.stSlider {
    padding-bottom: 5px;
}

/* Divider */
.soft-divider {
    height: 1px;
    background: #ebe5ee;
    margin: 20px 0;
}

/* Footer */
.footer {
    text-align: center;
    color: #99939f;
    font-size: 11px;
    padding: 20px;
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
        Financial Planning & Analysis | Decision Intelligence
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================
st.markdown(
    """
<div class="section-title">
    Executive Financial Overview
</div>

<div class="section-subtitle">
    نظرة تنفيذية سريعة على الوضع المالي الحالي قبل اتخاذ القرار.
</div>
""",
    unsafe_allow_html=True
)

kpis = st.columns(4)

kpi_data = [
    (
        "عدد الموظفين",
        f"{BASE_HEADCOUNT:,}",
        "Current Headcount"
    ),
    (
        "تكلفة القوى العاملة",
        f"{BASE_WORKFORCE_COST / 1e6:.2f}M",
        "Annual Workforce Cost"
    ),
    (
        "الإيرادات",
        f"{BASE_REVENUE / 1e6:.2f}M",
        "Annual Revenue"
    ),
    (
        "الميزانية",
        f"{BASE_BUDGET / 1e6:.2f}M",
        "Annual Budget"
    ),
]

for col, item in zip(kpis, kpi_data):

    label, value, english = item

    with col:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-en">{english}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# DECISION SCENARIO
# =========================================================
left, right = st.columns([0.85, 1.35], gap="large")


# =========================================================
# LEFT — DRIVERS
# =========================================================
with left:

    st.markdown(
        """
        <div class="panel">
            <div class="panel-title">
                Decision Drivers
            </div>

            <div class="panel-subtitle">
                محركات القرار التي يمكن للإدارة اختبارها.
            </div>
        """,
        unsafe_allow_html=True
    )

    st.slider(
        "الموظفون الجدد",
        min_value=-100,
        max_value=200,
        step=5,
        key="new_employees"
    )

    st.slider(
        "زيادة الرواتب %",
        min_value=0,
        max_value=20,
        step=1,
        key="salary_increase"
    )

    st.slider(
        "نمو الإيرادات %",
        min_value=-10,
        max_value=30,
        step=1,
        key="revenue_growth"
    )

    st.slider(
        "كفاءة التشغيل %",
        min_value=0,
        max_value=20,
        step=1,
        key="efficiency"
    )

    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

    st.button(
        "إعادة ضبط السيناريو",
        on_click=reset_scenario
    )

    st.markdown(
        """
        <div style="
            background:#f5f0f8;
            border-radius:14px;
            padding:14px;
            margin-top:15px;
            color:#6f6877;
            font-size:11px;
            line-height:1.8;
            font-family:'Noto Sans Arabic',sans-serif;
        ">
        غيّري الافتراضات وشاهدي كيف يتغير الأثر المالي
        والتوصية مباشرة.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# RIGHT — DECISION
# =========================================================
with right:

    st.markdown(
        """
        <div class="panel">
            <div class="panel-title">
                Decision Intelligence
            </div>

            <div class="panel-subtitle">
                تحويل الافتراضات إلى أثر مالي وتوصية تنفيذية.
            </div>
        """,
        unsafe_allow_html=True
    )

    # Decision card
    st.markdown(
        f"""
        <div class="decision-card {decision_class}">

            <div class="decision-label">
                RECOMMENDED DECISION
            </div>

            <div class="decision-title">
                {decision}
            </div>

            <div class="decision-ar">
                {decision_ar}
            </div>

            <div class="decision-text">
                {decision_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    score_col, pressure_col = st.columns(2)

    with score_col:
        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-number">
                    {score}
                </div>
                <div class="score-label">
                    DECISION SCORE / 100
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with pressure_col:

        pressure_class = (
            "negative"
            if budget_pressure > 100
            else "positive"
        )

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-number {pressure_class}">
                    {budget_pressure:.1f}%
                </div>
                <div class="score-label">
                    BUDGET PRESSURE
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# FINANCIAL IMPACT
# =========================================================
st.markdown(
    """
<div class="section-title">
    Financial Impact
</div>

<div class="section-subtitle">
    ماذا سيتغير ماليًا إذا تم تنفيذ السيناريو؟
</div>
""",
    unsafe_allow_html=True
)

impact_cols = st.columns(4)

impact_data = [
    (
        "الموظفون بعد القرار",
        f"{scenario_headcount:,}",
        "purple"
    ),
    (
        "التكلفة السنوية الجديدة",
        f"{scenario_workforce_cost / 1e6:.2f}M",
        "purple"
    ),
    (
        "أثر الإيرادات",
        f"{revenue_impact:,.0f}",
        "positive" if revenue_impact >= 0 else "negative"
    ),
    (
        "الأثر المالي الصافي",
        f"{net_financial_impact:,.0f}",
        "positive" if net_financial_impact >= 0 else "negative"
    ),
]

for col, item in zip(impact_cols, impact_data):

    label, value, cls = item

    with col:
        st.markdown(
            f"""
            <div class="impact-card">
                <div class="impact-label">{label}</div>
                <div class="impact-value {cls}">
                    {value}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# BEFORE VS AFTER
# =========================================================
before_col, after_col = st.columns(2, gap="large")


with before_col:

    st.markdown(
        """
        <div class="panel">
            <div class="panel-title">
                Current State
            </div>

            <div class="panel-subtitle">
                الوضع المالي الحالي.
            </div>
        """,
        unsafe_allow_html=True
    )

    current_items = [
        ("Headcount", f"{BASE_HEADCOUNT:,}"),
        ("Workforce Cost", f"{BASE_WORKFORCE_COST / 1e6:.2f}M SAR"),
        ("Revenue", f"{BASE_REVENUE / 1e6:.2f}M SAR"),
        ("Budget", f"{BASE_BUDGET / 1e6:.2f}M SAR"),
    ]

    for label, value in current_items:
        st.markdown(
            f"""
            <div class="driver">
                <div class="driver-title">{label}</div>
                <div class="driver-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


with after_col:

    st.markdown(
        """
        <div class="panel">
            <div class="panel-title">
                Scenario State
            </div>

            <div class="panel-subtitle">
                الوضع المتوقع بعد تنفيذ القرار.
            </div>
        """,
        unsafe_allow_html=True
    )

    scenario_items = [
        ("Headcount", f"{scenario_headcount:,}"),
        (
            "Workforce Cost",
            f"{scenario_workforce_cost / 1e6:.2f}M SAR"
        ),
        (
            "Revenue",
            f"{scenario_revenue / 1e6:.2f}M SAR"
        ),
        (
            "Cost / Employee / Month",
            f"{cost_per_employee:,.0f} SAR"
        ),
    ]

    for label, value in scenario_items:
        st.markdown(
            f"""
            <div class="driver">
                <div class="driver-title">{label}</div>
                <div class="driver-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# BRIDGE
# =========================================================
st.markdown(
    """
<div class="section-title">
    Financial Impact Bridge
</div>

<div class="section-subtitle">
    كيف انتقلنا من الوضع الحالي إلى الأثر المالي للقرار؟
</div>
""",
    unsafe_allow_html=True
)

bridge = pd.DataFrame(
    {
        "الأثر المالي": [
            "أثر الإيرادات",
            "الزيادة في التكلفة",
            "الأثر الصافي"
        ],
        "SAR": [
            revenue_impact,
            -incremental_cost,
            net_financial_impact
        ]
    }
)

st.bar_chart(
    bridge.set_index("الأثر المالي"),
    use_container_width=True
)


# =========================================================
# DECISION RATIONALE
# =========================================================
st.markdown(
    """
<div class="section-title">
    Decision Rationale
</div>

<div class="section-subtitle">
    لماذا وصل المحرك إلى هذه التوصية؟
</div>
""",
    unsafe_allow_html=True
)

reasons = []

if revenue_growth > 0:
    reasons.append(
        f"نمو الإيرادات المتوقع يبلغ {revenue_growth}%، "
        "مما يدعم الأثر المالي."
    )

if salary_increase > 0:
    reasons.append(
        f"زيادة الرواتب بنسبة {salary_increase}% "
        "ترفع تكلفة القوى العاملة."
    )

if new_employees > 0:
    reasons.append(
        f"إضافة {new_employees:,} موظف ترفع قاعدة التكلفة السنوية."
    )

if new_employees < 0:
    reasons.append(
        f"خفض القوى العاملة بمقدار {abs(new_employees):,} "
        "يخفض الضغط على التكلفة."
    )

if efficiency > 0:
    reasons.append(
        f"تحسين الكفاءة بنسبة {efficiency}% "
        "يخفف الأثر الصافي للتكلفة."
    )

if budget_pressure > 100:
    reasons.append(
        f"التكلفة المتوقعة تستخدم {budget_pressure:.1f}% "
        "من الميزانية المحددة."
    )
else:
    reasons.append(
        f"التكلفة المتوقعة تقع عند {budget_pressure:.1f}% "
        "من الميزانية المحددة."
    )

if not reasons:
    reasons.append(
        "لا توجد تغييرات جوهرية عن الوضع الحالي."
    )

for reason in reasons:

    st.markdown(
        f"""
        <div class="driver">
            <div class="driver-title">
                ● {reason}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SCENARIO SUMMARY
# =========================================================
st.markdown(
    """
<div class="panel">

<div class="panel-title">
Scenario Summary
</div>

<div class="panel-subtitle">
الافتراضات الحالية المستخدمة في القرار.
</div>

""",
    unsafe_allow_html=True
)

summary = pd.DataFrame(
    {
        "Decision Driver": [
            "New Employees",
            "Salary Increase",
            "Revenue Growth",
            "Operational Efficiency"
        ],
        "Current Scenario": [
            f"{new_employees:+}",
            f"{salary_increase}%",
            f"{revenue_growth}%",
            f"{efficiency}%"
        ]
    }
)

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
<div class="footer">
    Financial Decision Engine · Financial Planning & Analysis · MVP
    <br>
    From Data → Financial Impact → Decision
</div>
""",
    unsafe_allow_html=True
)
