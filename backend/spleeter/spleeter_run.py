from spleeter.separator import Separator

def separate_audio(input_path, output_path):
    # Initialize Spleeter with a pre-trained 2-stems model (vocal + instrumental)
    separator = Separator('spleeter:2stems')
    # Separate audio
    separator.separate_to_file(input_path, output_path)

if __name__ == "__main__":
    separate_audio('input_song.mp3', 'output/')