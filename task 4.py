"""
Task 4: Spatial Downsampling & Pixelation via Striding
HCI & Computer Graphics Lab 1

Perform spatial downsampling using NumPy striding and observe pixelation effects
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
        # Create a 1080×1920×3 image with gradient pattern
        height, width, channels = 1080, 1920, 3
        image = np.zeros((height, width, channels), dtype=np.uint8)
        
        # Create a gradient pattern for better visualization
        for i in range(height):
            for j in range(width):
                image[i, j, 0] = (i * 255) // height  # Red gradient
                image[i, j, 1] = (j * 255) // width   # Green gradient
                image[i, j, 2] = 128  # Blue constant
        
        print(f"✓ Created sample image with gradient pattern")
        print(f"  Image Shape: {image.shape}")
        return image

def downsample_image(image, N=8):
    """
    Downsample image using NumPy striding (taking every N-th pixel)
    
    Args:
        image: Input image array (H, W, C)
        N: Step factor (stride)
    
    Returns:
        Downsampled image array
    """
    # Use slice with step N to get every N-th pixel
    downsampled = image[::N, ::N, :]
    
    return downsampled

def re_expand_image(downsampled, original_shape, N=8):
    """
    Re-expand downsampled image back to original dimensions using np.repeat()
    This creates the blocky pixelation effect
    
    Args:
        downsampled: Downsampled image array
        original_shape: Target shape (H, W, C)
        N: Repeat factor (stride)
    
    Returns:
        Re-expanded image array
    """
    # Repeat each pixel N times along rows and N times along columns
    re_expanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)
    
    # Crop to exact original size (in case of rounding mismatches)
    re_expanded = re_expanded[:original_shape[0], :original_shape[1], :]
    
    return re_expanded

def calculate_metrics(original, downsampled):
    """
    Calculate compression and memory metrics
    
    Args:
        original: Original image array
        downsampled: Downsampled image array
    
    Returns:
        Dictionary with metrics
    """
    original_memory = original.nbytes
    downsampled_memory = downsampled.nbytes
    
    # Dimension reduction percentage
    dimension_reduction = ((1 - (downsampled.shape[0] / original.shape[0])) * 100)
    
    # Memory savings percentage
    memory_savings = ((1 - downsampled_memory / original_memory) * 100)
    
    # Calculate compression ratio
    compression_ratio = original_memory / downsampled_memory
    
    metrics = {
        'original_shape': original.shape,
        'downsampled_shape': downsampled.shape,
        'original_memory': original_memory,
        'downsampled_memory': downsampled_memory,
        'dimension_reduction': dimension_reduction,
        'memory_savings': memory_savings,
        'compression_ratio': compression_ratio
    }
    
    return metrics

def print_downsampling_analysis(metrics, N):
    """
    Print detailed downsampling analysis
    """
    print("\n" + "="*60)
    print("TASK 4: Spatial Downsampling & Pixelation via Striding")
    print("="*60)
    
    print(f"\n--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
    print(f"Original Shape : {metrics['original_shape']} | Memory: {metrics['original_memory']:,} bytes")
    print(f"Downsampled Shape : {metrics['downsampled_shape']} | Memory: {metrics['downsampled_memory']:,} bytes")
    print(f"Re-expanded Shape : {metrics['original_shape']} | Visual: Blocky Pixelation")
    print(f"Dimension Reduction: {metrics['dimension_reduction']:.2f}% reduction per axis")
    print(f"Memory Savings : {metrics['memory_savings']:.2f}% data reduction")
    
    print(f"\n--- COMPRESSION STATISTICS ---")
    print(f"Compression Ratio : {metrics['compression_ratio']:.2f}:1")
    print(f"Original Size : {metrics['original_memory'] / (1024**2):.2f} MB")
    print(f"Compressed Size : {metrics['downsampled_memory'] / 1024:.2f} KB")
    print(f"Data Loss : {100 - (metrics['downsampled_memory'] / metrics['original_memory'] * 100):.2f}%")

def demonstrate_striding_technique(image, N):
    """
    Demonstrate how striding works in NumPy
    """
    print(f"\n--- STRIDING TECHNIQUE (Step Factor = {N}) ---")
    print(f"\nDownsampling with NumPy striding:")
    print(f"   downsampled = image[::N, ::N, :]")
    print(f"   downsampled = image[::{N}, ::{N}, :]")
    print(f"\nThis takes every {N}-th pixel along rows and columns")
    
    print(f"\nRe-expansion with np.repeat():")
    print(f"   re_expanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)")
    print(f"\nThis repeats each pixel {N} times to fill the original space")
    
    print(f"\nExample with small 8×8 image:")
    print(f"   Original: [8, 8, 3]")
    print(f"   After [::4, ::4, :]: [2, 2, 3]")
    print(f"   After re-expand: [8, 8, 3] (but with {4}×{4} blocks)")

def visualize_downsampling(original, downsampled, re_expanded):
    """
    Create side-by-side comparison visualization
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Spatial Downsampling & Pixelation (N=8)', fontsize=16, fontweight='bold')
    
    # Original image
    axes[0].imshow(original)
    axes[0].set_title(f'Original Image\n{original.shape[0]}×{original.shape[1]}×{original.shape[2]}', 
                      fontsize=12, fontweight='bold')
    axes[0].axis('off')
    
    # Downsampled image (small)
    axes[1].imshow(downsampled)
    axes[1].set_title(f'Downsampled (N=8)\n{downsampled.shape[0]}×{downsampled.shape[1]}×{downsampled.shape[2]}', 
                      fontsize=12, fontweight='bold')
    axes[1].axis('off')
    
    # Re-expanded (pixelated)
    axes[2].imshow(re_expanded)
    axes[2].set_title(f'Re-expanded (Pixelated)\n{re_expanded.shape[0]}×{re_expanded.shape[1]}×{re_expanded.shape[2]}', 
                      fontsize=12, fontweight='bold')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig('task4_downsampling.png', dpi=100, bbox_inches='tight')
    print("\n✓ Visualization saved as 'task4_downsampling.png'")
    plt.show()

def create_detailed_comparison(original, downsampled, re_expanded):
    """
    Create a detailed comparison with zoomed-in regions
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Downsampling Analysis - Full & Zoomed Views', fontsize=16, fontweight='bold')
    
    # Row 1: Full images
    axes[0, 0].imshow(original)
    axes[0, 0].set_title('Original Image (Full)', fontsize=11, fontweight='bold')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(downsampled)
    axes[0, 1].set_title('Downsampled (Full)', fontsize=11, fontweight='bold')
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(re_expanded)
    axes[0, 2].set_title('Re-expanded (Full)', fontsize=11, fontweight='bold')
    axes[0, 2].axis('off')
    
    # Row 2: Zoomed-in regions (top-left corner)
    zoom_h = 200
    zoom_w = 200
    
    axes[1, 0].imshow(original[:zoom_h, :zoom_w, :])
    axes[1, 0].set_title('Original (Zoomed Top-Left)', fontsize=11, fontweight='bold')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(downsampled)
    axes[1, 1].set_title(f'Downsampled (Zoomed {8}×)', fontsize=11, fontweight='bold')
    axes[1, 1].axis('off')
    
    axes[1, 2].imshow(re_expanded[:zoom_h, :zoom_w, :])
    axes[1, 2].set_title('Re-expanded (Zoomed Top-Left)', fontsize=11, fontweight='bold')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    plt.savefig('task4_detailed_comparison.png', dpi=100, bbox_inches='tight')
    print("✓ Detailed comparison saved as 'task4_detailed_comparison.png'")
    plt.show()

def print_pixel_loss_analysis(metrics, N):
    """
    Print detailed pixel loss analysis
    """
    print(f"\n--- PIXEL LOSS ANALYSIS ---")
    
    original_height, original_width = metrics['original_shape'][:2]
    downsampled_height, downsampled_width = metrics['downsampled_shape'][:2]
    
    # Calculate actual pixels retained
    original_pixels = original_height * original_width
    downsampled_pixels = downsampled_height * downsampled_width
    
    print(f"Original pixels: {original_pixels:,}")
    print(f"Downsampled pixels: {downsampled_pixels:,}")
    print(f"Pixels retained: {(downsampled_pixels / original_pixels) * 100:.2f}%")
    print(f"Pixels discarded: {100 - (downsampled_pixels / original_pixels) * 100:.2f}%")
    
    print(f"\nWhen re-expanded with {N}×{N} blocks:")
    print(f"- Each downsampled pixel becomes a {N}×{N} block")
    print(f"- Original resolution restored but with visible pixelation")
    print(f"- Effective lossy compression due to spatial averaging")

def main():
    """
    Main function to execute Task 4
    """
    N = 8  # Step factor for downsampling
    
    # Step 1: Load or create sample image
    print("\n" + "="*60)
    print("Loading image...")
    print("="*60)
    original = load_or_create_sample_image()
    
    # Step 2: Downsample using striding
    print("\nDownsampling image using NumPy striding...")
    downsampled = downsample_image(original, N=N)
    
    # Step 3: Re-expand to original size
    print("Re-expanding image with pixelation effect...")
    re_expanded = re_expand_image(downsampled, original.shape, N=N)
    
    # Step 4: Calculate metrics
    print("Calculating compression metrics...")
    metrics = calculate_metrics(original, downsampled)
    
    # Step 5: Print analysis
    print_downsampling_analysis(metrics, N)
    
    # Step 6: Demonstrate technique
    demonstrate_striding_technique(original, N)
    
    # Step 7: Print pixel loss analysis
    print_pixel_loss_analysis(metrics, N)
    
    # Step 8: Create visualizations
    print("\nGenerating visualizations...")
    visualize_downsampling(original, downsampled, re_expanded)
    
    print("\nGenerating detailed comparison...")
    create_detailed_comparison(original, downsampled, re_expanded)
    
    print("\n" + "="*60)
    print("TASK 4 COMPLETED SUCCESSFULLY")
    print("="*60)

if __name__ == "__main__":
    main()