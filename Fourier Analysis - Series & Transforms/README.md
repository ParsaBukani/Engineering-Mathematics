# Fourier Analysis — Series & Transforms

_Engineering Mathematics — University of Tehran_

This project explores the **implementation and applications of Fourier analysis**, focusing on both  
**discrete Fourier series** and the **2D Fourier transform for images**.  
The assignment was divided into two main problems.


## Problem 1 — Discrete Fourier Series

1. **Signal Definition**  
   - Choose a periodic signal (e.g., square wave, triangular wave).  
   - Represent it as an array over one period and visualize it.

2. **Coefficient Calculation**  
   - Implement functions to compute Fourier series coefficients
   - Verify correctness by comparing with manual calculations for the first three terms.

3. **Signal Reconstruction**  
   - Reconstruct the original signal from the coefficients.  
   - Study the effect of increasing the number of terms.

> **Goal:** Implement the Fourier series and analyze how the number of coefficients affects reconstruction accuracy.


## Problem 2 — 2D Fourier Transform of Images

1. **Transform Computation**  
   - Implement the 2D Fourier transform manually (no library FFT functions).  
   - Visualize the log-magnitude of Fourier coefficients.

2. **Coefficient Reduction & Image Quality**  
   - Retain only a fraction of the Fourier coefficients (based on energy distribution).  
   - Study the trade-off between number of coefficients and reconstruction quality.

3. **Image Reconstruction**  
   - Implement the inverse 2D Fourier transform.  
   - Rebuild grayscale and color images from retained coefficients.  
   - Visualize results and evaluate with error metrics.

> **Goal:** Explore how Fourier coefficients contribute to image quality and compression.



## License

This project is licensed under the **MIT License**.

## Acknowledgements

Developed under the supervision of **Dr. Haghi**  
Teaching Assistants: **Babak Hosseini Mohtasham** and **Mohammad Sina Parvizi Motlagh**

