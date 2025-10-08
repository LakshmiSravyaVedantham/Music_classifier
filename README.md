# 🎵 Music Genre Classifier

A machine learning-powered web application that predicts music genres based on audio features. Built with Gradio for an interactive user interface.

## 📋 Overview

This project uses a trained machine learning model to classify music genres based on various audio features including tempo, spectral characteristics, and Mel-frequency cepstral coefficients (MFCCs).

## ✨ Features

- **Interactive Web Interface**: User-friendly Gradio interface with sliders and input fields
- **Real-time Predictions**: Instant genre classification with probability scores
- **Multiple Audio Features**: Analyzes 17 different audio characteristics
- **Shareable Link**: Generate public links to share the application

## 🎯 Audio Features Used

The classifier uses the following audio features:

1. **Tempo**: The speed or pace of the music (40-200 BPM)
2. **Spectral Centroid**: Indicates where the "center of mass" of the spectrum is located
3. **Spectral Rolloff**: The frequency below which a specified percentage of the total spectral energy lies
4. **Zero Crossing Rate**: The rate at which the signal changes from positive to negative or vice versa
5. **MFCCs (1-13)**: Mel-frequency cepstral coefficients that represent the short-term power spectrum of sound

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/LakshmiSravya123/Music_classifier.git
cd Music_classifier
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Run the application with:
```bash
python app.py
```

The application will launch and provide:
- A local URL (e.g., `http://127.0.0.1:7860`)
- A public shareable URL (e.g., `https://xxxxx.gradio.live`)

## 📦 Project Structure

```
MusicClassifier/
├── app.py                    # Main application file
├── music_genre_model.pkl     # Trained ML model
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Gradio**: Web interface framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **joblib**: Model serialization

## 📊 How It Works

1. The user inputs audio features through the web interface
2. Features are processed into a pandas DataFrame
3. The pre-trained model predicts the genre
4. Results are displayed with confidence scores for all genres

## 🤖 Model Information

The model is stored in `music_genre_model.pkl` and includes:
- Trained classifier pipeline
- Feature column names
- Class labels for music genres

## 🌐 Usage Example

1. Open the application in your browser
2. Adjust the sliders and input fields for audio features:
   - Set tempo (e.g., 120 BPM)
   - Adjust spectral centroid (e.g., 2000 Hz)
   - Configure MFCC values
3. View the predicted genre and probability scores

## 📝 Development

This project was developed using **Julius AI**, an AI-powered development assistant.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Lakshmi Sravya**
- GitHub: [@LakshmiSravya123](https://github.com/LakshmiSravya123)

## 🙏 Acknowledgments

- Built with Julius AI
- Gradio for the amazing web interface framework
- scikit-learn community for ML tools

---

Made with ❤️ using Julius AI
