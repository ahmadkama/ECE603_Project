# DeepSlice: Deep Learning for Network Slicing in 5G Networks

## Requirements
- Python 3.6+
- TensorFlow 2.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Running the Model

### Training the Deep Learning Model
To train the DeepSlice model:

1. Ensure you have the training dataset in CSV format with 8 input features and 1 output label
2. Run the training script:
   ```python
   python DeepSlice.py input_dataset.csv
   ```
3. The model will be trained and saved as 'network_slice_model.h5'
4. Training metrics and plots will be displayed showing accuracy and loss curves

## Running the Simulation
To run the simulation:

1. Modify the TTL value in the simulation script to the desired value
2. Run the simulation script:
   ```python
   python sim.py
   ```
3. The simulation will run and display the results

### Running the Simulation with Variations
To run the simulation with variations:

1. Run the simulation script:
   ```python
   python sim_variations.py
   ```
2. The simulation will run and display the results
