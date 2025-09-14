# Fast Fourier Transform (FFT) & Image Compression

_Engineering Mathematics — University of Tehran_

This project explores the **Fast Fourier Transform (FFT)** as a fundamental tool in **image processing**, with a focus on its application to **image compression**.  
It bridges theoretical aspects of Fourier analysis with practical implementation in Python, highlighting how high-frequency components can be reduced to achieve efficient compression while preserving visual quality.

## Overview

-   **Fourier Series & Transform**  
    Breakdown of signals into frequency components, enabling deeper insight into patterns and noise.
    
-   **From DFT to FFT**  
    Transition from the computationally expensive Discrete Fourier Transform (DFT) to the efficient **FFT algorithm**, reducing complexity from **O(N²) → O(N log N)**.
    
-   **FFT in Image Processing**
    -   Conversion of spatial-domain images into frequency-domain representation.     
    -   Selective removal of high-frequency components to reduce redundancy.   
    -   Image reconstruction using inverse FFT, achieving compression with minimal perceptual loss.
        
-   **Implementation in Python**
    -   Application of **2D FFT** per image channel.    
    -   Visualization of FFT magnitude spectra.    
    -   Comparison of compression levels at different thresholds (90%, 99%, 99.5%, 99.9%).
    -   Trade-off analysis between storage reduction and image quality.
        

## Results

-   **FFT Spectrum Visualization** — clear mapping of spatial details into frequency components.
-   **Compression Demonstration** — progressive removal of frequency coefficients shows significant reduction in file size with only slight degradation in visual quality.
-   **Practical Insight** — FFT-based compression provides a balance of efficiency and fidelity, useful in applications like storage, transmission, and multimedia systems.
    

## Contributors

-   **Parsa Bukani**
-   **Parsa Saeednia**
-   **Mohammadreza Pirhadi**
    

## License

This project is licensed under the **MIT License**.

