# Usage Guide

## Running the Application

### Local Development

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to the local URL displayed in the terminal (typically `http://127.0.0.1:7860`)

### Public Sharing

The application is configured with `share=True`, which automatically generates a public URL that you can share with others. This link is valid for 72 hours.

## Understanding the Features

### Audio Features Explained

#### Tempo (40-200 BPM)
- The speed of the music
- Lower values = slower music (ballads, ambient)
- Higher values = faster music (dance, electronic)

#### Spectral Centroid (500-6000 Hz)
- Indicates the "brightness" of the sound
- Higher values = brighter, more treble-heavy sounds
- Lower values = darker, more bass-heavy sounds

#### Spectral Rolloff (1000-8000 Hz)
- The frequency below which 85% of the spectrum's energy is contained
- Helps distinguish between harmonic and noisy sounds

#### Zero Crossing Rate (0.0-0.3)
- How often the signal changes from positive to negative
- Higher values = more percussive or noisy sounds
- Lower values = more tonal sounds

#### MFCCs (Mel-Frequency Cepstral Coefficients)
- 13 coefficients that capture the timbral texture of audio
- Represent the shape of the spectral envelope
- Critical for distinguishing between different instruments and voices

## Example Inputs

### Rock Music
- Tempo: 120-140
- Spectral Centroid: 2500-3500
- Zero Crossing Rate: 0.15-0.20
- MFCCs: Vary based on instrumentation

### Classical Music
- Tempo: 60-120
- Spectral Centroid: 1500-2500
- Zero Crossing Rate: 0.08-0.12
- MFCCs: Lower variance

### Electronic/Dance
- Tempo: 120-140
- Spectral Centroid: 3000-5000
- Zero Crossing Rate: 0.18-0.25
- MFCCs: Higher variance

## Tips for Best Results

1. **Adjust multiple features**: Don't just change one slider - music genres are characterized by combinations of features
2. **Experiment**: Try different combinations to see how the model responds
3. **Check probabilities**: Look at all genre probabilities, not just the top prediction
4. **Use realistic values**: Stay within the suggested ranges for each feature

## Troubleshooting

### Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that Python version is 3.7 or higher
- Verify `music_genre_model.pkl` exists in the directory

### Predictions seem incorrect
- Verify input values are within reasonable ranges
- Remember that the model's accuracy depends on training data
- Some music may have characteristics of multiple genres

### Public link not working
- Public links expire after 72 hours
- Restart the application to generate a new link
- Check your internet connection

## Advanced Usage

### Integrating with Other Applications

You can use the `predict_genre()` function programmatically:

```python
from app import predict_genre

result = predict_genre(
    tempo=120,
    spectral_centroid=2000,
    spectral_rolloff=4500,
    zero_crossing_rate=0.12,
    mfcc_1=0, mfcc_2=80, mfcc_3=-40,
    mfcc_4=25, mfcc_5=-15, mfcc_6=10,
    mfcc_7=-8, mfcc_8=5, mfcc_9=-3,
    mfcc_10=2, mfcc_11=-1, mfcc_12=0.5,
    mfcc_13=0
)
print(result)
```

---

Built with Julius AI
