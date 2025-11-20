# Gravitational Potential Calculator & Grapher

## Description
This project visualizes the variation of Gravitational Potential ($V$) with distance ($R$). 
It uses the formula:

$$ V = -\frac{GM}{R} $$

Where:
- **G**: Gravitational Constant ($6.67 \times 10^{-11}$)
- **M**: Mass of the object (kg)
- **R**: Distance from center (m)

## Features
1. **Calculator:** Inputs Mass and Radius to calculate the exact Potential.
2. **Visualizer:** Generates a graph showing:
   - The curve of potential as $R$ varies.
   - **Zero Potential** at infinity (Maximum).
   - **Negative Potential** as $R \to 0$ (Minimum).
   - A specific point marking the user's input.

## How to Run
1. Install dependencies:
   ```bash
   pip install matplotlib numpy
