"""
Example script demonstrating how to use the Music Genre Classifier
Built with Julius AI
"""

from app import predict_genre

def example_rock():
    """Example prediction for rock music characteristics"""
    print("=" * 60)
    print("Example 1: Rock Music")
    print("=" * 60)
    result = predict_genre(
        tempo=130,
        spectral_centroid=3000,
        spectral_rolloff=5000,
        zero_crossing_rate=0.18,
        mfcc_1=0, mfcc_2=85, mfcc_3=-35,
        mfcc_4=30, mfcc_5=-12, mfcc_6=15,
        mfcc_7=-5, mfcc_8=8, mfcc_9=-2,
        mfcc_10=3, mfcc_11=-1, mfcc_12=1.0,
        mfcc_13=0.5
    )
    print(result)
    print()

def example_classical():
    """Example prediction for classical music characteristics"""
    print("=" * 60)
    print("Example 2: Classical Music")
    print("=" * 60)
    result = predict_genre(
        tempo=90,
        spectral_centroid=2000,
        spectral_rolloff=3500,
        zero_crossing_rate=0.10,
        mfcc_1=0, mfcc_2=75, mfcc_3=-45,
        mfcc_4=20, mfcc_5=-18, mfcc_6=8,
        mfcc_7=-10, mfcc_8=3, mfcc_9=-4,
        mfcc_10=1, mfcc_11=-2, mfcc_12=0.3,
        mfcc_13=-0.5
    )
    print(result)
    print()

def example_electronic():
    """Example prediction for electronic/dance music characteristics"""
    print("=" * 60)
    print("Example 3: Electronic/Dance Music")
    print("=" * 60)
    result = predict_genre(
        tempo=128,
        spectral_centroid=4000,
        spectral_rolloff=6000,
        zero_crossing_rate=0.22,
        mfcc_1=5, mfcc_2=90, mfcc_3=-30,
        mfcc_4=35, mfcc_5=-10, mfcc_6=20,
        mfcc_7=-3, mfcc_8=10, mfcc_9=-1,
        mfcc_10=4, mfcc_11=0, mfcc_12=1.5,
        mfcc_13=1.0
    )
    print(result)
    print()

def main():
    """Run all example predictions"""
    print("\n🎵 Music Genre Classifier - Example Usage\n")
    
    example_rock()
    example_classical()
    example_electronic()
    
    print("=" * 60)
    print("Try running the Gradio app for interactive predictions:")
    print("python app.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
