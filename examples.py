import asyncio
import time
from dcache import dcache

# Example with a synchronous function
@dcache
def expensive_calculation(x, y):
    print(f"Calculating {x} + {y}...")
    time.sleep(2)  # Simulate expensive operation
    return x + y

# Example with an asynchronous function
@dcache
async def async_expensive_calculation(x, y):
    print(f"Async calculating {x} + {y}...")
    await asyncio.sleep(2)  # Simulate expensive async operation
    return x + y

# Example with required kwargs
@dcache(required_kwargs=["user_id"])
def get_user_data(user_id, include_details=False):
    print(f"Getting data for user {user_id}...")
    time.sleep(1)  # Simulate database query
    data = {"id": user_id, "name": f"User {user_id}"}
    if include_details:
        data["details"] = {"age": 30, "email": f"user{user_id}@example.com"}
    return data

async def main():
    # Test synchronous function
    print("First call (should compute):")
    result1 = expensive_calculation(5, 3)
    print(f"Result: {result1}")
    
    print("\nSecond call (should use cache):")
    result2 = expensive_calculation(5, 3)
    print(f"Result: {result2}")
    
    # Test asynchronous function
    print("\nFirst async call (should compute):")
    result3 = await async_expensive_calculation(10, 20)
    print(f"Result: {result3}")
    
    print("\nSecond async call (should use cache):")
    result4 = await async_expensive_calculation(10, 20)
    print(f"Result: {result4}")
    
    # Test with required kwargs
    print("\nFirst call with user_id (should compute):")
    result5 = get_user_data(user_id=123)
    print(f"Result: {result5}")
    
    print("\nSecond call with user_id (should use cache):")
    result6 = get_user_data(user_id=123)
    print(f"Result: {result6}")
    
    print("\nCall with different include_details (should still use cache):")
    result7 = get_user_data(user_id=123, include_details=True)
    print(f"Result: {result7}")
    
    print("\nCall with positional argument (should not use cache):")
    result8 = get_user_data(123)
    print(f"Result: {result8}")

if __name__ == "__main__":
    asyncio.run(main())