from sklearn.model_selection import train_test_split

# Example dataset: emails and their labels (1 = spam, 0 = not spam)
emails = [
    "Win a free iPhone now!",
    "Meeting at 10am tomorrow",
    "Congratulations, you won a lottery!",
    "Lunch plans?",
    "Get cheap meds online",
    "Project update attached"
]
labels = [1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

# Split into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2, random_state=42)

print("Training emails:", X_train)
print("Training labels:", y_train)
print("Test emails:", X_test)
print("Test labels:", y_test)
