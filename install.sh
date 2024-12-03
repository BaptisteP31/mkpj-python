#!/bin/sh

ANSI_RED="\033[0;31m"
ANSI_GREEN="\033[0;32m"
ANSI_YELLOW="\033[0;33m"
ANSI_BLUE="\033[0;34m"
ANSI_RESET="\033[0m"

# Check for Python 3
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "Python 3 could not be found. Please install Python 3 and try again."
    exit 1
fi

echo "Using Python command: $PYTHON_CMD"

# Create a temporary directory
TMP_DIR=$(mktemp -d)
echo "Created temporary directory at $TMP_DIR"

# Clone the repository
REPO_URL="https://github.com/BaptisteP31/mkpj-python"
echo $ANSI_BLUE"Cloning repository $REPO_URL..." $ANSI_RESET
if ! git clone $REPO_URL $TMP_DIR; then
    echo $ANSI_RED"Failed to clone repository. Aborting installation." $ANSI_RESET
    rm -rf $TMP_DIR
    exit 1
fi

# Change to the temporary directory
cd $TMP_DIR

# Build and install the package
echo $ANSI_BLUE"Building and installing package..." $ANSI_RESET
$PYTHON_CMD -m pip install .

# Inform the user
echo $ANSI_GREEN"Installation complete." $ANSI_RESET

# Clean up
echo "Cleaning up..."
rm -rf $TMP_DIR
echo "Temporary directory $TMP_DIR has been removed."