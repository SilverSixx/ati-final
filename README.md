## Requirements

Before running the app, you'll need to set up the environment with the required dependencies. Follow the steps below to install Conda, set up the environment, and run the Streamlit app.

If you don't have Conda installed, download and install it from [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Create the Conda Environment

Once Conda is installed, open your terminal or command prompt and run the following commands to set up your environment:

**1 .Clone the repository:**

```bash
git clone git@github.com:SilverSixx/ati-final.git
cd ati-final
```

**2. Create a Conda environment from the environment configuration file:**

```bash
conda create --name ati python=3.11  
```

**3. Activate the environment:**

```bash
conda activate ati
```

**4. Install the required dependencies: After activating the environment, install the necessary Python packages:**
```bash
pip install -r requirements.txt
```

## Run the Streamlit App

After installing the dependencies, you can now run the Streamlit app.

**Start the Streamlit app:**

```bash
streamlit run --server.port 8080 app.py 
```

This will open the Streamlit app in your default web browser. And follow what the app tells, you are half way done.