Signature Similarity Recognition

This repository offers Python code that uses deep learning methods to identify signature similarity. The ResNet101 architecture, which has been pre-trained on the ImageNet dataset, is employed to extract feature vectors from signature photos. The cosine similarity between these feature vectors is then computed to ascertain the similarity between signatures.

Requirements

```bash
# Python=3.10.12
tensorflow==2.15.0
numpy==1.25.2
opencv-python==4.8.0
scipy==1.11.4
```

You can install the required dependencies via pip:
```bash
pip install -r requirements.txt
```