
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Financial Decision Engine",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# Demo baseline from our Excel
# ----------------------------
BASE_HEADCOUNT = 500
AVG_MONTHLY_COST = 16936.05
BASE_PAYROLL = BASE_HEADCOUNT * AVG_MONTHLY_COST * 12
BASE_REVENUE = 120_000_000
BASE_BUDGET = 77_000_000

# ----------------------------
# Styling
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: Inter, "Noto Sans Arabic", sans-serif;
}
.stApp {
    background: #f7f4f9;
}
.hero {
    background: linear-gradient(135deg,#2e124a,#4B1F73 65%,#74499a);
    color: white;
    padding: 28px 32px;
    border-radius: 0 0 24px 24px;
    margin-bottom: 22px;
}
.hero h1 {margin:0;font-size:32px;font-weight:800;}
.hero p {margin:7px 0 0;opacity:.86;}
.eyebrow {font-size:11px;letter-spacing:1px;opacity:.72;margin-bottom:7px;}
.card {
    background:white;
    border:1px solid #e8e1ed;
    border-radius:18px;
    padding:18px;
    box-shadow:0 8px 24px rgba(48,18,77,.06);
    min-height:115px;
}
.card-label {color:#77717e;font-size:12px;}
.card-value {font-size:25px;font-weight:800;margin-top:8px;}
.card-sub {color:#77717e;font-size:11px;margin-top:4px;}
.panel {
    background:white;
    border:1px solid #e8e1ed;
    border-radius:20px;
    padding:22px;
    box-shadow:0 8px 24px rgba(48,18,77,.06);
}
.panel-title {font-size:20px;font-weight:800;margin-bottom:3px;}
.panel-sub {font-size:12px;color:#77717e;margin-bottom:15px;}
.result {
    background:#faf8fb;
    border:1px solid #e8e1ed;
    border-radius:15px;
    padding:15px;
    min-height:90px;
}
.result-label {font-size:11px;color:#77717e;}
.result-value {font-size:21px;font-weight:800;margin-top:7px;}
.good {color:#14845b;}
.bad {color:#b33d4a;}
.neutral {color:#4B1F73;}
.decision {
    border-radius:16px;
    padding:16px;
    background:#f2edf6;
    margin-top:14px;
}
.stButton > button {
    width:100%;
    border-radius:12px;
    border:0;
    background:#4B1F73;
    color:white;
    font-weight:700;
    padding:10px 16px;
}
section[data-testid="stSidebar"] {background:#fff;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">FINANCIAL DECISION INTELLIGENCE</div>
  <h1>Financial Decision Engine</h1>
  <p>من البيانات → الأثر المالي → القرار</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Top KPIs
# ----------------------------
cols = st.columns(4)
kpis = [
    ("عدد الموظفين", f"{BASE_HEADCOUNT:,}", "Current Headcount"),
    ("تكلفة القوى العاملة السنوية", f"{BASE_PAYROLL/1e6:.2f}M", "Annual Workforce Cost"),
    ("الميزانية السنوية", f"{BASE_BUDGET/1e6:.2f}M", "Annual Budget"),
    ("متوسط تكلفة الموظف شهريًا", f"{AVG_MONTHLY_COST:,.0f}", "SAR / Employee / Month"),
]
for col, (label, value, sub) in zip(cols, kpis):
    with col:
        st.markdown(
            f'<div class="card"><div class="card-label">{label}</div>'
            f'<div class="card-value">{value}</div><div class="card-sub">{sub}</div></div>',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------
# Scenario controls
# ----------------------------
left, right = st.columns([0.9, 1.5], gap="large")

with left:
    st.markdown('<div class="panel"><div class="panel-title">محركات القرار</div>'
                '<div class="panel-sub">غيّري الافتراضات وشاهدي الأثر المالي فورًا.</div>',
                unsafe_allow_html=True)

    new_employees = st.slider("الموظفون الجدد", -100, 200, 0, step=5)
    salary_increase = st.slider("زيادة الرواتب", 0, 20, 0, step=1)
    revenue_growth = st.slider("نمو الإيرادات", -10, 30, 0, step=1)
    efficiency = st.slider("كفاءة التشغيل", 0, 20, 0, step=1)

    reset = st.button("إعادة ضبط السيناريو")
    if reset:
        st.rerun()

    st.markdown(
        '<div style="background:#f4eff7;border-radius:14px;padding:12px;'
        'font-size:11px;color:#645b69;line-height:1.7;margin-top:12px">'
        'هذه نسخة MVP ببيانات افتراضية. لاحقًا نربطها ببيانات العميل الفعلية، '
        'ونضيف حفظ السيناريوهات والتقارير وتعدد المستخدمين.'
        '</div></div>',
        unsafe_allow_html=True
    )

# ----------------------------
# Engine
# ----------------------------
hc = BASE_HEADCOUNT + new_employees
payroll = AVG_MONTHLY_COST * hc * 12 * (1 + salary_increase/100) * (1 - efficiency/100)
revenue = BASE_REVENUE * (1 + revenue_growth/100)
incremental_cost = payroll - BASE_PAYROLL
revenue_delta = revenue - BASE_REVENUE
net_impact = revenue_delta - incremental_cost
budget_ratio = payroll / BASE_BUDGET * 100

if net_impact > 1_000_000:
    decision = "قرار إيجابي مبدئي"
    explanation = "الأثر المالي المتوقع موجب وفق الافتراضات الحالية."
    decision_class = "good"
elif net_impact < -1_000_000:
    decision = "يحتاج مراجعة"
    explanation = "الزيادة في التكلفة تتجاوز الأثر المالي المتوقع."
    decision_class = "bad"
else:
    decision = "محايد"
    explanation = "السيناريو قريب من الوضع الحالي ويحتاج تقييمًا إضافيًا."
    decision_class = "neutral"

with right:
    st.markdown('<div class="panel"><div class="panel-title">الأثر المالي للقرار</div>'
                '<div class="panel-sub">النتيجة تتغير مباشرة مع كل افتراض.</div>',
                unsafe_allow_html=True)

    r1 = st.columns(3)
    result_data = [
        ("الموظفون بعد القرار", f"{hc:,}"),
        ("التكلفة السنوية الجديدة", f"{payroll/1e6:.2f}M"),
        ("الزيادة في التكلفة", f"{incremental_cost:,.0f} SAR"),
        ("الإيرادات المتوقعة", f"{revenue/1e6:.2f}M"),
        ("الأثر المالي الصافي", f"{net_impact:,.0f} SAR"),
        ("التكلفة مقابل الميزانية", f"{budget_ratio:.1f}%"),
    ]
    for i, (label, value) in enumerate(result_data):
        with r1[i % 3]:
            cls = ""
            if label == "الأثر المالي الصافي":
                cls = decision_class
            st.markdown(
                f'<div class="result"><div class="result-label">{label}</div>'
                f'<div class="result-value {cls}">{value}</div></div>',
                unsafe_allow_html=True
            )

    st.markdown(
        f'<div class="decision"><strong class="{decision_class}">{decision}</strong>'
        f'<div style="font-size:12px;color:#77717e;margin-top:5px">{explanation}</div></div>',
        unsafe_allow_html=True
    )

    st.markdown("**التكلفة مقابل الميزانية**")
    st.progress(min(max(budget_ratio / 100, 0), 1))
    st.caption(f"{payroll/1e6:.2f}M SAR مقابل ميزانية {BASE_BUDGET/1e6:.2f}M SAR — {budget_ratio:.1f}%")

    compare = pd.DataFrame({
        "المؤشر": ["Headcount", "Annual Cost", "Revenue", "Net Impact"],
        "الحالي": [f"{BASE_HEADCOUNT:,}", f"{BASE_PAYROLL/1e6:.2f}M", f"{BASE_REVENUE/1e6:.2f}M", "0"],
        "السيناريو": [f"{hc:,}", f"{payroll/1e6:.2f}M", f"{revenue/1e6:.2f}M", f"{net_impact:,.0f}"],
        "التغير": [f"{new_employees:+,}", f"{incremental_cost:,.0f}", f"{revenue_delta:,.0f}", f"{net_impact:,.0f}"]
    })
    st.dataframe(compare, use_container_width=True, hide_index=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Simple visual insight
# ----------------------------
st.markdown("<br>", unsafe_allow_html=True)
a, b = st.columns(2)

with a:
    st.markdown('<div class="panel"><div class="panel-title">Financial Impact Bridge</div>'
                '<div class="panel-sub">مكونات التغير في الأثر المالي.</div>', unsafe_allow_html=True)
    bridge = pd.DataFrame({
        "Component": ["Revenue Impact", "Incremental Cost", "Net Impact"],
        "SAR": [revenue_delta, -incremental_cost, net_impact]
    }).set_index("Component")
    st.bar_chart(bridge)
    st.markdown("</div>", unsafe_allow_html=True)

with b:
    st.markdown('<div class="panel"><div class="panel-title">Scenario Snapshot</div>'
                '<div class="panel-sub">الافتراضات المستخدمة حاليًا.</div>', unsafe_allow_html=True)
    snapshot = pd.DataFrame({
        "Driver": ["New Employees", "Salary Increase", "Revenue Growth", "Efficiency"],
        "Value": [f"{new_employees:+}", f"{salary_increase}%", f"{revenue_growth}%", f"{efficiency}%"]
    })
    st.dataframe(snapshot, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("Financial Decision Engine — MVP | Demo data")
