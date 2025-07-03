import os
import time

# PATHS (UPDATE THESE IF NEEDED)
UNSORTED = r"C:\Python_Things\Unsorted_Estate_Docs"
SORTED = r"C:\Python_Things\Sorted_Estate_Docs"

# CATEGORIES (MODIFY KEYWORDS IF NEEDED)
CATEGORIES = {
    "Real Estate": ["deed", "property", "house"],
    "Financial": ["IRA", "401k", "bank"],
    "Personal Property": ["vehicle", "jewelry", "art"]
}

def wait_for_unlock(filepath, max_wait=10):
    """Wait until Windows releases file lock"""
    for _ in range(max_wait):
        try:
            with open(filepath, 'a') as f:
                return True  # File is unlocked
        except:
            time.sleep(1)
    return False

def atomic_copy(src, dst):
    """Nuclear-proof file copy"""
    try:
        # Read all content first
        with open(src, 'rb') as f_src:
            data = f_src.read()
        # Write to new location
        with open(dst, 'wb') as f_dst:
            f_dst.write(data)
        return True
    except Exception as e:
        print(f"❌ COPY FAILED: {os.path.basename(src)} - {str(e)}")
        return False

# MAIN SCRIPT
print("=== STARTING FILE SORTING ===")

# Create folders
for folder in CATEGORIES.keys():
    os.makedirs(os.path.join(SORTED, folder), exist_ok=True)

# Process files
for filename in os.listdir(UNSORTED):
    src = os.path.join(UNSORTED, filename)
    if not os.path.isfile(src):
        continue

    print(f"\nProcessing: {filename}")
    
    # Wait for file to unlock
    if not wait_for_unlock(src):
        print(f"⚠️ TIMEOUT: Could not access {filename}")
        continue

    # Read file content
    try:
        with open(src, 'r', errors='ignore') as f:
            content = f.read().lower()
    except Exception as e:
        print(f"⚠️ READ ERROR: {filename} - {str(e)}")
        continue

    # Find matching category
    moved = False
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in content:
                dst = os.path.join(SORTED, category, filename)
                if atomic_copy(src, dst):
                    try:
                        os.remove(src)
                        print(f"✅ MOVED: {filename} → {category}")
                        moved = True
                        break
                    except:
                        print(f"⚠️ COPIED BUT CAN'T DELETE ORIGINAL: {filename}")
                        moved = True
                        break
        if moved:
            break

    if not moved:
        print(f"❌ NO MATCH: {filename}")

print("\n=== COMPLETE ===")
print(f"Sorted files are in: {SORTED}")