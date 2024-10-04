# Simple NFT Application

This is a basic Non-Fungible Token (NFT) application built with Python (Flask) for the backend and HTML/JavaScript for the frontend. It demonstrates the core concepts of creating, transferring, and viewing NFTs.

## Features

- Create new NFTs with a name, description, and owner
- Transfer NFTs between users
- View all NFTs owned by a specific user

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Setup

1. Clone this repository or download the source code.

2. Navigate to the project directory in your terminal.

3. Install the required Python package (Flask) by running:

   ```
   pip install flask
   ```

4. Ensure you have two files in your project directory:
   - `app.py` (Backend)
   - `index.html` (Frontend)

## Running the Application

1. In the project directory, run the following command to start the Flask server:

   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000`

3. You should now see the NFT application interface.

## Usage

### Creating an NFT

1. Fill in the "NFT Name", "NFT Description", and "Owner ID" fields.
2. Click the "Create NFT" button.
3. An alert will show the ID of the newly created NFT.

### Transferring an NFT

1. Enter the "NFT ID" of the NFT you want to transfer.
2. Enter the "New Owner ID" for the NFT.
3. Click the "Transfer NFT" button.
4. An alert will confirm the transfer.

### Viewing User's NFTs

1. Enter a "User ID" in the provided field.
2. Click the "Get User's NFTs" button.
3. The NFTs owned by the specified user will be displayed below.

## Notes

- This application uses in-memory storage, so all data is lost when the server is stopped.
- This is a demonstration application and is not suitable for production use without significant enhancements.

## Future Improvements

- Implement persistent storage (database)
- Add user authentication and authorization
- Enhance the user interface
- Implement actual blockchain functionality for a more realistic NFT experience

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
