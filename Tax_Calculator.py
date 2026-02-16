import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tax Calculator Web App")
st.subheader("Comparison of Old Regime, New Regime & Flat Tax System")


income = st.number_input(
    "Enter your Annual Income (₹)",
    min_value=0,
    step=50000,
    value=500000
)

CESS = 0.04


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


def new_tax(income):
    tax = 0

    slabs = [
        (300000, 0),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]

    remaining_income = income

    for slab_amount, rate in slabs:
        taxable = min(remaining_income, slab_amount)
        tax += taxable * rate
        remaining_income -= taxable

        if remaining_income <= 0:
            break

    return tax * (1 + CESS)


def flat_tax(income, rate=0.20):
    tax = income * rate
    return tax * (1 + CESS)


old_regime_tax = old_tax(income)
new_regime_tax = new_tax(income)
flat_regime_tax = flat_tax(income)


def effective_rate(tax, income):
    if income == 0:
        return 0
    return (tax / income) * 100


old_etr = effective_rate(old_regime_tax, income)
new_etr = effective_rate(new_regime_tax, income)
flat_etr = effective_rate(flat_regime_tax, income)


st.header("Tax Summary")

st.write(f"**Old Regime Tax:** ₹ {old_regime_tax:,.2f}")
st.write(f"**New Regime Tax:** ₹ {new_regime_tax:,.2f}")
st.write(f"**Flat Tax (20%):** ₹ {flat_regime_tax:,.2f}")


tax_dict = {
    "Old Regime": old_regime_tax,
    "New Regime": new_regime_tax,
    "Flat Tax": flat_regime_tax
}

best_option = min(tax_dict, key=tax_dict.get)

st.success(f" Lowest Tax Payable Under: **{best_option}**")


income_range = np.linspace(100000, 2000000, 50)

old_taxes = [old_tax(i) for i in income_range]
new_taxes = [new_tax(i) for i in income_range]
flat_taxes = [flat_tax(i) for i in income_range]

old_rates = [(old_tax(i)/i)*100 for i in income_range]
new_rates = [(new_tax(i)/i)*100 for i in income_range]
flat_rates = [(flat_tax(i)/i)*100 for i in income_range]


st.header("Graph 1: Income vs Total Tax")

fig1 = plt.figure()
plt.plot(income_range, old_taxes, label="Old Regime")
plt.plot(income_range, new_taxes, label="New Regime")
plt.plot(income_range, flat_taxes, label="Flat Tax")

plt.xlabel("Income (₹)")
plt.ylabel("Total Tax (₹)")
plt.title("Income vs Total Tax")
plt.legend()
plt.grid(True)

st.pyplot(fig1)


st.header("Graph 2: Effective Tax Rate")

fig2 = plt.figure()
plt.plot(income_range, old_rates, label="Old Regime")
plt.plot(income_range, new_rates, label="New Regime")
plt.plot(income_range, flat_rates, label="Flat Tax")

plt.xlabel("Income (₹)")
plt.ylabel("Effective Tax Rate (%)")
plt.title("Income vs Effective Tax Rate")
plt.legend()
plt.grid(True)

st.pyplot(fig2)
