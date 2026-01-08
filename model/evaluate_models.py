from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, matthews_corrcoef, roc_auc_score
from sklearn.preprocessing import label_binarize

def evaluate_metrics(y_true, y_pred, y_prob, classes):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, average="macro"),
        "Recall": recall_score(y_true, y_pred, average="macro"),
        "F1": f1_score(y_true, y_pred, average="macro"),
        "MCC": matthews_corrcoef(y_true, y_pred),
        "AUC": roc_auc_score(
            label_binarize(y_true, classes),
            y_prob,
            multi_class="ovr"
        )
    }
