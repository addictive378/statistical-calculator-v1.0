def get_input_users():
    data = input("Enter data in the form of numbers to be calculated (separate with ,) : ")
    try:
        numbers = [float(num.strip()) for num in data.split(",")]
        return numbers
    except ValueError:
        print("Invalid input, enter only numbers separated by ,")
        return get_input_users()

def calculate_mean(numbers):
    sum_freq = {}
    for i in numbers:
        if i in sum_freq:
            sum_freq[i] += 1
        else:
            sum_freq[i] = 1
    sum_fx = sum(f * x for x, f in sum_freq.items())
    sum_f = sum(sum_freq.values())
    mean = sum_fx / sum_f
    return mean

def calculate_median(numbers):
    data_srt = sorted(numbers)
    n = len(data_srt)
    
    if len(data_srt) % 2 != 0:
        median_idx = n // 2
        return data_srt[median_idx]
    else:
        n1 = n // 2 - 1
        n2 = n // 2
        return (data_srt[n1] + data_srt[n2]) / 2
    
def calculate_modus(numbers):
    sum_freq = {}
    for i in numbers:
        if i in sum_freq:
            sum_freq[i] += 1
        else:
            sum_freq[i] = 1
        
        max_freq = max(sum_freq.values())
        modus = [key for key, value in sum_freq.items() if value == max_freq]
        if len(modus) == 1:
            return modus[0]
        return modus
    
def show_menu():
    print("\n=== Statistical Calculator Mean | Median | Modus ===")
    print("The version only supports single data, not group data.")
    print("Select the operation you want to perform:")
    print("1. Calculate Mean (Average)")
    print("2. Calculate Median")
    print("3. Calculate Modus")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter options 1 - 4: ")

        if choice == '4':
            print("Thanks for use this program!")
            break

        if choice in ['1', '2', '3']:
            numbers = get_input_users()
            if choice == '1':
                result = calculate_mean(numbers)
                print(f"Mean: {result}")
            elif choice == '2':
                result = calculate_median(numbers)
                print(f"Median: {result}")
            elif choice == '3':
                result = calculate_modus(numbers)  # Diperbaiki dari calculate_mean ke calculate_modus
                print(f"Modus: {result}")
        else:
            print("Invalid options, enter 1 - 4")

if __name__ == "__main__":
    main()