def build_tree(L):
    """
    Builds a tree-shaped ASCII art centered around its middle column.
    
    Growth Pattern Logic:
    1. Tiers: The tree is divided into L vertical sections (tiers).
    2. Height: Each tier 'i' has a height of i + 1.
       - Tier 1: 2 rows
       - Tier 2: 3 rows
       - Tier 3: 4 rows
    3. Stars: Within each tier, row 'j' has 2j - 1 stars (odd numbers: 1, 3, 5...).
       Example for Tier 2 (Height 3):
       Row 1: 2(1)-1 = 1 star  (*)
       Row 2: 2(2)-1 = 3 stars (***)
       Row 3: 2(3)-1 = 5 stars (*****)
    """
    if L < 1:
        return ""

    # --- Step 1: Calculate the structure ---
    # We store the number of stars for every single row in the tree.
    # We also keep track of max_stars to determine the total width of the grid.
    tiers = []
    max_stars = 0
    for i in range(1, L + 1):
        height = i + 1
        tier_rows = []
        for j in range(1, height + 1):
            stars = 2 * j - 1
            tier_rows.append(stars)
            # track the widest row of the whole tree
            if stars > max_stars:
                max_stars = stars
        tiers.append(tier_rows)

    # tiers becomes [[1, 3], [1, 3, 5], [1, 3, 5, 7]] for L=3

    # --- Step 2: Determine Grid Dimensions ---
    # The grid width is simply the widest row of stars.
    # The center (trunk position) is mid = width // 2.
    width = max_stars
    mid = width // 2
    output = []

    # --- Step 3: Build the rows ---
    # For each row with k stars, we calculate left padding to center it:
    # padding = mid - (k // 2)
    for tier in tiers:
        for stars in tier:
            left_padding = mid - (stars // 2)
            # Add row of stars with specific padding
            output.append(" " * left_padding + "*" * stars)
        # output becomes [' *', '***'] for L=1
        # then becomes [' *', '***', ' *', '***', '*****'] for L=2
        # then becomes [' *', '***', ' *', '***', '*****', ' *', '***', '*****', '*******'] for L=3
        
        # Add a blank separator line between tiers
        output.append("")

    # Remove the extra blank line added after the final tier
    if output and output[-1] == "":
        output.pop()

    # --- Step 4: Build the Trunk and Base ---
    # Trunk: A single '|' at the center.
    output.append(" " * mid + "|")

    # Base: Dash lines extending to the edges with a '+' in the center.
    # Length of dashes on each side is 'mid'.
    dash_side = mid
    output.append("—" * dash_side + "+" + "—" * dash_side)

    return "\n".join(output)

if __name__ == "__main__":
    # Example Demonstrations
    for l_val in [1, 2, 3]:
        print(f"Christmas Tree (L={l_val}):\n")
        print(build_tree(l_val))
        print("\n" + "="*30 + "\n")


build_tree(1)
