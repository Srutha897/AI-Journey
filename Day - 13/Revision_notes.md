# Day 13 - Revision Notes

## Project 1 - Movie Sentiment Analyzer
- TF-IDF: Term Frequency × Inverse Document Frequency
- fit_transform on train, transform on test (prevent data leakage)
- Balanced dataset: 25k positive, 25k negative
- random_state=42: reproducible splits
- Bug fixed: 54% → 89.47% accuracy

## Project 2 - Image Classifier
- CNN layers: Conv → ReLU → MaxPool → Flatten → FC
- Resize to 224×224 for ResNet50
- Transfer Learning: freeze layers 1-3, unfreeze layer 4
- Overfitting: 96.89% train vs 70.05% test (CNN from scratch)
- Fine tuning: 90.94% test accuracy ✅

## Quiz Score: 96/100 