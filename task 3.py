"""
Task 3: Channel Slicing & Isolation
HCI & Computer Graphics Lab 1

Load an image, extract RGB channels, and visualize in color and grayscale
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_or_create_sample_image():
    """
    Load image from file or create a sample image if file doesn't exist
    """
    try:
        # Try to load sample.jpg if it exists
        image = np.array(Image.open('sample.jpg'))
        print(f"✓ Loaded sample.jpg")
        print(f"  Image Shape: {image.shape}")
        return image
    except FileNotFoundError:
        print("⚠ sample.jpg not found. Creating sample image...")
        # Create a sample image if file doesn't exist
        # Create a 1080×1920×3 random image
        image = np.random.randint(0, 256, size=(1080, 1920, 3), dtype=np.uint8)
        print(f"✓ Created sample image")
        print(f"  Image Shape: {image.shape}")
        return image

def extract_channels(image):
    """
    Extract individual 2D channel intensity grids from RGB image
    """
    # Extract 2D intensity grids for each channel
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]
    
    return red_channel, green_channel, blue_channel

def create_single_channel_images(image, red_channel, green_channel, blue_channel):
    """
    Create 3D color arrays where only one channel is active
    """
    
    # Create red-only image (only R channel, G and B are 0)
    red_only = np.zeros_like(image)
    red_only[:, :, 0] = red_channel
    
    # Create green-only image (only G channel, R and B are 0)
    green_only = np.zeros_like(image)
    green_only[:, :, 1] = green_channel
    
    # Create blue-only image (only B channel, R and G are 0)
    blue_only = np.zeros_like(image)
    blue_only[:, :, 2] = blue_channel
    
    return red_only, green_only, blue_only

def print_channel_summary(image, red_channel, green_channel, blue_channel):
    """
    Print summary statistics for each channel
    """
    print("\n" + "="*60)
    print("TASK 3: Channel Slicing & Isolation")
    print("="*60)
    
    print("\n--- CHANNEL EXTRACTION SUMMARY ---")
    print(f"Original Image Shape : {image.shape}")
    print(f"Red Channel 2D Shape : {red_channel.shape} | Mean Intensity: {red_channel.mean():.2f}")
    print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {green_channel.mean():.2f}")
    print(f"Blue Channel 2D Shape : {blue_channel.shape} | Mean Intensity: {blue_channel.mean():.2f}")
    
    print("\n--- ADDITIONAL CHANNEL STATISTICS ---")
    print(f"Red Channel   - Min: {red_channel.min()}, Max: {red_channel.max()}, Std Dev: {red_channel.std():.2f}")
    print(f"Green Channel - Min: {green_channel.min()}, Max: {green_channel.max()}, Std Dev: {green_channel.std():.2f}")
    print(f"Blue Channel  - Min: {blue_channel.min()}, Max: {blue_channel.max()}, Std Dev: {blue_channel.std():.2f}")

def visualize_channels(image, red_channel, green_channel, blue_channel, red_only, green_only, blue_only):
    """
    Create 2×3 subplot layout showing color and grayscale channel views
    """
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('RGB Channel Extraction & Isolation', fontsize=16, fontweight='bold', y=0.995)
    
    # ===== TOP ROW: Color Images =====
    
    # Red-only (color image)
    axes[0, 0].imshow(red_only)
    axes[0, 0].set_title('Red Channel (Color View)', fontsize=12, fontweight='bold')
    axes[0, 0].axis('off')
    
    # Green-only (color image)
    axes[0, 1].imshow(green_only)
    axes[0, 1].set_title('Green Channel (Color View)', fontsize=12, fontweight='bold')
    axes[0, 1].axis('off')
    
    # Blue-only (color image)
    axes[0, 2].imshow(blue_only)
    axes[0, 2].set_title('Blue Channel (Color View)', fontsize=12, fontweight='bold')
    axes[0, 2].axis('off')
    
    # ===== BOTTOM ROW: Grayscale Intensity Maps =====
    
    # Red channel grayscale
    im1 = axes[1, 0].imshow(red_channel, cmap='gray')
    axes[1, 0].set_title('Red Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 0].axis('off')
    plt.colorbar(im1, ax=axes[1, 0], fraction=0.046, pad=0.04)
    
    # Green channel grayscale
    im2 = axes[1, 1].imshow(green_channel, cmap='gray')
    axes[1, 1].set_title('Green Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 1].axis('off')
    plt.colorbar(im2, ax=axes[1, 1], fraction=0.046, pad=0.04)
    
    # Blue channel grayscale
    im3 = axes[1, 2].imshow(blue_channel, cmap='gray')
    axes[1, 2].set_title('Blue Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 2].axis('off')
    plt.colorbar(im3, ax=axes[1, 2], fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    plt.savefig('task3_channel_extraction.png', dpi=100, bbox_inches='tight')
    print("\n✓ Visualization saved as 'task3_channel_extraction.png'")
    plt.show()

def demonstrate_slicing_techniques(image):
    """
    Demonstrate how channel slicing works in NumPy
    """
    print("\n--- CHANNEL SLICING TECHNIQUES ---")
    print("\nUsing NumPy axis indexing to extract channels:")
    
    print("\n1. Extract Red Channel (Axis 2, Index 0):")
    print("   red_channel = image[:, :, 0]")
    print(f"   Returns shape: {image[:, :, 0].shape}")
    
    print("\n2. Extract Green Channel (Axis 2, Index 1):")
    print("   green_channel = image[:, :, 1]")
    print(f"   Returns shape: {image[:, :, 1].shape}")
    
    print("\n3. Extract Blue Channel (Axis 2, Index 2):")
    print("   blue_channel = image[:, :, 2]")
    print(f"   Returns shape: {image[:, :, 2].shape}")
    
    print("\n4. Create single-channel color image:")
    print("   red_only = np.zeros_like(image)")
    print("   red_only[:, :, 0] = red_channel")
    print("   Now red_only has R values, G=0, B=0 for all pixels")

def main():
    """
    Main function to execute Task 3
    """
    
    # Step 1: Load or create sample image
    print("\n" + "="*60)
    print("Loading image...")
    print("="*60)
    image = load_or_create_sample_image()
    
    # Step 2: Extract channels
    print("\nExtracting color channels...")
    red_channel, green_channel, blue_channel = extract_channels(image)
    
    # Step 3: Create single-channel color images
    print("Creating single-channel color images...")
    red_only, green_only, blue_only = create_single_channel_images(
        image, red_channel, green_channel, blue_channel
    )
    
    # Step 4: Print summary
    print_channel_summary(image, red_channel, green_channel, blue_channel)
    
    # Step 5: Demonstrate slicing techniques
    demonstrate_slicing_techniques(image)
    
    # Step 6: Create visualization
    print("\nGenerating 2×3 subplot visualization...")
    visualize_channels(image, red_channel, green_channel, blue_channel, 
                      red_only, green_only, blue_only)
    
    print("\nDisplay Window : Matplotlib 2x3 Subplot Grid Rendered.")
    
    print("\n" + "="*60)
    print("TASK 3 COMPLETED SUCCESSFULLY")
    print("="*60)

if __name__ == "__main__":
    main()