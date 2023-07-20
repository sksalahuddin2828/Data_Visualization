import numpy as np
import matplotlib.pyplot as plt

def convolve_1d(signal, kernel):
    kernel_size = kernel.shape[0]
    signal_size = signal.shape[0]
    result_size = signal_size + kernel_size - 1
    result = np.zeros(result_size)

    for i in range(result_size):
        for j in range(kernel_size):
            if i - j >= 0 and i - j < signal_size:
                result[i] += signal[i - j] * kernel[j]

    return result

def visualize_4d_convolution(image, kernel):
    # Compute output dimensions
    output_height = image.shape[0] - kernel.shape[0] + 1
    output_width = image.shape[1] - kernel.shape[1] + 1

    # Initialize output tensor
    output = np.zeros((output_height, output_width, kernel.shape[3], image.shape[3]))

    # Perform convolution
    for i in range(output_height):
        for j in range(output_width):
            for out_channel in range(kernel.shape[3]):
                for in_channel in range(image.shape[2]):
                    for batch in range(image.shape[3]):
                        output[i, j, out_channel, batch] += np.sum(
                            image[i:i + kernel.shape[0], j:j + kernel.shape[1], in_channel, batch]
                            * kernel[:, :, in_channel, out_channel]
                        )

    # Visualize the 4D image and the kernel (Same as before)

    # Visualize the output feature maps
    plt.figure(figsize=(12, 6))

    for out_channel in range(kernel.shape[3]):
        for batch in range(image.shape[3]):
            plt.subplot(kernel.shape[3], image.shape[3], out_channel * image.shape[3] + batch + 1)
            plt.imshow(output[:, :, out_channel, batch], cmap='gray')
            plt.title(f'Output Channel {out_channel}, Batch {batch}')

    plt.show()

if __name__ == '__main__':
    # 1D Convolution Example (Same as before)

    # 4D Convolution Example
    image = np.random.rand(5, 5, 3, 2)  # 5x5 image with 3 channels and 2 images in a batch
    kernel = np.random.rand(3, 3, 3, 4)  # 3x3 kernel with 3 input channels and 4 output channels

    visualize_4d_convolution(image, kernel)
