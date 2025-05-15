import unittest
from EmotionDetection.emotion_detection import emotion_detector


class test_emotion_detection(unittest.TestCase):
    def test_emotion_detection(self):
        result_A = emotion_detector("I am glad this happened")
        self.assertEqual(result_A['dominant_emotion'], 'joy')
    def test_emotion_detection(self):
        result_B = emotion_detector("I am really mad about this")
        self.assertEqual(result_B['dominant_emotion'], 'anger')

    def test_emotion_detection(self):
        result_C = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_C['dominant_emotion'], 'disgust')      

    def test_emotion_detection(self):
        result_D = emotion_detector("I am so sad about this")
        self.assertEqual(result_D['dominant_emotion'], 'sadness')   

    def test_emotion_detection(self):
        result_E = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_E['dominant_emotion'], 'fear')   

unittest.main()