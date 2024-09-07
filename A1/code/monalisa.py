# imports
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 300  # higher resolution output images

img = plt.imread("Mona_Lisa.jpg")  # read the image

plt.imshow(img)
plt.gca().set_xlabel("x")  # set the x-label of the current Axes (returned by the gca)
plt.gca().set_ylabel("y")  # set the y-label of the current Axes

correlations_x = np.array(
    list(range(-10, 0)) + list(range(1, 11))
)  # x axis values for correlation plot
correlations_y = np.zeros(20)  # y axis values for correlation plot

for k in range(20):
    tx = correlations_x[k]  # shift amount
    img_new = np.zeros_like(img, dtype=np.uint8)  # create a new image
    if tx >= 0:
        img_new[:, tx:] = img[:, : img.shape[1] - tx]
    else:
        img_new[:, : img.shape[1] + tx] = img[:, -tx:]
    correlations_y[k] = np.corrcoef(img.flatten(), img_new.flatten())[
        0, 1
    ]  # store correlation

# plot the correlations
plt.figure()
plt.plot(correlations_x, correlations_y)
plt.xlabel("Pixel shift amount")
plt.ylabel("Correlation with original image")
plt.savefig("correlation.png")

# grayscale image for pixel intensities
img_gray = img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 + img[:, :, 2] * 0.1140
plt.imshow(img_gray, cmap="gray")

# histogram
h = np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        h[int(img_gray[i, j])] += 1
# normalized histogram
p = h / (img_gray.shape[0] * img_gray.shape[1])

# plot the normalized histogram
plt.figure()
_ = plt.hist(np.arange(256), weights=p, bins=64, edgecolor="black")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.savefig("normalized_histogram.png")
