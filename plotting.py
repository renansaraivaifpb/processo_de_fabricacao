import serial
import matplotlib.pyplot as plt
import pandas as pd

plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2)  # Create subplots with 1 row and 2 columns

i = 0
x = []
y1 = []
y2 = []

# Create an empty DataFrame
df = pd.DataFrame(columns=['Tempo', 'percentual umidade', 'medicao umidade'])

ser = serial.Serial('COM3', 9600)
ser.close()
ser.open()
nome_arquivo = input("Digite o nome arquivo: ")
while True:
    # Read data from serial port
    data = ser.readline().decode().strip()
    print(data)

    # Split the data at the comma
    parts = data.split(', ')

    # Check if there are two parts
    if len(parts) == 2:
        # Extract and convert each part to float
        y1_val = float(parts[0])
        y2_val = float(parts[1])

        # Append data to lists
        x.append(i)
        y1.append(y1_val)
        y2.append(y2_val)

        # Add data to DataFrame
        new_data = pd.DataFrame({'Tempo': [i], 'percentual umidade': [y1_val], 'medicao umidade': [y2_val]})
        df = pd.concat([df, new_data], ignore_index=True)

        # Plot data on the first subplot
        ax1.plot(df['Tempo'], df['medicao umidade'], color='b')
        ax1.set_xlabel('Tempo')
        ax1.set_ylabel('Valor da umidade')
        ax1.set_title('Escala 0 a 1023')

        # Plot data on the second subplot
        ax2.plot(df['Tempo'], df['percentual umidade'], color='r')
        ax2.set_xlabel('Tempo')
        ax2.set_ylabel('Valor da umidade em %')
        ax2.set_title('Escala 0% a 100%')
        
        # Update the plot
        plt.tight_layout()
        plt.pause(0.001)

        # Increment counter
        i += 1

        # Save DataFrame to CSV
        df.to_csv(nome_arquivo+".csv", index=False)
