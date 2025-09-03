from pathlib import Path
import pandas as pd

DATA = Path("data/raw")
df = pd.read_csv(DATA / "global_coffee_health.csv")  # update filename if needed
print(df.head())
