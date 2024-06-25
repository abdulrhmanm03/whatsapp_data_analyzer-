### Whatsapp data analyzer


!!! The readme file is not up to data will be updated soon


This FastAPI project provides endpoints to upload a whatsapp chat data file, process the data, and generate various plots. It includes functionality to upload data, generate time plots, and create pie charts.
 

## Features

- Upload file
- Generate time plots of message data
- Create pie charts of message data
- Automatically generated interactive API documentation


### Prerequisites

- Python 3.9+

### to run locally

1. Clone the repository:

    ```bash
    git clone https://github.com/abdulrhmanm03/whatsapp_data_analyzer-
    cd whatsapp_data_analyzer-
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the FastAPI application:

    ```bash
    uvicorn src.main:app --reload
    ```


### Access the API

Once the server is running, you can access the API documentation at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Getting the WhatsApp Chat Data

To use this FastAPI service, you need to export your WhatsApp chat data in a format that the application can process. Follow these steps to export your WhatsApp chat data:

### For Android:

1. **Navigate to the Chat**:
   - Open the individual or group chat you want to export.

2. **Access Chat Options**:
   - Tap the three dots (menu) in the top right corner.
   - Select "More" and then "Export chat".

3. **Choose Export Method**:
   - WhatsApp will ask whether you want to attach media files. Choose either "Without Media" as the app only support this for now

### For iPhone:

1. **Navigate to the Chat**:
   - Open the individual or group chat you want to export.

2. **Access Chat Options**:
   - Tap on the contact or group name at the top of the screen to open the chat info.
   - Scroll down and select "Export Chat".

3. **Choose Export Method**:
   - WhatsApp will ask whether you want to attach media files. Choose either "Without Media" as the app only support this for now

### Prepare the File for Upload:

1. **Check the File Format**:
   - Ensure the file is in `.txt` format, which is the format WhatsApp uses for exported chat data.

2. **Review the Content**:
   - Open the `.txt` file with a text editor to verify that it contains the chat data.




### Upload a File

You can upload a Whatsapp_data.txt file using the `/upload_file/` endpoint.

### Generate Plots

Use the `/plots/time_plot/` and `/plots/pie_plot/` endpoints to generate plots from the uploaded data.
Make share to upload the file first

## API Endpoints

### `POST /upload_file/`

- **Description**: Upload a CSV file and store its data.
- **Request**: `UploadFile`
- **Response**: JSON with the filename or an error message.

### `GET /plots/time_plot/`

- **Description**: Generate a time plot from the uploaded data.
- **Response**: JSON with the base64 encoded image of the time plot.

### `GET /plots/pie_plot/`

- **Description**: Generate a pie chart from the uploaded data.
- **Response**: JSON with the base64 encoded image of the pie chart.



