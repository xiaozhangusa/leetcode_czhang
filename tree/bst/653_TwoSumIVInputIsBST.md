# 🌲 Two Sum IV - Input is a BST

Imagine you are a **Matchmaker** in a village where everyone lives in a very specific, organized way—a **Binary Search Tree (BST) village**. Your goal is to find two villagers whose ages sum exactly to a target number **K**.

---

## 🎭 The Analogies

### 1. The "Memory Wall" (Hash Set)
You walk through the village, house by house. At each door, you look at the villager's age. Before saying hello, you check your high-tech **"Complementary Notebook"**.
*   **Target Sum (K):** 10
*   **Villager age:** 4
*   **Search for:** Is anyone with age `10 - 4 = 6` already in my notebook?
*   **Action:** If yes, match found! If no, write "4" in the notebook and keep walking.

### 2. The "Sorting the Queue" (Flatten to Array)
BST villagers are already somewhat ordered, but the paths are winding. You ask everyone to come out and stand in a single straight line from youngest to oldest (In-order traversal). 
Now you have a **sorted array**. You put one scout at the **front** (youngest) and one at the **back** (oldest).
*   **Sum too small?** Move the front scout forward (older).
*   **Sum too big?** Move the back scout backward (younger).
*   **Sum exact?** Party time!

### 3. The "Pincer Movement" (BST Iterator)
Instead of making everyone stand in a line (which takes memory), you send two specialized "Tree Climbers" into the woods.
*   **Climber A (Smallest):** Always hunts for the smallest available node (In-order).
*   **Climber B (Largest):** Always hunts for the largest available node (Reverse In-order).
They meet in the middle, just like the Two-Pointer scouts, but they do it **live on the tree**.

---

## 🛠️ Approaches Compared

| Approach | Time | Space | Intuition |
| :--- | :--- | :--- | :--- |
| **Hash Set** | $O(N)$ | $O(N)$ | "The Forgetful Matchmaker" - needs a notebook. |
| **In-order Array** | $O(N)$ | $O(N)$ | "The Parade" - simple but takes space. |
| **BST Iterator** | $O(N)$ | $O(H)$ | "The Pincer Movement" - most efficient for memory ($H$ is height). |

---

## 💡 Why is the BST Iterator so cool?
In a balanced tree, the height $H$ is $\log N$. While $N$ could be 10,000, $\log N$ is only ~14. Using the Iterator approach is like bringing a small notepad instead of a giant ledger to the village!

---

## 🚀 Example Walkthrough
**Input:** `root = [5, 3, 6, 2, 4, null, 7], k = 9`

1.  **Start Browsing:** You find `2`. Complement needed: `9 - 2 = 7`. Not seen `7` yet. Save `2`.
2.  **Next:** You find `3`. Complement needed: `9 - 3 = 6`. Not seen `6` yet. Save `3`.
3.  **Next:** You find `4`. Complement needed: `9 - 4 = 5`. Not seen `5` yet. Save `4`.
4.  **Next:** You find `5`. Complement needed: `9 - 5 = 4`. **BINGO!** We saw `4` earlier.
5.  **Return:** `True`.
