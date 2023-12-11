import matplotlib.pyplot as plt  # to visualize data
from collections import Counter  # to calc modus


def calc_mean(data):
    jumlah_nilai = sum(data)
    jumlah_total_data = len(data)
    mean_value = jumlah_nilai / jumlah_total_data
    print(f"Mean: {mean_value}")
    return mean_value


def visualize_mean(data):
    mean_value = calc_mean(data)
    
    # Create a histogram
    plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='blue')

    # Add a vertical line at the mean
    plt.axvline(x=mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Mean = {mean_value:.2f}')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Mean')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()
    
    
def calc_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    index_tengah = n//2 # double slash // is used for floor division

    # Jika jumlah data genap, median adalah rata-rata dari dua nilai tengah 
    if n % 2 == 0:
        median1 = sorted_data[index_tengah]
        median2 = sorted_data[index_tengah - 1]
        median_value = (median1 + median2) / 2
    # Jika jumlah data ganjil, median adalah nilai tengah
    else:
        median_value = sorted_data[index_tengah]
        
    print(f"Median: {median_value}")
    return median_value


def visualize_median(data):
    median_value = calc_median(data)
    
    # Create a histogram
    plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='blue')

    # Add a vertical line at the mean
    plt.axvline(x=median_value, color='red', linestyle='dashed', linewidth=1, label=f'Median = {median_value:.2f}')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Median')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

    
def calc_modus(data):
    counter = Counter(data)
    mode_data = dict(counter) # ubah ke tipe data dictionary
    max_counter = max(list(counter.values())) # mencari data yang memiliki counter paling banyak
    mode_value = []
    for k, v in mode_data.items():
        if v == max(list(counter.values())):
            mode_value.append(k)
    print(f"Modus: {mode_value}")
    return mode_value


def visualize_modus(data):
    mode_value = calc_modus(data)
    
    # Create a histogram
    plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='green')

    # Add a vertical line at the mean
    plt.axvline(x=mode_value[0], color='red', linestyle='dashed', linewidth=1, label=f'Modus 1 = {mode_value[0]:.2f}')
    plt.axvline(x=mode_value[1], color='blue', linestyle='dashed', linewidth=1, label=f'Modus 2 = {mode_value[1]:.2f}')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Modes')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

    
def calc_range(data):
    nilai_tertinggi = max(data)
    nilai_terendah = min(data)
    data_range = max(data) - min(data)
    
    print(f"Range: {nilai_tertinggi} - {nilai_terendah} = {data_range}")  
    return data_range


def visualize_range(data):
    # Create a histogram
    plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='green')

    # Define the horizontal line coordinates
    y = 1.5 # The y-coordinate where the line will be drawn
    x1 = 4/70*1  # The x-coordinate of the start point
    x2 = 66/70*1  # The x-coordinate of the end point

    # Add a horizontal line
    plt.axhline(y=y, xmin=x1, xmax=x2, color='red', linestyle='dashed', linewidth=1, label=f'Range = {calc_range(data)}')

    # Add vertical line
    plt.axvline(x=min(data), color='blue', linestyle='dashed', linewidth=1, label=f'Min Data: {min(data):.2f}')
    plt.axvline(x=max(data), color='blue', linestyle='dashed', linewidth=1, label=f'Max Data: {max(data):.2f}')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Range')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()
    
    
def calc_variance(data):
    mean = calc_mean(data)
    
    # Kuadrat selisih antara setiap nilai data dengan rata-rata
    squared_diff = []
    for x in data:
        squared_diff_per_x = (x - mean)**2
        squared_diff.append( squared_diff_per_x )
    
    # Jumlah kuadrat selisih antara setiap nilai data dengan rata-rata, kemudian dibagi dengan jumlah total data
    variance = sum(squared_diff) / len(data)
    
    print(f"Variansi: {sum(squared_diff)} / {len(data)} = {variance}")    
    return variance


def calc_std(data):
    variance = calc_variance(data)
    standard_deviation = variance**0.5
    print(f"Standard Deviation: {variance}**0.5 = {standard_deviation}")
    return standard_deviation


def visualize_std(data):
    mean = calc_mean(data)
    standard_deviation = calc_std(data)
    
    # Buat histogram
    plt.hist(data, bins=30, edgecolor='black', alpha=0.5, color='green')

    # Tambahkan garis vertikal pada standar deviasi
    plt.axvline(x=mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean = {mean}')
    plt.axvline(x=mean - standard_deviation, color='blue', linestyle='dashed', linewidth=1, label=f'{mean-standard_deviation:.2f}')
    plt.axvline(x=mean + standard_deviation, color='blue', linestyle='dashed', linewidth=1, label=f'{mean+standard_deviation:.2f}')

    # Tambahkan label dan judul
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'Std Deviation = {standard_deviation:.2f}')

    # Tambahkan legenda
    plt.legend()

    # Tampilkan plot
    plt.show()
