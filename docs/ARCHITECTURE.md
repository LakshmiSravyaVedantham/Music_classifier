# Architecture Documentation

## System Overview

The Music Genre Classifier is a machine learning application that predicts music genres based on audio features. The system consists of three main components:

## Components

### 1. Machine Learning Model (`music_genre_model.pkl`)

**Purpose**: Pre-trained classifier for genre prediction

**Contents**:
- Trained scikit-learn pipeline
- Feature column names
- Genre class labels

**Input**: 17 audio features
- 1 tempo feature
- 3 spectral features (centroid, rolloff, zero crossing rate)
- 13 MFCC features

**Output**: 
- Predicted genre label
- Probability distribution across all genres

### 2. Web Application (`app.py`)

**Purpose**: Interactive user interface for predictions

**Framework**: Gradio 5.49.0

**Key Functions**:

#### `predict_genre()`
```python
def predict_genre(tempo, spectral_centroid, spectral_rolloff, 
                  zero_crossing_rate, mfcc_1, ..., mfcc_13)
```

**Process Flow**:
1. Accepts 17 audio features as input
2. Constructs pandas DataFrame with proper column names
3. Uses model pipeline for prediction
4. Calculates probability scores
5. Returns formatted prediction with probabilities

**Interface Components**:
- Sliders for continuous features (tempo, spectral features, zero crossing rate)
- Number inputs for MFCC coefficients
- Text output for predictions

### 3. Dependencies (`requirements.txt`)

**Core Libraries**:
- `gradio==5.49.0`: Web interface
- `pandas`: Data manipulation
- `scikit-learn`: ML model support
- `joblib`: Model serialization

## Data Flow

```
User Input (Web Interface)
    ↓
Feature Collection (17 values)
    ↓
DataFrame Construction
    ↓
Model Pipeline
    ↓
Prediction + Probabilities
    ↓
Formatted Output
    ↓
Display to User
```

## Feature Engineering

### Audio Features Used

1. **Temporal Features**
   - Tempo (BPM)

2. **Spectral Features**
   - Spectral Centroid: Brightness indicator
   - Spectral Rolloff: Energy distribution
   - Zero Crossing Rate: Signal changes

3. **Cepstral Features**
   - 13 MFCCs: Timbral characteristics

## Model Pipeline

The model uses a scikit-learn pipeline that may include:
- Feature scaling/normalization
- Dimensionality reduction (optional)
- Classification algorithm

## Deployment Architecture

### Local Deployment
```
Python Process
    ↓
Gradio Server (Port 7860)
    ↓
Local Browser (127.0.0.1:7860)
```

### Public Sharing
```
Python Process
    ↓
Gradio Server
    ↓
Gradio Cloud Proxy
    ↓
Public URL (*.gradio.live)
    ↓
Remote Users
```

## Security Considerations

1. **Model File**: Pre-trained, read-only
2. **User Input**: Validated by Gradio sliders/inputs
3. **Public Sharing**: 72-hour expiration on public links
4. **Dependencies**: Pinned versions in requirements.txt

## Performance Characteristics

- **Prediction Latency**: < 100ms per prediction
- **Model Size**: ~1.8 MB
- **Memory Usage**: Minimal (model loaded once at startup)
- **Concurrent Users**: Supported via Gradio's built-in handling

## Extensibility

### Adding New Features
1. Update `predict_genre()` function signature
2. Add corresponding Gradio input component
3. Update feature_cols in model bundle
4. Retrain model with new features

### Changing the Model
1. Train new model with same feature structure
2. Save as pickle file with same bundle format
3. Replace `music_genre_model.pkl`
4. No code changes required

### UI Customization
- Modify Gradio components in `inputs` list
- Adjust slider ranges and default values
- Change interface title and description

## Error Handling

- **Missing Model File**: Application fails at startup
- **Invalid Input**: Gradio validates input ranges
- **Prediction Errors**: Caught and displayed to user

## Future Enhancements

Potential improvements:
- Audio file upload and feature extraction
- Batch prediction support
- Model performance metrics display
- Genre confidence visualization
- Historical prediction tracking
- A/B testing framework

---

Built with Julius AI
