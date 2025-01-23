# Azure Functions Python App with Docker

This repository contains an Azure Functions application built with Python, designed to demonstrate a basic setup with multiple HTTP-triggered functions, environment variable usage, and deployment via Docker.

## Overview

This application includes two HTTP triggered functions:

*   `function1`: A GET endpoint that accepts query parameters (`name`, `age`).
*   `function2`: A POST endpoint that accepts a JSON body containing parameters (`name`, `city`).

Both functions utilize environment variables for demonstration purposes.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+:** [Download Python](https://www.python.org/downloads/)
*   **Azure Functions Core Tools:** [Install Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal&pivots=programming-language-python)
*   **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
*   **Azure CLI:** [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) (for Azure deployments)
*   **npm:** [Install npm](https://nodejs.org/en/download) (for installing azure function core tools)

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Set up a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    .venv/Scripts/activate # Windows
    source .venv/bin/activate  # macOS/Linux
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a local settings file** Create a `local.settings.json` based on the example below:
   ```json
        {
          "IsEncrypted": false,
          "Values": {
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AzureWebJobsStorage": "UseDevelopmentStorage=true",
            "OPENAI_API_KEY": "***",
            "TAVILY_API_KEY": "***"
          }
        }
   ```
   *   `AzureWebJobsStorage` can use a valid connection string or `UseDevelopmentStorage=true` if the Azure Storage Emulator is installed. If on macOS or Linux make sure to start the azurite container as specified below.
     *   **Docker Azure Storage Emulator (macOS/Linux):**
      *  Run docker image `mcr.microsoft.com/azure-storage/azurite`
        ```bash
        docker run -d -p 10000:10000 -p 10001:10001 -p 10002:10002 mcr.microsoft.com/azure-storage/azurite
        ```
        * Connection String you can use in this case:
        ```
          DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;
        ```

## Running Locally

1.  **Start the function app:**

    ```bash
    func start
    ```

2.  **Test the endpoints:**

    *   **Function 1 (GET):**
        Open your browser or use a tool like Postman to make a GET request to `http://localhost:7071/api/function1?name=John&age=30`

    *   **Function 2 (POST):**
        Use a tool like Postman to make a POST request to `http://localhost:7071/api/function2`. Set the `Content-Type` header to `application/json`, and use a body like:

        ```json
        {
            "name": "Jane",
            "city": "London"
        }
        ```

## Building the Docker Image

1.  **Build the image:**

    ```bash
    docker build -t my-function-app-image .
    ```

2.  **Test the docker image locally (optional):**

    ```bash
     docker run -p 8080:80 my-function-app-image
    ```
     *   Test by accessing the endpoints via your browser or via the tools you used before.
      *   **Function 1:** `http://localhost:8080/api/function1?name=John&age=30`
      *   **Function 2:** Use Postman or curl to make a POST request to `http://localhost:8080/api/function2`, set the `Content-Type` to `application/json`, and set the body with the JSON object.

## Deploying to Azure Container Registry (ACR)

1.  **Login to Azure CLI:**

    ```bash
    az login
    ```

2.  **Create an Azure Container Registry (ACR)** if you do not have one yet using the Azure portal.
    * You will need the Resource Group Name and ACR name for later steps.
    *   [Azure Container Registry (ACR) Documentation](https://learn.microsoft.com/en-us/azure/container-registry/)
3.  **Login to ACR:**

    ```bash
    az acr login --name <your-acr-name>
    ```

    Replace `<your-acr-name>` with the name of your ACR.

4.  **Tag the Docker image:**

    ```bash
    docker tag my-function-app-image <your-acr-name>.azurecr.io/my-function-app-image:v1
    ```
    Replace `<your-acr-name>` with the name of your ACR.

5.  **Push the image to ACR:**

    ```bash
    docker push <your-acr-name>.azurecr.io/my-function-app-image:v1
    ```

6.  **Create a Function App using the Azure Portal** selecting "Docker Container" as the publish method (not "Code").
    *   When creating, configure the Docker image source, choosing "Azure Container Registry" and your ACR details.
    *   Provide the Image and Tag you pushed to ACR: `<your-acr-name>.azurecr.io/my-function-app-image:v1`.
    *   [Docker with Azure Functions Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-create-function-app-linux-container)

7.  **Test:** Test your function app by accessing the provided URLs.

## Azure Resources

*   **Azure Functions Documentation:**
    [https://learn.microsoft.com/en-us/azure/azure-functions/](https://learn.microsoft.com/en-us/azure/azure-functions/)
*   **Azure Functions Python Developer Guide:**
    [https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
*  **Azure Functions Core Tools Documentation:**
     [https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal&pivots=programming-language-python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal&pivots=programming-language-python)
*   **Azure CLI Documentation:**
    [https://learn.microsoft.com/en-us/cli/azure/](https://learn.microsoft.com/en-us/cli/azure/)

## Important Notes

*   **Environment Variables:** When deploying to Azure, manage environment variables in the Function App's "Configuration" settings in the Azure portal.
*   **Secrets Management:** For production, consider using Azure Key Vault for secure secrets management.
*   **`local.settings.json`:** The `local.settings.json` file should **not** be checked into source control, as it may contain sensitive information.
*   **Port 80:** Azure Functions requires the container to listen on port 80.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues for improvements.

## License

This project is licensed under the MIT License.
