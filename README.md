# OpenCV Intro — FreeCodeCamp Course Walkthrough 👁️

My complete walkthrough of **[FreeCodeCamp's OpenCV Course](https://www.youtube.com/watch?v=oXlwWbU8l2o)** (~3.5 hours, taught by Jason Dsouza — companion repo: [jasmcaus/opencv-course](https://github.com/jasmcaus/opencv-course)). Every script and notebook here was written by me while following along, section by section, from the basics up to face recognition and deep computer vision.

## Course sections covered

### Basics
- `Reading Images & Video.ipynb` — loading and displaying images and video streams
- `Resizing and Rescaling Frames.ipynb` — resizing images and rescaling video frames
- `Draw and Write on Images.ipynb` — drawing shapes and putting text on images
- `5 Essential Functions.ipynb` — grayscale, blur, edge cascade, dilate, erode
- `Image Transformations.py` — translation, rotation, flipping, cropping
- `Contour Detection.py` — finding and drawing contours

### Advanced
- `Color Spaces.py` — BGR ↔ HSV ↔ LAB ↔ RGB conversions
- `Color Channels.py` — splitting and merging color channels
- `Smoothing.py` — averaging, Gaussian, median and bilateral blurring
- `Bitwise Operations.py` — AND, OR, XOR, NOT
- `Masking.py` — isolating regions of interest with masks
- `Histogram Computations.py` — grayscale and color histograms
- `Thresholding.py` — simple and adaptive thresholding
- `Edge Detection.py` — Laplacian, Sobel and Canny edge detectors

### Faces
- `Face Detection With Haar Cascades.py` — detecting faces with `haar_face.xml`
- `faces_train.py` — training OpenCV's LBPH face recognizer (outputs `face_trained.yml`, `features.npy`, `labels.npy`)
- `face_recognition.py` — recognizing faces with the trained model

### Capstone
- `Deep Computer Vision.ipynb` — building an image classifier with a convolutional neural network

### Bonus — applying what I learned
- `Satellite Frame Detection Simulation.ipynb` — my own experiment using the course's techniques for frame detection on satellite imagery

## Running the code

```bash
pip install opencv-contrib-python numpy matplotlib
```

Then run any script directly, e.g.:

```bash
python "Edge Detection.py"
```

> The face detection/recognition scripts need `opencv-contrib-python` (not the plain `opencv-python`) for the `cv2.face` module, and expect sample images — point the paths at your own photos or the course's resources.

## 🔗 More

- Author: [@pop123-ux](https://github.com/pop123-ux)
- Medium write-ups: [medium.com/@Pop123](https://medium.com/@Pop123)
