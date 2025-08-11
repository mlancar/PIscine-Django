
#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

FILE="requirements.txt"
VENV="django_venv"

echo -e "Creation of virtalenv: ${BLUE}'$VENV'${NC}"
python3 -m venv "$VENV"

echo -e "Activation of virtualenv: ${BLUE}'$VENV'${NC}"
source django_venv/bin/activate

if [ ! -f "$FILE" ]; then
    echo -e "${RED}ERROR: file '$FILE' not found${NC}"
    exit 1
fi

echo -e "Installation packages from ${BLUE}'$FILE'${NC}"

pip install --upgrade pip

if pip install -r "$FILE"; then
    echo -e "✅ ${GREEN}Installation Successfull${NC}"
else
    echo -e "❌ ${RED}Installation Failed${NC}"
    exit 1
fi