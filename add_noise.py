import json
import random

def add_sparse_noise(input_data, noise_level=10, num_noisy=5):
    noisy = input_data.copy()  # Copy original data
    indices = random.sample(range(len(input_data)), k=num_noisy)
    for idx in indices:
        noisy_val = noisy[idx] + random.uniform(-noise_level, noise_level)
        noisy_val = max(0, noisy_val)      # No negative values
        noisy_val = min(255, noisy_val)    # Clamp upper bound if needed
        noisy[idx] = noisy_val
    return noisy

def main():
    with open("data.json", "r") as f:
        original = json.load(f)

    noisy_data = {"data": []}

    for sample in original.get("data", []):
        noisy_input = add_sparse_noise(sample["input"], noise_level=10, num_noisy=random.randint(5,10))
        noisy_data["data"].append({
            "input": noisy_input,
            "output": sample["output"]
        })

    with open("data_noisy.json", "w") as f:
        json.dump(noisy_data, f)

    print(f"Noisy data saved to data_noisy.json ({len(noisy_data['data'])} samples)")

if __name__ == "__main__":
    main()
