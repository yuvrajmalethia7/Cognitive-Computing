import random

# 1
print("1. List Operations")
L = [10, 20, 30, 40, 50, 60, 70, 80]
L += [200, 300]
L.remove(10)
L.remove(30)
print("Original List:", L)
L.sort()
print("Ascending Order:", L)
L.sort(reverse=True)
print("Descending Order:", L)
print()

# 2
print("2. Tuple Operations")
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
print("Highest Score:", max(scores), "at Index:", scores.index(max(scores)))
print("Lowest Score:", min(scores), "Count:", scores.count(min(scores)))
print("Reversed Tuple as List:", list(scores[::-1]))
user_score = int(input("Enter a score to check in the tuple: "))
if user_score in scores:
    print(f"{user_score} found at index {scores.index(user_score)}")
else:
    print(f"{user_score} is not in the tuple.")
print()

# 3
print("3. Random Numbers")
nums = [random.randint(100, 900) for _ in range(100)]
odds = [n for n in nums if n % 2 != 0]
evens = [n for n in nums if n % 2 == 0]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [n for n in nums if is_prime(n)]
print("Odd Numbers:", odds)
print("Even Numbers:", evens)
print("Prime Numbers:", primes)
print()

# 4
print("4. Set Operations")
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print("Union of A and B:", A | B)
print("Intersection of A and B:", A & B)
print("Symmetric Difference of A and B:", A ^ B)
print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))
x = int(input("Enter a score to remove from A: "))
if x in A:
    A.remove(x)
    print(f"{x} removed. Updated A:", A)
else:
    print(f"{x} not found in A.")
print()

# 5
print("5. Dictionary Key Rename")
places = {"city": "New York", "country": "USA"}
places["location"] = places.pop("city")
print("Updated Dictionary:", places)
