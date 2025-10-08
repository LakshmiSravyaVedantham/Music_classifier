# API Documentation

## Core Function

### `predict_genre()`

Predicts the music genre based on audio features.

#### Signature

```python
def predict_genre(
    tempo: float,
    spectral_centroid: float,
    spectral_rolloff: float,
    zero_crossing_rate: float,
    mfcc_1: float,
    mfcc_2: float,
    mfcc_3: float,
    mfcc_4: float,
    mfcc_5: float,
    mfcc_6: float,
    mfcc_7: float,
    mfcc_8: float,
    mfcc_9: float,
    mfcc_10: float,
    mfcc_11: float,
    mfcc_12: float,
    mfcc_13: float
) -> str
```

#### Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `tempo` | float | 40-200 | Beats per minute |
| `spectral_centroid` | float | 500-6000 | Center of mass of spectrum (Hz) |
| `spectral_rolloff` | float | 1000-8000 | Frequency rolloff point (Hz) |
| `zero_crossing_rate` | float | 0.0-0.3 | Rate of signal zero crossings |
| `mfcc_1` to `mfcc_13` | float | varies | Mel-frequency cepstral coefficients |

#### Returns

**Type**: `str`

**Format**:
```
Prediction: [Genre Name]
[Genre1]: [probability]
[Genre2]: [probability]
...
```

#### Example

```python
from app import predict_genre

result = predict_genre(
    tempo=120.0,
    spectral_centroid=2000.0,
    spectral_rolloff=4500.0,
    zero_crossing_rate=0.12,
    mfcc_1=0.0,
    mfcc_2=80.0,
    mfcc_3=-40.0,
    mfcc_4=25.0,
    mfcc_5=-15.0,
    mfcc_6=10.0,
    mfcc_7=-8.0,
    mfcc_8=5.0,
    mfcc_9=-3.0,
    mfcc_10=2.0,
    mfcc_11=-1.0,
    mfcc_12=0.5,
    mfcc_13=0.0
)

print(result)
```

**Output**:
```
Prediction: rock
rock: 0.856
pop: 0.089
electronic: 0.032
classical: 0.015
jazz: 0.008
```

## Model Bundle Structure

The `music_genre_model.pkl` file contains a dictionary with:

```python
{
    'model': sklearn_pipeline,      # Trained classifier pipeline
    'feature_cols': list[str]       # Feature column names
}
```

### Accessing Model Components

```python
import joblib

bundle = joblib.load('music_genre_model.pkl')
model = bundle['model']
features = bundle['feature_cols']

# Get available genre classes
classes = model.classes_
print(f"Available genres: {classes}")
```

## Gradio Interface

### Interface Configuration

```python
iface = gr.Interface(
    fn=predict_genre,
    inputs=[...],           # 17 input components
    outputs='text',
    title='Music Genre Classifier'
)
```

### Launch Options

```python
# Local only
iface.launch()

# With public sharing
iface.launch(share=True)

# Custom port
iface.launch(server_port=8080)

# Custom host
iface.launch(server_name="0.0.0.0")
```

## Input Components

### Sliders

```python
gr.Slider(
    minimum=40,
    maximum=200,
    value=120,
    label='tempo'
)
```

### Number Inputs

```python
gr.Number(
    value=0,
    label='mfcc_1'
)
```

## Error Handling

### Common Errors

**Model Not Found**:
```python
FileNotFoundError: [Errno 2] No such file or directory: 'music_genre_model.pkl'
```
**Solution**: Ensure model file is in the same directory as `app.py`

**Invalid Input Type**:
```python
TypeError: predict_genre() takes 17 positional arguments but X were given
```
**Solution**: Provide all 17 required audio features

**Model Loading Error**:
```python
ModuleNotFoundError: No module named 'sklearn'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

## Programmatic Usage

### Batch Predictions

```python
import pandas as pd
from app import predict_genre

# Sample data
samples = [
    (120, 2000, 4500, 0.12, 0, 80, -40, 25, -15, 10, -8, 5, -3, 2, -1, 0.5, 0),
    (90, 1800, 3500, 0.10, 0, 75, -45, 20, -18, 8, -10, 3, -4, 1, -2, 0.3, -0.5),
]

for sample in samples:
    result = predict_genre(*sample)
    print(result)
    print("-" * 40)
```

### Integration Example

```python
def analyze_audio_file(audio_path):
    """
    Extract features from audio file and predict genre
    (Feature extraction not included in this project)
    """
    # Extract features (using librosa or similar)
    features = extract_features(audio_path)
    
    # Predict genre
    prediction = predict_genre(
        tempo=features['tempo'],
        spectral_centroid=features['spectral_centroid'],
        spectral_rolloff=features['spectral_rolloff'],
        zero_crossing_rate=features['zero_crossing_rate'],
        **features['mfccs']
    )
    
    return prediction
```

## Performance Notes

- **Cold Start**: ~1-2 seconds (model loading)
- **Prediction Time**: < 100ms per prediction
- **Memory Usage**: ~50MB (model + dependencies)
- **Concurrent Requests**: Handled by Gradio automatically

---

Built with Julius AI
