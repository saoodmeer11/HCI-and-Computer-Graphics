"""
Task 2: Environment Setup & Synthetic Image Matrix Creation
HCI & Computer Graphics Lab 1

Create a 300×400×3 synthetic image with colored quadrants
"""

import numpy as np
import matplotlib.pyplot as plt

def create_synthetic_image():
    """
    Create a synthetic 300×400×3 image array with colored quadrants
    """
    
    # Create zero-initialized uint8 array
    # Shape: (Height=300, Width=400, Channels=3)
    image = np.zeros((300, 400, 3), dtype=np.uint8)
    
    # Fill quadrants with specific colors
    # Top-left quadrant: Pure Red [255, 0, 0]
    image[0:150, 0:200] = [255, 0, 0]
    
    # Top-right quadrant: Pure Green [0, 255, 0]
    image[0:150, 200:400] = [0, 255, 0]
    
    # Bottom-left quadrant: Pure Blue [0, 0, 255]
    image[150:300, 0:200] = [0, 0, 255]
    
    # Bottom-right quadrant: White [255, 255, 255]
    image[150:300, 200:400] = [255, 255, 255]
    
    return image

def display_matrix_metrics(image):
    """
    Print matrix metrics and properties
    """
    print("\n" + "="*60)
    print("TASK 2: Synthetic Image Matrix Creation")
    print("="*60)
    
    print("\n--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {image.shape}")
    print(f"Data Type : {image.dtype}")
    print(f"Total Elements : {image.size:,} values")
    print(f"Memory Footprint : {image.nbytes:,} bytes ({image.nbytes/1024:.2f} KB)")
    
    print("\n--- QUADRANT COLORS ---")
    print(f"Top-Left (Red)     : {image[75, 100]}")      # Sample pixel from red quadrant
    print(f"Top-Right (Green)  : {image[75, 300]}")      # Sample pixel from green quadrant
    print(f"Bottom-Left (Blue) : {image[225, 100]}")     # Sample pixel from blue quadrant
    print(f"Bottom-Right (White): {image[225, 300]}")    # Sample pixel from white quadrant

def visualize_image(image):
    """
    Display the synthetic image using matplotlib
    """
    plt.figure(figsize=(10, 7.5))
    plt.imshow(image)
    plt.title("Synthetic Image with Colored Quadrants (300×400×3)", fontsize=14, fontweight='bold')
    plt.xlabel("Width (pixels)")
    plt.ylabel("Height (pixels)")
    
    # Add grid lines at quadrant boundaries
    plt.axhline(y=150, color='black', linestyle='--', linewidth=1, alpha=0.5)
    plt.axvline(x=200, color='black', linestyle='--', linewidth=1, alpha=0.5)
    
    # Add text labels for quadrants
    plt.text(100, 75, 'Red\n[255,0,0]', ha='center', va='center', 
             color='white', fontweight='bold', fontsize=11)
    plt.text(300, 75, 'Green\n[0,255,0]', ha='center', va='center', 
             color='black', fontweight='bold', fontsize=11)
    plt.text(100, 225, 'Blue\n[0,0,255]', ha='center', va='center', 
             color='white', fontweight='bold', fontsize=11)
    plt.text(300, 225, 'White\n[255,255,255]', ha='center', va='center', 
             color='black', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    plt.savefig('task2_synthetic_image.png', dpi=100, bbox_inches='tight')
    print("\n✓ Image saved as 'task2_synthetic_image.png'")
    plt.show()

def demonstrate_array_slicing(image):
    """
    Demonstrate how array slicing was used to fill quadrants
    """
    print("\n--- ARRAY SLICING DEMONSTRATION ---")
    print("The image was created using spatial array slicing:")
    print("\n1. Top-Left Quadrant (Red):")
    print("   image[0:150, 0:200] = [255, 0, 0]")
    print(f"   Shape: {image[0:150, 0:200].shape}")
    
    print("\n2. Top-Right Quadrant (Green):")
    print("   image[0:150, 200:400] = [0, 255, 0]")
    print(f"   Shape: {image[0:150, 200:400].shape}")
    
    print("\n3. Bottom-Left Quadrant (Blue):")
    print("   image[150:300, 0:200] = [0, 0, 255]")
    print(f"   Shape: {image[150:300, 0:200].shape}")
    
    print("\n4. Bottom-Right Quadrant (White):")
    print("   image[150:300, 200:400] = [255, 255, 255]")
    print(f"   Shape: {image[150:300, 200:400].shape}")

def main():
    """
    Main function to execute Task 2
    """
    
    # Step 1: Create synthetic image
    print("\nCreating synthetic 300×400×3 image...")
    image = create_synthetic_image()
    
    # Step 2: Display metrics
    display_matrix_metrics(image)
    
    # Step 3: Show array slicing details
    demonstrate_array_slicing(image)
    
    # Step 4: Visualize
    print("\nGenerating visualization...")
    visualize_image(image)
    
    print("\n" + "="*60)
    print("TASK 2 COMPLETED SUCCESSFULLY")
    print("="*60)

if __name__ == "__main__":
    main()