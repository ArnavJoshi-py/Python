# ---------------------------------------------
# Tax Calculator Web App using Streamlit
# Concept: Direct Taxation & Progressive Tax
# ---------------------------------------------
pip install streamlit numpy matplotlib
streamlit run app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(page_title="Tax Calculator", layout="centered")

st.title("💰 Tax Calculator Web App")
st.write(
    """
    Compare tax liability under:
    - Old Tax Regime
    - New Tax Regime
    - Flat Tax System
    (Includes 4% Health & Education Cess)
    """
)

# -------------------------------
# TAX CALCULATION FUNCTIONS
# -------------------------------

# Old Tax Regime (simplified slabs)
def old_regime_tax(income):
    tax = 0

    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30

    return tax


# New Tax Regime (simplified slabs)
def new_regime_tax(income):
    tax = 0

    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 15000 + (income - 600000) * 0.10
    elif income <= 1200000:
        tax = 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = 90000 + (income - 1200000) * 0.20
    else:
        tax = 150000 + (income - 1500000) * 0.30

    return tax


# Flat Tax System (example: 20%)
def flat_tax(income, rate=0.20):
    return income * rate


# Add 4% Health & Education Cess
def add_cess(tax):
    return tax * 1.04


# Effective Tax Rate
def effective_rate(tax, income):
    if income == 0:
        return 0
    return (tax / income) * 100


# -------------------------------
# USER INPUT
# -------------------------------
income = st.number_input(
    "Enter Annual Income (₹)",
    min_value=0,
    step=50000,
    value=500000
)

# -------------------------------
# CALCULATIONS
# -------------------------------
old_tax = add_cess(old_regime_tax(income))
new_tax = add_cess(new_regime_tax(income))
flat_tax_value = add_cess(flat_tax(income))

tax_data = {
    "Old Regime": old_tax,
    "New Regime": new_tax,
    "Flat Tax": flat_tax_value
}

lowest_regime = min(tax_data, key=tax_data.get)

# -------------------------------
# DISPLAY RESULTS
# -------------------------------
st.subheader("📊 Tax Summary")

st.write(f"**Old Regime Tax:** ₹ {old_tax:,.2f}")
st.write(f"**New Regime Tax:** ₹ {new_tax:,.2f}")
st.write(f"**Flat Tax:** ₹ {flat_tax_value:,.2f}")

st.success(f"✅ Lowest Tax Payable Under: **{lowest_regime}**")

# Effective Rates
st.subheader("Effective Tax Rates")

st.write(
    f"""
    Old Regime: {effective_rate(old_tax, income):.2f}%  
    New Regime: {effective_rate(new_tax, income):.2f}%  
    Flat Tax: {effective_rate(flat_tax_value, income):.2f}%
    """
)

# -------------------------------
# GRAPH 1: Income vs Total Tax
# -------------------------------
income_range = np.linspace(100000, 2000000, 50)

old_list = [add_cess(old_regime_tax(i)) for i in income_range]
new_list = [add_cess(new_regime_tax(i)) for i in income_range]
flat_list = [add_cess(flat_tax(i)) for i in income_range]

fig1, ax1 = plt.subplots()
ax1.plot(income_range, old_list, label="Old Regime")
ax1.plot(income_range, new_list, label="New Regime")
ax1.plot(income_range, flat_list, label="Flat Tax")

ax1.set_xlabel("Income")
ax1.set_ylabel("Total Tax")
ax1.set_title("Income vs Total Tax")
ax1.legend()

st.pyplot(fig1)

# -------------------------------
# GRAPH 2: Effective Tax Rate
# -------------------------------
old_rate = [(add_cess(old_regime_tax(i)) / i) * 100 for i in income_range]
new_rate = [(add_cess(new_regime_tax(i)) / i) * 100 for i in income_range]
flat_rate = [(add_cess(flat_tax(i)) / i) * 100 for i in income_range]

fig2, ax2 = plt.subplots()
ax2.plot(income_range, old_rate, label="Old Regime")
ax2.plot(income_range, new_rate, label="New Regime")
ax2.plot(income_range, flat_rate, label="Flat Tax")

ax2.set_xlabel("Income")
ax2.set_ylabel("Effective Tax Rate (%)")
ax2.set_title("Income vs Effective Tax Rate")
ax2.legend()

st.pyplot(fig2)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Python for Economics Lab | Streamlit Tax Calculator")
