"""
Task 1: Display Pixel Density (PPI/DPI) Calculator
HCI & Computer Graphics Lab 1
"""

import math

def calculate_dpi(wpx, hpx, diagonal_inches):
    """
    Calculate DPI using the diagonal pixels and physical diagonal size
    Formula: DPI = √(W² + H²) / D_inches
    """
    diagonal_pixels = math.sqrt(wpx**2 + hpx**2)
    dpi = diagonal_pixels / diagonal_inches
    return dpi

def classify_density(dpi):
    """
    Classify display density based on DPI value
    """
    if dpi < 100:
        return "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        return "Medium Density (HD Display)"
    else:
        return "High Density (Retina / Mobile)"

def calculate_aspect_ratio(wpx, hpx):
    """
    Calculate simplified aspect ratio using GCD
    """
    gcd = math.gcd(wpx, hpx)
    return f"{wpx//gcd}:{hpx//gcd}"

def dpi_calculator():
    """Main function to run the DPI calculator"""
    
    print("="*60)
    print("DISPLAY PIXEL DENSITY (DPI/PPI) CALCULATOR")
    print("="*60)
    print()
    
    # Get user input
    wpx = int(input("Enter horizontal resolution (pixels): "))
    hpx = int(input("Enter vertical resolution (pixels): "))
    diagonal_inches = float(input("Enter physical diagonal size (inches): "))
    
    # Calculate metrics
    total_pixels = wpx * hpx
    aspect_ratio = calculate_aspect_ratio(wpx, hpx)
    dpi = calculate_dpi(wpx, hpx, diagonal_inches)
    density_category = classify_density(dpi)
    
    # Display results
    print()
    print("--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio : {aspect_ratio}")
    print(f"Calculated DPI : {dpi:.2f} DPI")
    print(f"Density Category : {density_category}")
    print()

if __name__ == "__main__":
    while True:
        dpi_calculator()
        
        # Ask if user wants to calculate another display
        another = input("Calculate another display? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("\nThank you for using the DPI Calculator!")
            break
        print()