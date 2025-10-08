
# Minimal Gradio app to load the trained model and run predictions
import pandas as pd
import joblib
import gradio as gr

bundle = joblib.load('music_genre_model.pkl')
pipe = bundle['model']
feature_cols = bundle['feature_cols']


def predict_genre(tempo, spectral_centroid, spectral_rolloff, zero_crossing_rate,
                  mfcc_1, mfcc_2, mfcc_3, mfcc_4, mfcc_5, mfcc_6, mfcc_7, mfcc_8, mfcc_9, mfcc_10, mfcc_11, mfcc_12, mfcc_13):
    row = [[tempo, spectral_centroid, spectral_rolloff, zero_crossing_rate,
            mfcc_1, mfcc_2, mfcc_3, mfcc_4, mfcc_5, mfcc_6, mfcc_7, mfcc_8, mfcc_9, mfcc_10, mfcc_11, mfcc_12, mfcc_13]]
    df_in = pd.DataFrame(row, columns=feature_cols)
    pred = pipe.predict(df_in)[0]
    proba = pipe.predict_proba(df_in)[0]
    classes = list(pipe.classes_)
    pairs = sorted(zip(classes, proba), key=lambda x: x[1], reverse=True)
    top = [c + ': ' + str(round(float(p), 3)) for c, p in pairs]
    return 'Prediction: ' + str(pred) + '\n' + '\n'.join(top)

inputs = [
    gr.Slider(40, 200, value=120, label='tempo'),
    gr.Slider(500, 6000, value=2000, label='spectral_centroid'),
    gr.Slider(1000, 8000, value=4500, label='spectral_rolloff'),
    gr.Slider(0.0, 0.3, value=0.12, step=0.001, label='zero_crossing_rate'),
    gr.Number(value=0, label='mfcc_1'),
    gr.Number(value=80, label='mfcc_2'),
    gr.Number(value=-40, label='mfcc_3'),
    gr.Number(value=25, label='mfcc_4'),
    gr.Number(value=-15, label='mfcc_5'),
    gr.Number(value=10, label='mfcc_6'),
    gr.Number(value=-8, label='mfcc_7'),
    gr.Number(value=5, label='mfcc_8'),
    gr.Number(value=-3, label='mfcc_9'),
    gr.Number(value=2, label='mfcc_10'),
    gr.Number(value=-1, label='mfcc_11'),
    gr.Number(value=0.5, label='mfcc_12'),
    gr.Number(value=0, label='mfcc_13')
]

iface = gr.Interface(fn=predict_genre, inputs=inputs, outputs='text', title='Music Genre Classifier')

if __name__ == '__main__':
    iface.launch(share=True)
