#Confusion matrix Description

#A confusion matrix is basically a reality check for your model.
#You trained a model to predict something — like spam/not spam, disease/no disease, pass/fail, etc.
 #Now you want to see:
#Where did it get things right?


#Where did it mess up?


#And how badly?


#Instead of just saying “accuracy = 90%”, the confusion matrix shows exactly what kind of mistakes happened.
#For a binary classification problem (2 classes), it looks like this:



#In simple words:
#True Positive (TP) → Model said YES, and it was YES.


#True Negative (TN) → Model said NO, and it was NO.


#False Positive (FP) → Model said YES, but it was NO. (False alarm)


#False Negative (FN) → Model said NO, but it was YES. (Missed case)


#So basically:
 #It shows who your model confused with whom.
#That’s why it’s called a confusion matrix.

# Step 1: Import libraries
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Step 2: Example actual and predicted values
# Suppose these are the true labels
y_true = [0, 1, 0, 1, 0, 1, 1, 0]

# Suppose these are model predictions
y_pred = [0, 1, 0, 0, 0, 1, 1, 1]

# Step 3: Create confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Step 4: Print matrix values
print("Confusion Matrix:\n", cm)

# Step 5: Display it nicely
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()


