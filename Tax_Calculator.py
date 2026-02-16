import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# PAGE SETTINGS
# --------------------------------
st.set_page_config(page_title="Tax Calculator", layout="wide")

st.title("💰 Tax Calculator Web App")
st.write("Comparison of Old Regime, New Regime and Flat Tax System")

CESS = 0.04  # 4% cess

# --------------------------------
# INPUT
# --------------------------------
income = st.number_input(
    "Enter Annual Income (₹)",
    min_value=0,
    value=500000,
    step=50000
)

# --------------------------------
# OLD TAX REGIME
# --------------------------------
def old_tax(income):
    tax = 0

    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30

    return tax * (1 + CESS)


# --------------------------------
# NEW TAX REGIME
# --------------------------------
def new_tax(income):

    slabs = [
        (300000, 0),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float("inf"), 0.30),
    ]

    tax = 0
    remaining = income

    for slab, rate in slabs:
        taxable = min(remaining, slab)
        tax += taxable * rate
        remaining -= taxable
        if remaining <= 0:
            break

    return tax * (1 + CESS)


# --------------------------------
# FLAT TAX
# --------------------------------
def flat_tax(income, rate=0.20):
    return income * rate * (1 + CESS)


# --------------------------------
# EFFECTIVE TAX RATE
# --------------------------------
def effective_rate(tax, income):
    return (tax / income * 100) if income > 0 else 0


# --------------------------------
# CALCULATIONS
# --------------------------------
old_val = old_tax(income)
new_val = new_tax(income)
flat_val = flat_tax(income)

st.header("📊 Tax Summary")

st.write(f"Old Regime Tax: ₹ {old_val:,.2f}")
st.write(f"New Regime Tax: ₹ {new_val:,.2f}")
st.write(f"Flat Tax (20%): ₹ {flat_val:,.2f}")

best = min(
    {"Old Regime": old_val, "New Regime": new_val, "Flat Tax": flat_val},
    key=lambda x: {"Old Regime": old_val,
                   "New Regime": new_val,
                   "Flat Tax": flat_val}[x]
)

st.success(f"✅ Lowest Tax Payable Under: {best}")

# --------------------------------
# GRAPH DATA
# --------------------------------
income_range = np.linspace(100000, 2000000, 60)

old_taxes = [old_tax(i) for i in income_range]
new_taxes = [new_tax(i) for i in income_range]
flat_taxes = [flat_tax(i) for i in income_range]

old_rates = [effective_rate(old_tax(i), i) for i in income_range]
new_rates = [effective_rate(new_tax(i), i) for i in income_range]
flat_rates = [effective_rate(flat_tax(i), i) for i in income_range]

# --------------------------------
# GRAPH 1
# --------------------------------
st.header("📈 Graph 1: Income vs Total Tax")

fig1, ax1 = plt.subplots()
ax1.plot(income_range, old_taxes, label="Old Regime")
ax1.plot(income_range, new_taxes, label="New Regime")
ax1.plot(income_range, flat_taxes, label="Flat Tax")

ax1.set_xlabel("Income (₹)")
ax1.set_ylabel("Total Tax (₹)")
ax1.legend()
ax1.grid(True)

st.pyplot(fig1)

# --------------------------------
# GRAPH 2
# --------------------------------
st.header("📉 Graph 2: Effective Tax Rate")

fig2, ax2 = plt.subplots()
ax2.plot(income_range, old_rates, label="Old Regime")
ax2.plot(income_range, new_rates, label="New Regime")
ax2.plot(income_range, flat_rates, label="Flat Tax")

ax2.set_xlabel("Income (₹)")
ax2.set_ylabel("Effective Tax Rate (%)")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)
