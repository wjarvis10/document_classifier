import joblib
import random
from faker import Faker
from collections import defaultdict
import logging

fake = Faker()

def generate_bank_statement():
    transaction_types = [
        "Direct Deposit",
        "ACH Payment",
        "Wire Transfer",
        "Check Deposit",
        "Debit Card Purchase",
        "POS Purchase",
        "Online Transfer",
        "ATM Withdrawal",
        "Loan Repayment",
        "Bank Fee"
    ]

    num_entries=random.randint(10, 20)

    entries = []
    for _ in range(num_entries):
        date = fake.date_this_year()
        description = random.choice(transaction_types)
        amount = random.randint(10, 1000)
        entry = f"{date}\n{description}\n${amount}"
        entries.append(entry)


    header =  f"""
    Bank of {fake.company()}
    Customer Support: {fake.phone_number()}
    www.fakebankdomain.com
    Account Holder: {fake.name()}
    Statement Period: 2024-01
    Date
    Description
    Debit ($)
    Credit ($)
    """.strip()

    return header + "\n".join(entries) + "\nEnd of Statement"

def generate_invoice():
    return f"""
    INVOICE
    Invoice Number: {random.randint(1000, 9000)}
    Issue Date: {fake.date_this_year()}
    Invoice To: {fake.name()}
    Item: {fake.bs().title()}
    Quantity: {random.randint(1, 5)}
    Unit Price: ${random.randint(100, 1000)}
    Total: ${random.randint(100, 3000)}
    Contact: {fake.email()}
    """.strip()

def generate_drivers_license():
    return f"""
    DRIVER LICENSE
    Name: {fake.name()}
    DOB: {fake.date_of_birth()}
    Eyes: {fake.color_name()}
    License No: {fake.uuid4()[:8].upper()}
    Expiry: {fake.date_between(start_date='today', end_date='+5y')}
    Address: {fake.address()}
    """.strip()

# can add more generators based upon scope
DOCUMENT_GENERATORS = {
    "bank_statement": generate_bank_statement,
    "invoice": generate_invoice,
    "drivers_license": generate_drivers_license,
}

SAMPLES_PER_TYPE = 10

# === Generate data ===

synthetic_data = defaultdict(list)

for label, generator in DOCUMENT_GENERATORS.items():
    for _ in range(SAMPLES_PER_TYPE):
        synthetic_data[label].append(generator())

# === Save ===
joblib.dump(dict(synthetic_data), "../model/synthetic_data.pkl")
logging.info(f"✅ Saved synthetic data for {len(synthetic_data)} document types.")