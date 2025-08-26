import streamlit as st

# --- Title ---
st.title("Multi-Agent RAG Demo (Salary + Insurance)")

# --- Text input ---
user_query = st.text_input("Your Question:")

# --- Process button ---
if st.button("Ask") and user_query:
    query = user_query.lower()
    if any(word in query for word in ["salary", "annual", "monthly", "deduction"]):
        st.write("💰 Salary Agent: Your annual salary = monthly salary × 12, minus deductions.")
    elif any(word in query for word in ["insurance", "premium", "claim", "coverage"]):
        st.write("🛡 Insurance Agent: Insurance covers hospitalization, emergencies, and claim process.")
    else:
        st.write("⚠️ I can only answer Salary or Insurance questions.")
