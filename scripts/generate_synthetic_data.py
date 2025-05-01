import joblib
import random
from faker import Faker
from collections import defaultdict

fake = Faker()

def generate_bank_statement():
    return f"""
    Bank of {fake.company()}
    Account Holder: {fake.name()}
    Statement Period: 2024-01
    {fake.date_this_month()} Direct Deposit ${random.randint(100, 1000)}
    {fake.date_this_month()} Debit Purchase ${random.randint(10, 500)}
    {fake.date_this_month()} Loan Repayment ${random.randint(200, 800)}
    {fake.date_this_month()} Wire Transfer ${random.randint(200, 900)}
    {fake.date_this_month()} ATM Withdrawal ${random.randint(5, 250)}
    {fake.date_this_month()} POS Purchase ${random.randint(100, 1000)}
    {fake.date_this_month()} Debit Purchase ${random.randint(10, 500)}
    End of Statement
    """.strip()

def generate_invoice():
    return f"""
    INVOICE
    Date: {fake.date_this_year()}
    To: {fake.name()}
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

SAMPLES_PER_TYPE = 5

# === Generate data ===

synthetic_data = defaultdict(list)

for label, generator in DOCUMENT_GENERATORS.items():
    for _ in range(SAMPLES_PER_TYPE):
        synthetic_data[label].append(generator())

# === Save ===
joblib.dump(dict(synthetic_data), "../model/synthetic_data.pkl")
print(f"✅ Saved synthetic data for {len(synthetic_data)} document types.")