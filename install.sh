#!/bin/bash
set -e

INSTALL_DIR="$HOME/.pomonotch"
BIN_DIR="$HOME/.local/bin"
REPO="https://github.com/Raaaphhh/PomoNotch.git"

echo "Installing PomoNotch..."

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "Updating existing installation..."
    git -C "$INSTALL_DIR" pull --quiet
else
    git clone --quiet "$REPO" "$INSTALL_DIR"
fi

chmod +x "$INSTALL_DIR/notch/notch_binary"

pip3 install --quiet -r "$INSTALL_DIR/requirements.txt"

mkdir -p "$BIN_DIR"
cat > "$BIN_DIR/pomonotch" << 'EOF'
#!/bin/bash
python3 "$HOME/.pomonotch/main.py" "$@"
EOF
chmod +x "$BIN_DIR/pomonotch"

if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.zshrc"
fi

if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC" 2>/dev/null; then
    echo '' >> "$SHELL_RC"
    echo '# PomoNotch' >> "$SHELL_RC"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
fi

echo ""
echo "PomoNotch installed! Open a new terminal tab and run: pomonotch"
