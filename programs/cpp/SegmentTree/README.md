# 🌳 Segment Tree in C++

A clean and efficient **Segment Tree** implementation in C++ for **range sum queries** and **point updates**.  
This template is optimized for competitive programming and learning purposes.

---

## 🚀 Features

- Supports **range sum queries** in `O(log n)`
- Supports **point updates** in `O(log n)`
- Clean, minimal, and ready for reuse
- Easily adaptable for min, max, gcd, or custom operations

---

## 🧩 Example

### Input (inside code)
```cpp
vector<int> arr = {1, 3, 5, 7, 9, 11};
SegmentTree st(arr);
cout << st.query(1, 4) << "\n";
st.update(2, 10);
cout << st.query(1, 4) << "\n";
