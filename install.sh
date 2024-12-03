#!/bin/sh

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3 and try again."
    exit 1
fi

# Create a temporary directory
TMP_DIR=$(mktemp -d)
echo "Created temporary directory at $TMP_DIR"

# Clone the repository
REPO_URL="https://github.com/your-username/your-repo.git"  # Replace with the actual repository URL
echo "Cloning repository from $REPO_URL..."
git clone $REPO_URL $TMP_DIR

# Change to the temporary directory
cd $TMP_DIR

# Build and install the package
echo "Building and installing the package..."
pip install .

# Inform the user
echo "Installation complete. The package has been installed."

# Clean up
echo "Cleaning up..."
rm -rf $TMP_DIR
echo "Temporary directory $TMP_DIR has been removed."