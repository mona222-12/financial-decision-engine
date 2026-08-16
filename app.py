import streamlit as st
import pandas as pd

# ============================================================
# FINANCIAL DECISION ENGINE
# Executive Financial Planning & Analysis
# ============================================================

st.set_page_config(
    page_title="Financial Decision Engine",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# BASELINE
# ============================================================

BASE_HEADCOUNT = 500
AVG_MONTHLY_COST = 16936.05

BASE_WORKFORCE_COST = (
    BASE_HEADCOUNT
    * AVG_MONTHLY_COST
    * 12
)

BASE_REVENUE = 120_000_000
BASE_BUDGET = 77_000_000

# ============================================================
# SESSION STATE
# ============================================================

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0


# ============================================================
# FORMATTING
# ============================================================

def money_m(value):
    return f"{value / 1_000_000:,.2f}M"

def money_full(value):
    return f"{value:,.0f} SAR"

def pct(value):
    return f"{value:.1f}%"

def signed_money(value):
    if value > 0:
        return f"+{value:,.0f} SAR"
    elif value < 0:
        return f"{value:,.0f} SAR"
    return "0 SAR"


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family:
        Inter,
        "Noto Sans Arabic",
        Arial,
        sans-serif;
}

.stApp {
    background: #f7f5f9;
}

/* Remove Streamlit top spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* HERO */

.hero {
    background:
        linear-gradient(
            135deg,
            #251039 0%,
            #4B1F73 52%,
            #76509A 100%
        );

    border-radius: 28px;

    padding: 42px 44px 38px 44px;

    color: white;

    margin-bottom: 28px;

    box-shadow:
        0 18px 45px rgba(57, 25, 86, 0.20);
}

.hero-eyebrow {
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 600;
    opacity: 0.72;
    margin-bottom: 14px;
}

.hero-title {
    font-size: 42px;
    line-height: 1.1;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero-subtitle {
    font-family:
        "Noto Sans Arabic",
        Arial,
        sans-serif;

    font-size: 18px;
    font-weight: 500;
    opacity: 0.92;
}

.hero-author {
    margin-top: 25px;
    font-size: 12px;
    letter-spacing: 1px;
    opacity: 0.65;
}

/* SECTION */

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #282531;
    margin-top: 8px;
}

.section-subtitle {
    color: #77717f;
    font-size: 13px;
    margin-bottom: 18px;
}

/* KPI */

.kpi {
    background: white;
    border: 1px solid #e8e1ed;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;

    box-shadow:
        0 8px 25px rgba(53, 27, 75, 0.06);
}

.kpi-label {
    color: #817989;
    font-size: 13px;
    margin-bottom: 12px;
}

.kpi-value {
    color: #292633;
    font-size: 29px;
    font-weight: 800;
}

.kpi-sub {
    color: #9a94a1;
    font-size: 11px;
    margin-top: 8px;
}

/* PANELS */

.panel {
    background: white;
    border: 1px solid #e8e1ed;
    border-radius: 22px;

    padding: 25px;

    box-shadow:
        0 8px 25px rgba(53, 27, 75, 0.06);
}

.panel-title {
    color: #292633;
    font-size: 20px;
    font-weight: 800;
}

.panel-subtitle {
    color: #817989;
    font-size: 12px;
    margin-top: 4px;
    margin-bottom: 20px;
}

/* RESULT */

.result {
    background: #faf9fb;
    border: 1px solid #ece6ef;
    border-radius: 16px;
    padding: 16px;
    min-height: 100px;
}

.result-label {
    color: #817989;
    font-size: 11px;
}

.result-value {
    color: #2d2935;
    font-size: 21px;
    font-weight: 800;
    margin-top: 8px;
}

.positive {
    color: #15845b !important;
}

.negative {
    color: #b13b4b !important;
}

.purple {
    color: #4B1F73 !important;
}

/* DECISION */

.decision-box {
    border-radius: 18px;
    padding: 20px;
    margin-top: 20px;

    background:
        linear-gradient(
            135deg,
            #f4eff7,
            #faf8fb
        );

    border: 1px solid #e5dbea;
}

.decision-label {
    color: #817989;
    font-size: 11px;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.decision-title {
    font-size: 24px;
    font-weight: 800;
}

.decision-text {
    color: #77717f;
    font-size: 12px;
    margin-top: 6px;
    line-height: 1.7;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;

    background: #4B1F73;
    color: white;

    font-weight: 700;
    min-height: 44px;
}

.stButton > button:hover {
    background: #351452;
    color: white;
}

/* SLIDERS */

.stSlider > div > div > div > div {
    background: #4B1F73;
}

/* TABLE */

.dataframe {
    border-radius: 12px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #96909d;
    font-size: 11px;
    padding: 25px 0 5px 0;
}

/* MOBILE */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 30px 24px;
        border-radius: 22px;
    }

    .hero-title {
        font-size: 31px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

    .kpi {
        min-height: 125px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">

    <div class="hero-eyebrow">
        FINANCIAL DECISION INTELLIGENCE
    </div>

    <div class="hero-title">
        Financial Decision Engine
    </div>

    <div class="hero-subtitle" dir="rtl">
        من البيانات → الأثر المالي → القرار
    </div>

    <div class="hero-author">
        FINANCIAL PLANNING & ANALYSIS
    </div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.markdown(
    """
<div class="section-title">
    Executive Financial Overview
</div>

<div class="section-subtitle" dir="rtl">
    نظرة تنفيذية سريعة على الوضع المالي الحالي قبل اتخاذ القرار.
</div>
""",
    unsafe_allow_html=True
)


k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-label">عدد الموظفين</div>
            <div class="kpi-value">{BASE_HEADCOUNT:,}</div>
            <div class="kpi-sub">Current Headcount</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k2:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-label">تكلفة القوى العاملة السنوية</div>
            <div class="kpi-value">{money_m(BASE_WORKFORCE_COST)}</div>
            <div class="kpi-sub">Annual Workforce Cost</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k3:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-label">الميزانية السنوية</div>
            <div class="kpi-value">{money_m(BASE_BUDGET)}</div>
            <div class="kpi-sub">Annual Budget</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k4:
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-label">متوسط تكلفة الموظف شهريًا</div>
            <div class="kpi-value">{AVG_MONTHLY_COST:,.0f}</div>
            <div class="kpi-sub">SAR / Employee / Month</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# DECISION ENGINE
# ============================================================

left, right = st.columns([0.85, 1.55], gap="large")


# ============================================================
# LEFT — DRIVERS
# ============================================================

with left:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Decision Drivers
            </div>

            <div class="panel-subtitle" dir="rtl">
                غيّري الافتراضات وشاهدي الأثر المالي للقرار فورًا.
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
        step=1
    )

    revenue_growth = st.slider(
        "نمو الإيرادات",
        min_value=-10,
        max_value=30,
        value=0,
        step=1
    )

    efficiency = st.slider(
        "كفاءة التشغيل",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    st.markdown("<br>", unsafe_allow_html=True)

    reset = st.button("إعادة ضبط السيناريو")

    if reset:
        st.rerun()

    st.markdown(
        """
        <div style="
            background:#f5f0f7;
            border-radius:14px;
            padding:14px;
            margin-top:15px;
            color:#6f6877;
            font-size:11px;
            line-height:1.8;
        " dir="rtl">

        <b>منهجية المحرك</b><br>
        يتم تحويل كل افتراض إلى أثر مالي،
        ثم مقارنة الأثر بالوضع الحالي للوصول
        إلى إشارة قرار أولية.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CALCULATIONS
# ============================================================

headcount = BASE_HEADCOUNT + new_employees

salary_factor = 1 + (salary_increase / 100)

efficiency_factor = 1 - (efficiency / 100)

annual_workforce_cost = (
    headcount
    * AVG_MONTHLY_COST
    * 12
    * salary_factor
    * efficiency_factor
)

revenue = (
    BASE_REVENUE
    * (1 + revenue_growth / 100)
)

incremental_cost = (
    annual_workforce_cost
    - BASE_WORKFORCE_COST
)

revenue_impact = (
    revenue
    - BASE_REVENUE
)

net_impact = (
    revenue_impact
    - incremental_cost
)

budget_usage = (
    annual_workforce_cost
    / BASE_BUDGET
    * 100
)

budget_gap = (
    BASE_BUDGET
    - annual_workforce_cost
)


# ============================================================
# DECISION LOGIC
# ============================================================

if net_impact > 1_000_000:

    decision = "قرار إيجابي مبدئي"
    decision_class = "positive"

    explanation = (
        "الأثر المالي المتوقع موجب، "
        "ما يشير إلى أن السيناريو قد يخلق قيمة مالية "
        "وفق الافتراضات الحالية."
    )

elif net_impact < -1_000_000:

    decision = "يحتاج مراجعة"
    decision_class = "negative"

    explanation = (
        "الأثر المالي المتوقع سالب، "
        "لذلك تحتاج الإدارة إلى مراجعة التكلفة "
        "أو الافتراضات قبل اعتماد القرار."
    )

else:

    decision = "محايد"

    decision_class = "purple"

    explanation = (
        "الأثر المالي قريب من نقطة التعادل، "
        "ويحتاج القرار إلى تحليل إضافي قبل الاعتماد."
    )


# ============================================================
# RIGHT — IMPACT
# ============================================================

with right:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Financial Impact
            </div>

            <div class="panel-subtitle" dir="rtl">
                كيف يتغير الوضع المالي إذا تم تنفيذ السيناريو؟
            </div>

        """,
        unsafe_allow_html=True
    )

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    الموظفون بعد القرار
                </div>

                <div class="result-value purple">
                    {headcount:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r2:
        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    التكلفة السنوية الجديدة
                </div>

                <div class="result-value">
                    {money_m(annual_workforce_cost)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r3:
        cost_class = "negative" if incremental_cost > 0 else "positive"

        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    التغير في التكلفة
                </div>

                <div class="result-value {cost_class}">
                    {signed_money(incremental_cost)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    r4, r5, r6 = st.columns(3)

    with r4:
        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    الإيرادات المتوقعة
                </div>

                <div class="result-value">
                    {money_m(revenue)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r5:

        revenue_class = (
            "positive"
            if revenue_impact > 0
            else "negative"
        )

        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    أثر الإيرادات
                </div>

                <div class="result-value {revenue_class}">
                    {signed_money(revenue_impact)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r6:

        st.markdown(
            f"""
            <div class="result">
                <div class="result-label">
                    استخدام الميزانية
                </div>

                <div class="result-value purple">
                    {budget_usage:.1f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # DECISION
    # ========================================================

    st.markdown(
        f"""
        <div class="decision-box">

            <div class="decision-label">
                DECISION SIGNAL
            </div>

            <div class="decision-title {decision_class}">
                {decision}
            </div>

            <div class="decision-text" dir="rtl">
                {explanation}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # BUDGET
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "**Budget Utilization**"
    )

    st.progress(
        min(max(budget_usage / 100, 0), 1)
    )

    if budget_gap >= 0:

        st.caption(
            f"{money_m(annual_workforce_cost)} "
            f"مقابل ميزانية {money_m(BASE_BUDGET)} "
            f"— المتبقي {money_m(budget_gap)}"
        )

    else:

        st.caption(
            f"{money_m(annual_workforce_cost)} "
            f"مقابل ميزانية {money_m(BASE_BUDGET)} "
            f"— تجاوز {money_m(abs(budget_gap))}"
        )


    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FINANCIAL BRIDGE
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
        Financial Decision Bridge
    </div>

    <div class="section-subtitle" dir="rtl">
        من أين جاء الأثر المالي للقرار؟
    </div>
    """,
    unsafe_allow_html=True
)


bridge_left, bridge_right = st.columns([1.25, 0.75], gap="large")


with bridge_left:

    bridge = pd.DataFrame(
        {
            "الأثر": [
                "Revenue Impact",
                "Incremental Cost",
                "Net Impact"
            ],
            "SAR": [
                revenue_impact,
                -incremental_cost,
                net_impact
            ]
        }
    )

    st.bar_chart(
        bridge.set_index("الأثر"),
        use_container_width=True
    )


with bridge_right:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Decision Summary
            </div>

            <div class="panel-subtitle" dir="rtl">
                الخلاصة المالية للسيناريو الحالي.
            </div>

        """,
        unsafe_allow_html=True
    )

    summary = pd.DataFrame(
        {
            "Metric": [
                "Headcount",
                "Workforce Cost",
                "Revenue",
                "Net Impact"
            ],

            "Current": [
                f"{BASE_HEADCOUNT:,}",
                money_m(BASE_WORKFORCE_COST),
                money_m(BASE_REVENUE),
                "0 SAR"
            ],

            "Scenario": [
                f"{headcount:,}",
                money_m(annual_workforce_cost),
                money_m(revenue),
                signed_money(net_impact)
            ]
        }
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        f"""
        <div style="
            margin-top:15px;
            padding:14px;
            border-radius:14px;
            background:#f7f3f9;
        ">

        <div style="
            color:#817989;
            font-size:11px;
        ">
        NET FINANCIAL IMPACT
        </div>

        <div class="{decision_class}"
             style="
                font-size:24px;
                font-weight:800;
                margin-top:5px;
             ">
            {signed_money(net_impact)}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# SCENARIO SNAPSHOT
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

s1, s2 = st.columns(2, gap="large")


with s1:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Scenario Assumptions
            </div>

            <div class="panel-subtitle" dir="rtl">
                الافتراضات التي بُني عليها القرار.
            </div>

        """,
        unsafe_allow_html=True
    )

    assumptions = pd.DataFrame(
        {
            "Driver": [
                "New Employees",
                "Salary Increase",
                "Revenue Growth",
                "Efficiency"
            ],

            "Selected": [
                f"{new_employees:+,}",
                f"{salary_increase}%",
                f"{revenue_growth}%",
                f"{efficiency}%"
            ]
        }
    )

    st.dataframe(
        assumptions,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


with s2:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Management Insight
            </div>

            <div class="panel-subtitle" dir="rtl">
                ماذا تعني الأرقام لصانع القرار؟
            </div>

        """,
        unsafe_allow_html=True
    )

    if net_impact > 1_000_000:

        insight = (
            "السيناريو يحقق أثرًا ماليًا موجبًا. "
            "قبل الاعتماد النهائي، يجب اختبار استدامة نمو الإيرادات "
            "ومدى قدرة الكفاءة التشغيلية على دعم النتيجة."
        )

    elif net_impact < -1_000_000:

        insight = (
            "السيناريو يخلق ضغطًا ماليًا. "
            "يمكن تحسين النتيجة عبر خفض الزيادة في التكلفة، "
            "رفع الكفاءة، أو إعادة تقييم مستهدفات الإيرادات."
        )

    else:

        insight = (
            "السيناريو قريب من نقطة التعادل. "
            "يفضل اختبار سيناريوهات بديلة قبل اتخاذ القرار النهائي."
        )

    st.markdown(
        f"""
        <div style="
            background:#f7f3f9;
            border-left:4px solid #4B1F73;
            padding:18px;
            border-radius:12px;
            color:#5f5966;
            font-size:13px;
            line-height:1.9;
        " dir="rtl">

        {insight}

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

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
