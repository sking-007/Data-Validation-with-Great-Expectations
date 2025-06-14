import pandas as pd
from great_expectations.dataset import PandasDataset
import os

# Create test data
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "email": ["test@example.com", "user@site.com", "bad-email", None, "admin@page.com"],
    "amount": [250.5, -20.0, 300.0, None, 450.0]
})
df.to_csv("raw_data.csv", index=False)

# Define validation rules
class CustomDataset(PandasDataset):
    def validate_data(self):
        self.expect_column_values_to_not_be_null("id")
        self.expect_column_values_to_match_regex("email", r"[^@\s]+@[^@\s]+\.[^@\s]+", mostly=0.8)
        self.expect_column_values_to_be_between("amount", 0, 10000, allow_cross_type=True)

data = CustomDataset(df)
results = data.validate_data()
print(results)
